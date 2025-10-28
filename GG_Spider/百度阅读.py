# content4308796672|20559543-0
import json
import urllib.parse

# https://boxnovel.baidu.com/boxnovel/yuedu/wapcontent?fromaction=wise&data=%7B%22doc_id%22%3A%2201f1ea49bec30c22590102020740be1e640ecc67%22%2C%22cid%22%3A%224308796672%7C20559543%22%2C%22title%22%3A%22%E6%AD%A3%E4%B9%89%E7%9A%84%E4%BD%BF%E5%91%BD%22%2C%22is_yuedu_source%22%3A0%7D&fr=9
enc = ("%7B%22doc_id%22%3A%2201f1ea49bec30c22590102020740be1e640ecc67%22%2C%22cid%22%3A%224308796672%7C20559543%22%2C%22title%22%3A%22%E6%AD%A3%E4%B9%89%E7%9A%84%E4%BD%BF%E5%91%BD%22%2C%22is_yuedu_source%22%3A0%7D")

json_str = urllib.parse.unquote(enc)
payload = json.loads(json_str)
print(json.dumps(payload, ensure_ascii=False, indent=2))
# {
#   "doc_id": "01f1ea49bec30c22590102020740be1e640ecc67",
#   "cid": "4308796672|20559543",
#   "title": "正义的使命",
#   "is_yuedu_source": 0
# }