import tensorflow as tf

def slice_tensor(x: tf.Tensor) -> tf.Tensor:
    return x[:,:5]

def build_model():
    slice_layer = tf.keras.layers.Lambda(slice_tensor)

    model = tf.keras.Sequential(slice_layer)

    example_input = tf.ragged.range([4,7,9]).to_tensor(0)

    model_output = model(example_input)

    model.save("test_model.tf/1")

if __name__ == "__main__":
    build_model()