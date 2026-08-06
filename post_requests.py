import requests
url = "https://api.example.com/login"
headers = {
    "User-Agent":"Mozilla/5.0 (windows NT 10.0, win64; X64) AppleWebkit/537.36 (kHTML, like Gecko) chrome/58.03029.110 safari/537.36","Content-Type":"application/json"
}
data = {
    "Username":"myusername",
    "password":"mupassword"
}
response = requests.post(url, headers = headers,json = data)
print(response.text)