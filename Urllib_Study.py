import json
import urllib
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import Request
from urllib.parse import urlencode


print(dir(urllib))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__',
# 'error', 'parse', 'request', 'response']

# print(dir(urllib.error))
# ['ContentTooShortError', 'HTTPError', 'URLError',
# '__all__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__',
# '__spec__', 'io', 'urllib']

# print(dir(urllib.request))
# ['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler',
# 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler',
# 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor',
# 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError',
# 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr',
# 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth',
# 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector',
# 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler',
# 'Request', 'URLError', 'URLopener', 'UnknownHandler',
# '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_proxy_bypass_winreg_override', '_randombytes', '_safe_gethostbyname', '_splitattr', '_splithost', '_splitpasswd', '_splitport', '_splitquery', '_splittag', '_splittype', '_splituser', '_splitvalue', '_thishost', '_to_bytes', '_url_tempfiles',
# 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_registry', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_registry', 'quote', 're', 'request_host', 'socket', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']

# print(dir(urllib.parse))
# ['DefragResult', 'DefragResultBytes', 'ParseResult', 'ParseResultBytes', 'ResultBase', 'SplitResult', 'SplitResultBytes',
# '_ALWAYS_SAFE', '_ALWAYS_SAFE_BYTES', '_DefragResultBase', '_NetlocResultMixinBase', '_NetlocResultMixinBytes', '_NetlocResultMixinStr', '_ParseResultBase', '_Quoter', '_ResultMixinBytes', '_ResultMixinStr', '_SplitResultBase', '_UNSAFE_URL_BYTES_TO_REMOVE', '_WHATWG_C0_CONTROL_OR_SPACE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__getattr__', '__loader__', '__name__', '__package__', '__spec__', '_asciire', '_byte_quoter_factory', '_check_bracketed_host', '_checknetloc', '_coerce_args', '_decode_args', '_encode_result', '_generate_unquoted_parts', '_hexdig', '_hextobyte', '_hostprog', '_implicit_encoding', '_implicit_errors', '_noop', '_portprog', '_splitattr', '_splithost', '_splitnetloc', '_splitnport', '_splitparams', '_splitpasswd', '_splitport', '_splitquery', '_splittag', '_splittype', '_splituser', '_splitvalue', '_to_bytes', '_typeprog', '_unquote_impl',
# 'clear_cache', 'functools', 'ipaddress', 'math', 'namedtuple', 'non_hierarchical', 'parse_qs', 'parse_qsl', 'quote', 'quote_from_bytes', 'quote_plus', 're', 'scheme_chars', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'to_bytes', 'types', 'unquote', 'unquote_plus', 'unquote_to_bytes', 'unwrap', 'urldefrag', 'urlencode', 'urljoin', 'urlparse', 'urlsplit', 'urlunparse', 'urlunsplit', 'uses_fragment', 'uses_netloc', 'uses_params', 'uses_query', 'uses_relative', 'warnings']

url = "http://httpbin.org/get?name=gg"

req_url = urllib.request.Request(url)
print(dir(req_url))
print(req_url.headers)
print(req_url.full_url)
print(req_url.host)
print(req_url.selector)
response = urllib.request.urlopen(req_url)
response_bytes = response.read()
response_str = response_bytes.decode('utf-8')
print(response_str)
print("-------------------------------------------01")
req_url = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'},method='GET')
print(req_url.headers)
print(req_url.host)
print(req_url.selector)
response = urllib.request.urlopen(req_url)
response_bytes = response.read()
response_str = response_bytes.decode('utf-8')
print(response_str)
print("-------------------------------------------02")
date_text = {"name":"gg"}
url_encoded = urllib.parse.urlencode(date_text)
req_url = urllib.request.Request(url,data=url_encoded.encode(), headers={'User-Agent': 'Mozilla/5.0'},method='GET')
print(req_url.headers)
print(req_url.data)
response = urllib.request.urlopen(req_url)
response_bytes = response.read()
response_str = response_bytes.decode('utf-8')
print(response_str)
print("--------------------------------------03")
url = "http://httpbin.org/post?name=gg"
date_text = {"name":"gg"}
url_encoded = json.dumps(date_text)
req_url = urllib.request.Request(url,data=url_encoded.encode(), headers={'User-Agent': 'Mozilla/5.0',"content-type":"application/json",},method='POST')
response = urllib.request.urlopen(req_url)
# print(response.read())
response_bytes = response.read()
response_str = response_bytes.decode('utf-8')
print(response_str)
print("--------------------------------------04--post--Json格式")
date_text = {"name":"gg"}
url_encoded = urllib.parse.urlencode(date_text)
req_url = urllib.request.Request(url,data=url_encoded.encode(), headers={'User-Agent': 'Mozilla/5.0',"content-type":"application/x-www-form-urlencoded",},method='POST')
response = urllib.request.urlopen(req_url)
# print(response.read())
response_bytes = response.read()
response_str = response_bytes.decode('utf-8')
print(response_str)
print("--------------------------------------05--post--parse格式")



