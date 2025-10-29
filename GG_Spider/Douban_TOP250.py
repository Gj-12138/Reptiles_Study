"""
Python爬虫抓取豆瓣TOP250数据
"""
import json
import re
import time
import requests


import logging



f=open(f"../static/top250.txt",mode="w",encoding='utf-8')
page = 0
for i in range(0,251,25):
    time.sleep(1)
    url = f"https://movie.douban.com/top250?start={i}&filter="
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
    }
    response = requests.get(url,headers=headers)
    # print(response.text)
#     # 编写正则表达式
    obj = re.compile(r'<div class="item">.*?'
                     r'<a href="(?P<details_url>.*?)">.*?<img width="100" alt=".*?" src="(?P<move_img_url>.*?)">.*?</a>.*?'
                     r'<span class="title">(?P<name>.*?)</span>.*?'
                     r'<div class="bd">.*?<p>.*?导演: (?P<dao>.*?)&nbsp;'
                     r'.*?<br>(?P<year>.*?)&nbsp;'
                     r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*?<span>(?P<num>.*?)人评价</span>', re.S)

    # 进行正则匹配
    result = obj.finditer(response.text)
    for item in result:
        # print(item)
        name = item.group("name")
        dao = item.group("dao")
        year = item.group("year").strip()  # 去掉字符串两侧的空白
        score = item.group("score")
        num = item.group("num")
        move_img_url=item.group("move_img_url")
        details_url=item.group("details_url")
        move = {
            "电影名":name,
            "导演":dao,
            "年份":year,
            "评分":score,
            "点评人数":num,
            "电影海报url":move_img_url,
            "详情页url":details_url,
        }
        f.write(json.dumps(move,ensure_ascii=False)+"\n")
        # print(move)
    page+=1
    print(f"第{page}页爬取完成")

f.close()




