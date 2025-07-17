import requests
import claves

API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = claves.chiave_news

params = {
    "country": "us",
    "apiKey": API_KEY,
    "pageSize": 1
}

response = requests.get(API_URL, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")