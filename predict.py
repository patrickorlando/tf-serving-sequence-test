import asyncio
import aiohttp

async def fetch(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            return await response.text()

async def main():
    # Define the URL to make the request to
    url = "http://localhost:8501/v1/models/test_model.tf:predict"

    model_inputs = [
        list(range(10)),
        [list(range(10)),list(range(10))],
        [list(range(5)),list(range(5))]
    ]
    # Define the data to include in the JSON payload
    payloads = [
        {"instances": [x]}
        for x in model_inputs
    ]

    # Make the request and print the response
    # Loop over the data payloads and make requests with each one
    responses = [fetch(url, data) for data in payloads]
    responses = await asyncio.gather(*responses)
    print(responses)

# Run the main() function
asyncio.run(main())