# Import the os module to access environment variables
import os

# Import the load_dotenv() function to load variables from a .env file
from dotenv import load_dotenv

# Import the requests library to send HTTP requests to the News API
import requests

# Load all environment variables from the .env file
load_dotenv()

# Retrieve the API key stored in the .env file
api_key = os.getenv("NEWS_API_KEY")

# Ask the user to enter the type of news they want to search for
query = input("What type of news are you interested in? ")

# Create the News API URL using the user's query and the API key
url = (
    f"https://newsapi.org/v2/everything?"
    f"q={query}&sortBy=publishedAt&apiKey={api_key}"
)

# Send a GET request to the News API
response = requests.get(url)

# Convert the JSON response into a Python dictionary
news = response.json()

# Loop through each news article in the response
for article in news["articles"]:
    # Print the title of the article
    print(article["title"])

    # Print the description of the article
    print(article["description"])

    # Print a separator line to distinguish between articles
    print("-" * 50)
