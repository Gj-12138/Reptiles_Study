# https://www.bilibili.com/anime/index/?from_spmid=666.4.index.0#st=1&order=3&season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&sort=0&page=1
from curl_cffi import requests

# 番剧
# url = "https://api.bilibili.com/pgc/season/index/result?st=1&order=3&season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&sort=0&page=2&season_type=1&pagesize=20&type=1"
#
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
# }
# page=1
# while True:
#     url = f"https://api.bilibili.com/pgc/season/index/result?st=1&order=3&season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&sort=0&page={page}&season_type=1&pagesize=20&type=1"
#     response = requests.get(url,headers=headers)
#     datas = response.json()
#
#     data = datas["data"]
#
#     has_next = data["has_next"]
#     items = data["list"]
#
#     for item in items:
#         print(item)
#
#     if has_next:
#         page+=1
#     else:
#         break


# 首页--换一换

# https://api.bilibili.com/x/web-interface/wbi/index/top/feed/rcmd?web_location=1430650&y_num=5&fresh_type=3&feed_version=V8&fresh_idx_1h=2&fetch_row=1&fresh_idx=2&brush=0&device=win&homepage_ver=1&ps=10&last_y_num=5&screen=1596-1151&seo_info=&tt_exp=&last_showlist=av_115429259349844,av_115343158742178,av_115428756103068,ad_5614_114351843316842,av_115438151342706,av_115422179361494,av_115442798564723,av_115166326819469,av_115427833285800,av_115356848884986%3Bav_115427799799830,ad_5637_114357094582291,av_115353745169556,av_115439191460591,av_n_115280227341761,av_n_115355406109881,av_n_115292592144644,av_n_115445382254669,av_n_115438302269515,av_n_115415334264632,av_n_115441439676430,av_n_115396057303044&uniq_id=136024069720&w_rid=5cdfc182f992f59d22da265755988e0b&wts=1761789946

# url = "https://api.bilibili.com/x/web-interface/wbi/index/top/feed/rcmd?web_location=1430650&y_num=5&fresh_type=3&feed_version=V8&fresh_idx_1h=2&fetch_row=1&fresh_idx=2&brush=0&device=win&homepage_ver=1&ps=10&last_y_num=5&screen=1596-1151&seo_info=&tt_exp=&last_showlist=av_115429259349844,av_115343158742178,av_115428756103068,ad_5614_114351843316842,av_115438151342706,av_115422179361494,av_115442798564723,av_115166326819469,av_115427833285800,av_115356848884986%3Bav_115427799799830,ad_5637_114357094582291,av_115353745169556,av_115439191460591,av_n_115280227341761,av_n_115355406109881,av_n_115292592144644,av_n_115445382254669,av_n_115438302269515,av_n_115415334264632,av_n_115441439676430,av_n_115396057303044&uniq_id=136024069720&w_rid=5cdfc182f992f59d22da265755988e0b&wts=1761789946"
#
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
# }
#
# response = requests.get(url,headers=headers)
# res_json = response.json()
# datas = res_json["data"]
# items = datas["item"]
# for item in items:
#     print(item)


# 首页--下拉刷新
# https://api.bilibili.com/x/web-interface/wbi/index/top/feed/rcmd?web_location=1430650&y_num=3&fresh_type=4&feed_version=V8&fresh_idx_1h=2&fetch_row=7&fresh_idx=2&brush=2&device=win&homepage_ver=1&ps=12&last_y_num=4&screen=553-1151&seo_info=&tt_exp=&last_showlist=av_n_115218420078806,av_n_115411693605590,av_n_115348527385280,ad_n_5614,av_115432547748940,av_115433957101358,av_n_115371478617226,av_n_115422783348102,av_n_115353510217938,av_n_115431171955346%3Bad_5637_115378407607880,av_115197012410461,live_n_25340848,av_115450734188614,av_115440550481122,av_n_115429594960949,av_n_115455717147994,av_n_115434527457873,av_n_115302641769685,av_n_115394245369767,av_n_115307339324917,av_n_115417699982876&uniq_id=1294405494391&w_rid=9a2358077daaee2a50dc5950d7909c4d&wts=1761790594
# url = """
# https://api.bilibili.com/x/web-interface/wbi/index/top/feed/rcmd?web_location=1430650
# &fresh_idx=2
# &ps=30
# """
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
# }
#
# response = requests.get(url,headers=headers)
# res_json = response.json()
# datas = res_json["data"]
# items = datas["item"]
# for item in items:
#     print(item)


"""

    详情页-视频

"""


# url =  "https://www.bilibili.com/video/BV1VVs8zpE2g/?vd_source=2a951d43982440eba0baa5b0e5446e56"
#
# url =  "https://www.bilibili.com/video/BV1VVs8zpE2g/?vd_source=2a951d43982440eba0baa5b0e5446e56"
# response = requests.get(url)
# print(response.text)

"https://api.bilibili.com/x/v2/reply/wbi/main?oid=115416827430059&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=f7c53715141c61f21218777a1cfcce59&wts=1761910052"
"https://api.bilibili.com/x/v2/reply/wbi/main?oid=115416827430059&type=1&mode=3&pagination_str=%7B%22offset%22:%22CAESEDE4MDQxOTU4OTI3NTE3MDciAggB%22%7D&plat=1&web_location=1315875&w_rid=b7f490f397987e227e226b41782c5eaa&wts=1761910973"
"https://api.bilibili.com/x/v2/reply/wbi/main?oid=115416827430059&type=1&mode=3&pagination_str=%7B%22offset%22:%22CAESEDE4MDQxOTgzMTgzNTAzMjEiAggB%22%7D&plat=1&web_location=1315875&w_rid=cdd2fd63f34faefaa572d5edc94f5f86&wts=1761912452"
"https://api.bilibili.com/x/v2/reply/wbi/main?oid=115416827430059&type=1&mode=3&pagination_str=%7B%22offset%22:%22CAESEDE4MDQxOTgzMTgzNTAzMjEiAggB%22%7D&plat=1&web_location=1315875&w_rid=40082009925d5cdf3415cca6250ced53&wts=1761912451"
"https://api.bilibili.com/x/v2/reply/wbi/main?oid=115416827430059&type=1&mode=3&pagination_str=%7B%22offset%22:%22CAESEDE4MDQxOTgzMTgzNTAzMjEiAggB%22%7D&plat=1&web_location=1315875&w_rid=b371674c384fd40009d386c9f497e6ae&wts=1761912449"
"https://api.bilibili.com/x/v2/reply/wbi/main?oid=115416827430059&type=1&mode=3&pagination_str=%7B%22offset%22:%22CAESEDE4MDQxOTgzMTgzNTAzMjEiAggB%22%7D&plat=1&web_location=1315875&w_rid=c3dd74dd2e1079f8a25bb433fbd52cca&wts=1761912448"
"https://api.bilibili.com/x/v2/reply/wbi/main?oid=115416827430059&type=1&mode=3&pagination_str=%7B%22offset%22:%22CAESEDE4MDQxOTgzMTgzNTAzMjEiAggB%22%7D&plat=1&web_location=1315875&w_rid=f5c5c46abfbd830286358c050e1793d3&wts=1761912447"
"https://api.bilibili.com/x/v2/reply/wbi/main?oid=115416827430059&type=1&mode=3&pagination_str=%7B%22offset%22:%22CAESEDE4MDQxOTgzMTgzNTAzMjEiAggB%22%7D&plat=1&web_location=1315875&w_rid=c73028faf4b51a96ea12c41c3b823fe6&wts=1761912446"



# BV1VVs8zpE2g
# vd_source=2a951d43982440eba0baa5b0e5446e56
# oid=115416827430059
# 'vah^hlf^tqkr'
"""

    视频详情页-评论

"""

comment_url = "https://api.bilibili.com/x/v2/reply/wbi/main?oid=115416827430059&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=f7c53715141c61f21218777a1cfcce59&wts=1761910052"
response = requests.get(comment_url)
# print(response.json())
comment_datas = response.json().get("data").get("replies")
for comment_data in comment_datas:
    # print(comment_data)
    rpid = comment_data.get("rpid")
    root_rpid = comment_data.get("root")
    content_message = comment_data.get("content").get("message")
    uname = comment_data.get("member").get("uname")

    print({
        "评论id": rpid,
        "父评论id": root_rpid,
        "评论类容": content_message,
        "评论者名字": uname
    })
