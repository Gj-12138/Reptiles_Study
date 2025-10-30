# https://product.weather.com.cn/alarm/grepalarm_cn.php?_=1761801814758
import json
import random
import time

import requests

time_stamp01=int(time.time()*1000)

# print(time_stamp)

url = f"https://product.weather.com.cn/alarm/grepalarm_cn.php?_={time_stamp01}"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
    "referer":"https://www.weather.com.cn/",
}

response = requests.get(url,headers=headers)
res_test = response.content.decode('utf-8')
json_data = res_test[14:-1]
datas =json.loads(json_data)
for data in datas['data']:
    time.sleep(random.randint(1,2))
    # print(data[1])
    time_stamp02 = int(time.time() * 1000)
    detail_url = f"https://product.weather.com.cn/alarm/webdata/{data[1]}?_={time_stamp02}"
    detail_response = requests.get(detail_url,headers=headers)
    detail_text = detail_response.content.decode('utf-8')[14:]
    print(detail_text)