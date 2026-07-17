import requests

# Send a GET request to Google's homepage
response = requests.get("https://www.google.com")

# Print the HTML content of the webpage
print(response.text)
