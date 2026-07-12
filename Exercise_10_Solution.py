import requests
import json

query = input("What type of news are you interested in?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-03-01&sortBy=publishedAt&apiKey=04ff4aaeabc6404c8c58cdf016576275"
r = requests.get(url)
news = json.loads(r.text)
print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------")