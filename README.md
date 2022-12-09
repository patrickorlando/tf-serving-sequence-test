# tf-serving-sequence-test
Testing how Tensorflow Serving handles variable length sequences as input. In the context of session-based recommender models.

Particularly in the case where we use transformer encoders for the user's item interaction sequence, padding every single request to
the maximum sequence length will result in a lot of wasted compute.
This dummy model tests the behaviour of tf-serving when the sequence length varies.

## Outcome:
1. You **cannot** have ragged inputs in a single request.
    ```json
    {
      "instances": [
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4, 5]
      ]
    }
    ```
2. You **can** have different sequence length in different requests, **without** request batching enabled.
  If batching is enabled you get this error:
    ```
    '{
      "error": "Tensors with name \'serving_default_lambda_input:0\' from different tasks have different shapes and padding is turned off. 
      Set pad_variable_length_inputs to true, or ensure that all tensors with the same name have equal dimensions starting with the first dim."
    }'
    ```
3. There's no documentation for the parameter ``, but enabling it causes the server to abort, with the error:
    ```
    2022-12-09 00:39:00.445797: F external/org_tensorflow/tensorflow/core/framework/tensor_util.cc:94] Check failed: offset + from_data.size() <= to_data.size() (1880 vs. 120)
    /usr/bin/tf_serving_entrypoint.sh: line 3:     7 Aborted                 tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} "$@"
    ```
