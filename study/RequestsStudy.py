import re
from os import write

import requests

# print(dir(requests))
# ['ConnectTimeout', 'ConnectionError', 'DependencyWarning', 'FileModeWarning', 'HTTPError', 'JSONDecodeError', 'NullHandler', 'PreparedRequest', 'ReadTimeout', 'Request', 'RequestException', 'RequestsDependencyWarning', 'Response', 'Session', 'Timeout', 'TooManyRedirects', 'URLRequired',
# '__author__', '__author_email__', '__build__', '__builtins__', '__cached__', '__cake__', '__copyright__', '__description__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__title__', '__url__', '__version__', '_check_cryptography', '_internal_utils',
# 'adapters', 'api', 'auth', 'certs', 'chardet_version', 'charset_normalizer_version', 'check_compatibility', 'codes', 'compat', 'cookies', 'delete', 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 'request', 'session', 'sessions', 'ssl', 'status_codes', 'structures', 'urllib3', 'utils', 'warnings']


print(requests.__cake__)

"""
基础
"""
# url = "http://httpbin.org/get?name=gg"

# response = requests.get(url)
# print(response)
# print(dir(response))
# print(response.text)
# print(response.status_code)
# print(response.url)
# print(response.headers)
# print("------------------------------01")
# response = requests.get(url,params={"age":17,"length":"18cm"})
# print(response.content)
# print(response.text)
# print(response.json())
# print("------------------------------02")
# response = requests.get(url,params={"age":17,"length":"18cm"})
# print(response.request.headers)
# print(response.request.method)
# print(response.request.url)
# print(dir(response.request))
# print("------------------------------03")
# url = "http://httpbin.org/post?name=gg"
# response = requests.post(url,params={"age":17,"length":"18cm"},json={"ggggg":"11111"},headers={"Content-Type":"application/json"})
# print(response.json())
# print(response.json()["data"])
# print("------------------------------04")

# url = "https://contentcms-bj.cdn.bcebos.com/cmspic/bc7bfcbbdc9f43646903046238a87d2a.jpeg?x-bce-process=image/crop,x_0,y_0,w_636,h_346"
# response = requests.get(url)
# with open(f"../static/test01.jpg","wb") as f:
#     f.write(response.content)
#
# print("------------------------------05")


# --------------------------------------------------
#
"""
进阶
"""
"""
requests.get() 请求参数
"""
# 创建django项目模拟目标网站

url = "http://127.0.0.1:8000/admin/"

# response = requests.get(url)
# print(response.status_code)
#
# response = requests.get(url,allow_redirects=False) #禁止重定向
# print(response.status_code)
# print("--------------------------------------------01")
# headers = {
#     "cookie":"sessionid=zkhjjsg2afldjyg9eho6w2yrvln166mm"
# }
# # cookies
# response = requests.get(url,allow_redirects=False,headers=headers)
# print(response.status_code)
# print(response.text)
# print("--------------------------------------------02")
# cookies = {
#     "sessionid":"zkhjjsg2afldjyg9eho6w2yrvln166mm"
# }
# response = requests.get(url,allow_redirects=False,cookies=cookies)
# print(response.status_code)
# print(response.text)


"""
request 模拟登录
"""
url2 = "http://127.0.0.1:8000/admin/login/?next=/admin/"

response = requests.get(url2)
# 先通过get请求，获取cookie和csrfmiddlewaretoken
# print(response.cookies)
# print(response.text)
csrfmiddlewaretoken = re.search(r'<input type="hidden" name="csrfmiddlewaretoken" value="(.*?)">',response.text).group(1)
# print(csrfmiddlewaretoken)

response = requests.post(url2, data={'csrfmiddlewaretoken': csrfmiddlewaretoken,'username':"admin",'password':123456}, cookies=response.cookies)
# 在通过post传递数据
print(response.text)

print("--------------------------------------------01")
session = requests.Session() #创建实例
response = session.get(url2)
csrfmiddlewaretoken = re.search(r'<input type="hidden" name="csrfmiddlewaretoken" value="(.*?)">',response.text).group(1)
# 通过get获取csrfmiddlewaretoken
response = session.post(url2,data={'csrfmiddlewaretoken': csrfmiddlewaretoken,'username':"admin",'password':123456})
print(response.text)
print("--------------------------------------------02")


