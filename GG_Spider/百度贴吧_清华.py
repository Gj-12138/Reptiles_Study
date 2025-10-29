import requests

url = "https://tieba.baidu.com/t/f/?class=college/"
print("启动")
response = requests.get(url)
# print(response.url)
# print(response.status_code)
print(response.text)