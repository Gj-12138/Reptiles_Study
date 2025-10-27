import random
import re
import time

import requests

with open(f"../static/笔趣阁_神秘复苏.txt","w",encoding="utf-8") as f:
    i = 7
    while i < 20:
        url = f"https://www.d3016ba0.icu/book/65055/{i}.html"
        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
        }
        response  = requests.get(url,headers=headers)
        # print(response.text)
        # print(response.status_code)
        pat = re.compile(r'<div[^>]*id="chaptercontent"[^>]*>(.*?)(?:请收藏本站：https://www.bqg78.com|</div>)', re.S)
        txt = re.sub(r'<br\s*/?>|\s*https?://[\w./]+', '', pat.search(response.text).group(1))
        txt = re.sub(r'\s+', ' ', txt).strip()
        i+=1
        print(txt)
        f.write(txt+ '\n\n')
        time.sleep(random.uniform(1, 2))