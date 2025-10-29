import requests

url = "https://tieba.baidu.com/t/f/2753#"



response = requests.get(url)
print(response.url)
print(response.status_code)
print(response.text)