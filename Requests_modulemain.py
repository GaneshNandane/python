import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)

Soup = BeautifulSoup (r.text,'html.parser')
print(Soup.prettify())
for heading in Soup.find_all("h2"):
    print(heading.text)
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title":"harry",
    "body":"bhai",
    "userID": 12,
}
headers = {
    "Content-type":"application/json;charset =UTF-8"
}
response = requests.post(url, headers = headers, json = data)
print(response.text)