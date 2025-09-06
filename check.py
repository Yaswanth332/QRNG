import requests

# Replace with your deployed endpoint

# Replace with your actual API key from Render environment
headers = {
    "x-api-key": "12345-ABCDE"
}

Random_Bits=" https://qrng-api.onrender.com/api/random-bits?length=6"

Random_Integer="https://qrng-api.onrender.com/api/random-int?min=0&max=100"

Random_Float="https://qrng-api.onrender.com/api/random-float?min=0.0&max=1.0"
# Make the GET request
url={
    "Random_Bits":Random_Bits,
    "Random_Integer":Random_Integer,
    "Random_Float":Random_Float
}
for i,j in url.items():
    response = requests.get(j, headers=headers)
    # Check the response
    if response.status_code == 200:
        print(f"{i} request was successful")
    else:
        print(f"{i} request failed with status code {response.status_code}")
    print(response.json())
    print("\n")
    