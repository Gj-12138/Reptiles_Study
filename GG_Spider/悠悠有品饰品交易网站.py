# https://www.youpin898.com/
import json

import requests

# https://www.youpin898.com/market

# 分类列表
# https://api.youpin898.com/api/youpin/commodity/v2/commodity/tag/query/list


# https://api.youpin898.com/api/homepage/pc/goods/market/querySaleTemplate

url = "https://api.youpin898.com/api/homepage/pc/goods/market/querySaleTemplate"
headers ={
    'Host': 'api.youpin898.com',
    'platform': 'pc',
    'appType': '1',
    'App-Version': '5.27.0',
    'AppVersion': '5.27.0',
    'secret-v': 'h5_v1',
    'Content-Type': 'application/json',
    'Origin': 'https://www.youpin898.com',
    "referer": "https://www.youpin898.com/",
    "deviceid":"620181a4-693d-4fac-a331-782377891fc5",
    "deviceuk":"5FRtdplFAZeKXFuK0rw0UYaIeIzIT3l7AU0C47nz88YC6oXJj84wtX0MLMGhkUP1G",
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
    "uk":"5FRtKy4HAHM93HltDy2sKqMvoTaPOq7oeJN21D62dKZyx5VEWVFUT1YISyIkb651G",
    "authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5MTk1NDNjMTk1Njk0ZGM0YjFiNWZhOTg2YWE2MzY0MiIsIm5hbWVpZCI6IjMxMjYzNDAiLCJJZCI6IjMxMjYzNDAiLCJ1bmlxdWVfbmFtZSI6IkdK5qGA5qGA5qGAIiwiTmFtZSI6IkdK5qGA5qGA5qGAIiwidmVyc2lvbiI6IkJnWiIsIm5iZiI6MTc2MTcwODc3NiwiZXhwIjoxNzYyNTcyNzc2LCJpc3MiOiJ5b3VwaW44OTguY29tIiwiZGV2aWNlSWQiOiI2MjAxODFhNC02OTNkLTRmYWMtYTMzMS03ODIzNzc4OTFmYzUiLCJhdWQiOiJ1c2VyIn0.rOqlCwf8DnDcN5Id7XujKBTAhPhzbPJbkHYKaPqRhrM",
}
pageIndex_max=1246
for i in range(pageIndex_max):
    payload = {"listSortType":0,"sortType":0,"pageSize":20,"pageIndex": i}
    response = requests.post(url,headers=headers,data=json.dumps(payload), timeout=10)
    # print(response.url)
    # print(response.status_code)
    print(response.text)
