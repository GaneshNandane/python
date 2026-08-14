import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"

# Send a GET request to the webpage
response = requests.get(url)

# Raise an error if the request was unsuccessful
response.raise_for_status()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Print the formatted HTML of the webpage
print(soup.prettify())

# Find and print all <h2> headings from the webpage
for heading in soup.find_all("h2"):
    print(heading.get_text(strip=True))

# URL of the API where the data will be sent
url = "https://jsonplaceholder.typicode.com/posts"

# Data to send to the API
data = {
    "title": "harry",
    "body": "bhai",
    "userId": 12,
}

# Specify that the request body contains JSON data
headers = {
    "Content-Type": "application/json; charset=UTF-8"
}

# Send the data to the API using a POST request
response = requests.post(url, headers=headers, json=data)

# Raise an error if the request was unsuccessful
response.raise_for_status()

# Print the response returned by the API
print(response.text)
