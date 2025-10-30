# https://www.gamer520.com/page/1
import re

import requests
max_index_page = 940
url = "https://www.gamer520.com/page/3"
response = requests.get(url)
print(response.status_code)
# print(response.text)
index_text = response.text

index_result = re.findall(r'<article.*?>.*?'
                          r'<div class="placeholder" style="padding-bottom: 56.315789473684%;">.*?'
                          r'<a\b[^>]*href="(.*?)">.*?'
                          r'<img.*?data-src="(.*?)" src=".*?" alt="(.*?)">.*?'
                          r'</a>.*?'
                          r'</div>.*?'
                          r'</article>',index_text,re.S)
for item in index_result:
    print(item)

