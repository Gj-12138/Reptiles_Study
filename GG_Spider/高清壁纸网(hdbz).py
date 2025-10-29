# https://www.hdbz.net/ # 首页
import re
from tokenize import cookie_re

import requests


# url = "https://www.hdbz.net/"
#
# index_response = requests.get(url)
#
# print(index_response.url)
# print(index_response.status_code)
# index_html = index_response.content.decode('utf-8')
# index_re = re.compile(r'<a href="([^"]+)" target="_blank" title="(.*?)" data-resolution=".*?" class="item">.*?'
#                       r'<img src=".*?" data-original="(.*?)" alt=".*?" class="lazy" />.*?<div class="resolution">.*?</div>.*?'
#                       r'<div class="title">.*?</div>.*?</a>',re.S)
# index_result = index_re.findall(index_html)
# # print(index_result)
# for item in index_result:
#     # print(item)
#     detail_path=item[0]
#     detail_img = item[2]
#
#     detail_url="https://www.hdbz.net"+detail_path
#     # print(detail_path)
#     # print(detail_img)
#     detail_html = requests.get("detail_url")
#     # print(detail_html.content.decode('utf-8'))
#     # print(detail_html.status_code)
#     # text = '<div class="pic-preview"><img alt="创：战神 4K壁纸(3840x2160)" src="https://img.hdbz.net/thumbs/2025/1023/180093.jpg?x-oss-process=style/w_1330-h_870" /></div>'
#     detail_text = detail_html.content.decode('utf-8')
#     detail_result = re.findall('<div class="pic-preview">.*?'
#                                '<img alt=".*?" src="(.*?)" />',detail_text,re.S)
#     print(detail_result)

# cookie
# login_cookies = {
#     'unotify' :'4f3235c2b40adc7f5be926175a1bf8fa'
# }
# 登录的请求地址： https://vip.hdbz.net/auth/ajaxlogin

# login_url =  "https://vip.hdbz.net/auth/ajaxlogin"
#
# session01 = requests.Session()
# # username: userName, userpwd: userPwd
# login_data = {
#     "username":"19293307187",
#     "userpwd":"Qikuedu123"
# }
#
# login_response = session01.post(login_url, data=login_data)
# print(login_response.text)

# 收藏： https://vip.hdbz.net/site/ImageStore

# collect_url = "https://vip.hdbz.net/site/ImageStore"
# collect_data = {
#     "aid": "180093",
#     "imageurl": "/wallpaper/202510/180093.html"
# }
# collect_response = session01.post(collect_url,data=collect_data)
# print(collect_response.text)


