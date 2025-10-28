import re

import requests


url = "https://pic.netbian.com/new/"
headers = {
    "cookie": "RcGFvecookieclassrecord=%2C66%2C; PHPSESSID=f05i03q8e4pk0lgph5f5457hq7; RcGFvmlusername=qq726297176161; RcGFvmluserid=8135132; RcGFvmlgroupid=1; RcGFvmlrnd=eoaqz9WbS4ykXv1DZNUz; RcGFvmlinfo=%5B%22http%3A%5C%2F%5C%2Fthirdqq.qlogo.cn%5C%2Fek_qqthird%5C%2FAQUtpgcGrGo07tBopQpCqHtkFQmBFQqLBnsZrJIG4ic8OQg3TokOFCNQc3y1pXkbYmQHwiaueTnyg28E3Wr7CqaYobxpk2B9JaiccEaJFGK%5C%2F100%22%2C%220%22%2C%22qq726297176161%22%2C%22%5Cu666e%5Cu901a%5Cu4f1a%5Cu5458%22%5D; RcGFvmlauth=653f5b4f4486f8e71f5d711c9cb7a29e",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
}
response = requests.get(url,headers=headers)
print(response.status_code)
# print(response.text)
# print(response.content.decode('gbk'))
text = response.content.decode('gbk')
src_list = re.findall(r'<img\s+src="([^"]+)"', text, flags=re.I)
print(src_list)
for item in src_list:
    print(f"https://pic.netbian.com{item}")


"""
拿取cookies，不会拿，拿不到
"""
# session = requests.Session()
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
# }
# response = session.get("https://pic.netbian.com/4kdongman/",headers=headers)
# print(response.status_code)
# print(response.url)
# print(session.cookies)

"""
有拦截
"""
# url = 'https://pic.netbian.com/tupian/40179.html'
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
# }
# response = requests.get(url,headers=headers)
# print(response.status_code)
# # print(response.content.decode('gbk'))
# text = response.content.decode('gbk')
# div_match = re.search(r'<div class="photo-pic">.*?</div>', text, flags=re.I | re.S)
# # print(div_match.group(0))
# src_list = re.findall(r'<img\s+src="([^"]+)"',div_match.group(0), flags=re.I)
# # print(src_list[0])
# path_img = src_list[0]
# # print(f"https://pic.netbian.com{path_img}")
#
# url_img = f"https://pic.netbian.com/uploads/allimg/251027/201942-17615675826e8e.jpg"
# img_headers = {
#     "cookie":"PHPSESSID=f05i03q8e4pk0lgph5f5457hq7; RcGFvmlinfo=%5B%22http%3A%5C%2F%5C%2Fthirdqq.qlogo.cn%5C%2Fek_qqthird%5C%2FAQUtpgcGrGo07tBopQpCqHtkFQmBFQqLBnsZrJIG4ic8OQg3TokOFCNQc3y1pXkbYmQHwiaueTnyg28E3Wr7CqaYobxpk2B9JaiccEaJFGK%5C%2F100%22%2C%220%22%2C%22qq726297176161%22%2C%22%5Cu666e%5Cu901a%5Cu4f1a%5Cu5458%22%5D; RcGFvecookieclassrecord=%2C66%2C60%2C",
#     "referer":"https://pic.netbian.com/tupian/40179.html",
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
# }
#
# response = requests.get(url_img, headers=img_headers)
# img_response = requests.get(url_img, headers=img_headers)
# print(img_response.status_code)
# print(img_response.content)


