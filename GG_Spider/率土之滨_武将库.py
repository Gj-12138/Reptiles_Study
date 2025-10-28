import requests

# https://stzb.163.com/card_list.html
# 找到爬取地址
url = "https://g0.gph.netease.com/ngsocial/community/stzb/cfg/hero_extra.json?gameid=g10"
response = requests.get(url)
print(response.status_code)
print(response.url)
# print(response.text)
for item in response.json():
    # print(item)
    iconid = item.get('iconId')
    # print(iconid)
    print(f"https://g0.gph.netease.com/ngsocial/community/stzb/cn/cards/cut/card_small_{iconid}.jpg?gameid=g10")
