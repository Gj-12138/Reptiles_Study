import re

from curl_cffi import requests

# url = "https://pic.netbian.com/new/"
# headers = {
#     "cookie": "RcGFvecookieclassrecord=%2C66%2C; PHPSESSID=f05i03q8e4pk0lgph5f5457hq7; RcGFvmlusername=qq726297176161; RcGFvmluserid=8135132; RcGFvmlgroupid=1; RcGFvmlrnd=eoaqz9WbS4ykXv1DZNUz; RcGFvmlinfo=%5B%22http%3A%5C%2F%5C%2Fthirdqq.qlogo.cn%5C%2Fek_qqthird%5C%2FAQUtpgcGrGo07tBopQpCqHtkFQmBFQqLBnsZrJIG4ic8OQg3TokOFCNQc3y1pXkbYmQHwiaueTnyg28E3Wr7CqaYobxpk2B9JaiccEaJFGK%5C%2F100%22%2C%220%22%2C%22qq726297176161%22%2C%22%5Cu666e%5Cu901a%5Cu4f1a%5Cu5458%22%5D; RcGFvmlauth=653f5b4f4486f8e71f5d711c9cb7a29e",
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
# }
# response = requests.get(url,headers=headers)
# print(response.status_code)
# # print(response.text)
# # print(response.content.decode('gbk'))
# text = response.content.decode('gbk')
# src_list = re.findall(r'<img\s+src="([^"]+)"', text, flags=re.I)
# print(src_list)
# for item in src_list:
#     print(f"https://pic.netbian.com{item}")

"""
详情页
"""
# url = 'https://pic.netbian.com/tupian/40179.html'
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
# }
# response = requests.get(url,headers=headers)
# print(response.status_code)
# text = response.content.decode('gbk')
#
# div_match = re.search(r'<div class="photo-pic">.*?</div>', text, flags=re.I | re.S)
#
# src_list = re.findall(r'<img\s+src="([^"]+)"',div_match.group(0), flags=re.I)
#
# path_img = src_list[0]
# print(f"https://pic.netbian.com{path_img}")
#


# url_img = f"https://pic.netbian.com/uploads/allimg/251027/201942-17615675826e8e.jpg"
# img_headers = {
#     "referer":"https://pic.netbian.com/tupian/40176.html",
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
# }
#
# img_response = requests.get(url_img, headers=img_headers,verify=True,allow_redirects=False)
# print(img_response.content)
# with open("201942img.jpg","wb") as f:
#     f.write(img_response.content)
