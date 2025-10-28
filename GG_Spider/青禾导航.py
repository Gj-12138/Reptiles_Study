import re

import requests
from bs4 import BeautifulSoup, NavigableString

url = "https://www.qhdh.top/"
response = requests.get(url)
print(response.url)
print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
for card in soup.select('.url-card'):
    a = card.select_one('a[data-id]')
    if a.select_one('strong') is None:
        break
    else:
        name = a.select_one('strong').get_text(strip=True)
    if a.select_one('p') is None:
        info = " "
    else:
        info = a.select_one('p').get_text(strip=True)

    href = a['href']
    print({
        '名字':name ,
        '简介':info ,
        '网站地址': href,
    })

