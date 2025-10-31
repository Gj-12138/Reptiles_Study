# https://baike.baidu.com/#home
from curl_cffi import requests

# https://baike.baidu.com/item/%E7%A5%9E%E8%88%9F%E4%BA%8C%E5%8D%81%E4%B8%80%E5%8F%B7/65042368?fromModule=home_hotspot


url = "https://dlswbr.baidu.com/heicha/mw/abclite-2020-s.js"

# session = requests.Session()
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "ab_sr":"1.0.1_YTg2NjI0YmRiNjNiNjU0OGQ1NDJhZGNiMjA5NjA4OWQzYjY5NDFhNmM1YzRhYTdjZTE3ODU1MzE5NTAyMzE4NjUzY2QwYjQ2MjkyYTczZDBkNTM5NGFmODQ0NjdkYjFkNGQ5NGI0N2U1NmE5MTg0MTE4NGE4N2QwNTZhY2QwZjNmZTdhMDE3ZWQwNTRlNWNlY2MzZmMyMzlhODA0OGE5OQ=="
}
# home_respnse = session.get(url,headers = headers)

respnse = requests.get("https://baike.baidu.com/item/%E7%A5%9E%E8%88%9F%E4%BA%8C%E5%8D%81%E4%B8%80%E5%8F%B7/65042368?fromModule=home_hotspot",headers = headers)
print(respnse.text)



