
"""

    题四：JS逆向入门
    https://www.mashangpa.com/problem-detail/4/
"""


# https://www.mashangpa.com/api/problem-detail/4/data/?page=1&sign=2fa61136abdd19095e3689b7fb05252f&_ts=1761827081634

# import time
# import hashlib
# from curl_cffi import requests
# sum = 0
# page = 1
# while True:
#     time_stamp = int(time.time()*1000)
#     if page > 20:
#         break
#     sign_str = "tuling"+str(time_stamp)+str(page)
#     sign = hashlib.md5(sign_str.encode()).hexdigest()
#     url = f"https://www.mashangpa.com/api/problem-detail/4/data/?page={page}&sign={sign}&_ts={time_stamp}"
#     page+=1
#     headers = {
#         "referer":"https://www.mashangpa.com/problem-detail/4/",
#         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
#         "cookie":"sessionid=xgklknpr6fw3ixkxfsxxr8pyeltxnkfb"
#     }
#
#     response = requests.get(url,headers=headers)
#     print()
#     datas = response.json()
#     current_array = datas["current_array"]
#     for num in current_array:
#         sum += int(num)
#         print(sum)
#


"""

    题五：屠龙刀
    https://www.mashangpa.com/problem-detail/5/
"""
# https://www.mashangpa.com/api/problem-detail/5/data/

# pip install pycryptodome
import time
import hashlib
from curl_cffi import requests

import json
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

import json
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


# def aes_cbc_encrypt(json_str, key_bytes, iv_bytes):
#     """
#     AES-CBC加密（与前端CryptoJS逻辑完全对齐）
#     :param json_str: 待加密的JSON字符串（无空格）
#     :param key_bytes: 密钥字节数组（16字节）
#     :param iv_bytes: IV字节数组（16字节）
#     :return: 十六进制密文
#     """
#     # 1. 明文转为UTF-8字节（与CryptoJS.enc.Utf8.parse一致）
#     plaintext = json_str.encode('utf-8')
#
#     # 2. 初始化AES-CBC加密器
#     cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
#
#     # 3. Pkcs7填充（AES块大小16字节）
#     padded_plaintext = pad(plaintext, AES.block_size)
#
#     # 4. 加密并转为十六进制字符串
#     ciphertext = cipher.encrypt(padded_plaintext)
#     return binascii.b2a_hex(ciphertext).decode('utf-8')
#
#
# sum = 0
# page = 1
# while True:
#     time_stamp = int(time.time() * 1000)
#     if page > 20:
#         break
#
#
#     # 1. 密钥字节（从key.words转换而来）
#     key_hex = "6A6F386A39774777253648627866466E"
#     key_bytes = binascii.a2b_hex(key_hex)  # 转为16字节bytes
#     time_stamp = int(time.time() * 1000)
#     # 2. IV字节（从iv.words转换而来）
#     iv_hex = "30313233343536373839414243444546"
#     iv_bytes = binascii.a2b_hex(iv_hex)  # 转为16字节bytes
#
#     # 3. 待加密的JSON（必须与前端JSON.stringify结果完全一致，无空格）
#     params = {
#         "page": page,
#         "_ts": time_stamp  # 替换为你测试的实际_ts
#     }
#     json_str = json.dumps(params, separators=(',', ':'))  # 禁用空格
#
#     # 4. 加密
#     encrypted = aes_cbc_encrypt(json_str, key_bytes, iv_bytes)
#     # print("加密结果：", encrypted)
#
#
#     url = f"https://www.mashangpa.com/api/problem-detail/5/data/"
#     page+=1
#
#     headers = {
#         "referer":"https://www.mashangpa.com/problem-detail/5/",
#         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
#         "cookie":"sessionid=xgklknpr6fw3ixkxfsxxr8pyeltxnkfb"
#     }
#     json_data = {
#         "xl":encrypted
#     }
#
#     response = requests.post(url,headers=headers,json=json_data)
#     datas = response.json()
#     current_array = datas["current_array"]
#     for num in current_array:
#         print(num)
#         sum += int(num)
#         print(sum)







