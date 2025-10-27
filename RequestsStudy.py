from os import write

import requests

# print(dir(requests))
# ['ConnectTimeout', 'ConnectionError', 'DependencyWarning', 'FileModeWarning', 'HTTPError', 'JSONDecodeError', 'NullHandler', 'PreparedRequest', 'ReadTimeout', 'Request', 'RequestException', 'RequestsDependencyWarning', 'Response', 'Session', 'Timeout', 'TooManyRedirects', 'URLRequired',
# '__author__', '__author_email__', '__build__', '__builtins__', '__cached__', '__cake__', '__copyright__', '__description__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__title__', '__url__', '__version__', '_check_cryptography', '_internal_utils',
# 'adapters', 'api', 'auth', 'certs', 'chardet_version', 'charset_normalizer_version', 'check_compatibility', 'codes', 'compat', 'cookies', 'delete', 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 'request', 'session', 'sessions', 'ssl', 'status_codes', 'structures', 'urllib3', 'utils', 'warnings']


print(requests.__cake__)


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
url = "https://contentcms-bj.cdn.bcebos.com/cmspic/bc7bfcbbdc9f43646903046238a87d2a.jpeg?x-bce-process=image/crop,x_0,y_0,w_636,h_346"
response = requests.get(url)
with open(f"static/test01.jpg","wb") as f:
    f.write(response.content)

print("------------------------------03")

