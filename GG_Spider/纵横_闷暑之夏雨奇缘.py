import random
import re
import time

import requests

next_id = 64083373
i = 0
while True:
    url = f"https://read.zongheng.com/chapter/991141/{next_id}.html"
    html = requests.get(url).text
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text)
    pat = re.compile(r'<div[^>]*class="content"[^>]*>(.*?)</div>', re.S)
    txt = re.sub(r'<p>', '', pat.search(response.text).group(1))
    txt = re.sub(r'</p>', '\t', txt).strip()
    next_id = re.search(r'data-nextcid="(\d+)"', response.text).group(1)
    # print(next_id)
    print(txt)
    i+=1
    if i>=3:
        print("已达设定目标")
        break
    if next_id == "0":
        print("文章结束")
        break
    time.sleep(random.uniform(1, 2))
