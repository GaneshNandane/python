# Import the requests library for sending HTTP requests
import requests

# URL of the API endpoint where the POST request will be sent
url = "https://api.example.com/login"

# Define the request headers
headers = {
    # Identify the client making the request
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",

    # Specify that the request body is in JSON format
    "Content-Type": "application/json"
}

# Data to be sent to the server in JSON format
data = {
    "Username": "myusername",
    "password": "mypassword"
}

# Send a POST request with the headers and JSON data
response = requests.post(url, headers=headers, json=data)

# Print the response received from the server
print(response.text)
