import requests


url = "https://steamcommunity.com/market/search?appid=730"
response = requests.get(url)
print(response.url)
print(response.status_code)
print(response.text)