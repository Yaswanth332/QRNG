import requests

# Replace with your deployed endpoint
url = "https://qrng-api.onrender.com/api/random-bits?length=8"

# Replace with your actual API key from Render environment
headers = {
    "x-api-key": "12345-ABCDE"
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    print("Success! API Response:")
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
