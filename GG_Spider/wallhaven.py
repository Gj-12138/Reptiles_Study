# <figure class="thumb thumb-qrzy75 thumb-sfw thumb-general" data-wallpaper-id="qrzy75" style="width:300px;height:200px">
import random
import re
import time

import requests

# https://wallhaven.cc/hot?page=1
i = 1
while True:
    url = f"https://wallhaven.cc/hot?page={i}"
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text)
    img_items = re.findall(r'data-wallpaper-id="(.+?)"', response.text)
    # img_items_length = img_items.__len__()
    if not(img_items):
        print("页面结构或已变化")
        break
    n = 1
    for img_item in img_items:
        # print(img_item)
        img_group = img_item[:2]
        # print(img_group)
        with open(f"../static/page-{i}-{n}.jpg", "wb") as f:
            response_img = requests.get(f"https://w.wallhaven.cc/full/{img_group}/wallhaven-{img_item}.jpg")
            time.sleep(random.uniform(1, 2))
            f.write(response_img.content)
            print(f"当前图片为：page_{i}_{n}.jpg")
        n+=1

    i += 1
    if i >= 2:
        break