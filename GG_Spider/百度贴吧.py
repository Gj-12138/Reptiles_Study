# https://tieba.baidu.com/t/f/
import re
import time

from curl_cffi import requests

url = "https://tieba.baidu.com/t/f/"
print("启动")
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
response = requests.get(url)
# print(response.url)
# print(response.status_code)
# print(response.text)

# <a class="each_topic_entrance_item" data-fid="2753" href="//tieba.baidu.com/t/f/2753">清华大学</a>

datas = re.findall(r'<a.*?class="each_topic_entrance_item".*?href="(.*?)".*?data-fid="(.*?)">(.*?)</a>',response.text,re.S)
# print(datas)
for data in datas:
    time.sleep(1)
    # print(data)
    # ('//tieba.baidu.com/t/f/25439', '25439', ' 西安交通大学')
    detail_url = f"https:{data[0]}"
    # print(detail_url)
    detail_response = requests.get(detail_url)
    # print(detail_response.text)
    detail_datas = re.findall(r'<h1 class="forum_name">(?P<title>.*?)</h1>.*?'
                       r'<span class="about_name">关注:</span>.*?<span class="about_value">(?P<guanzhu>.*?)</span>.*?'
                       r'<span class="about_name">帖子:</span><span class="about_value">(?P<tiezi>.*?)</span>.*?'
                       r''
                       ,detail_response.text,re.S)
    for detail_data in detail_datas:
        print({
            "学校":detail_data[0],
            "关注":detail_data[1],
            "帖子":detail_data[2],
        })

