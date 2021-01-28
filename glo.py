import os
from typing import Union

FALG = True  # 社区，如果为True则不执行time.sleep(),反之则执行
headPhoto = 'http://zhuorui-public.oss-cn-shenzhen.aliyuncs.com/head_photo/images/2021/01/11/16103477341540274.jpeg'  # 用户头像发生变化，请在这里修改头像地址
BASE_DIR: Union[bytes, str] = os.path.dirname(os.path.abspath(__file__))
HTTP = "http://192.168.1.241"
console_HTTP = "http://192.168.1.239:8080/apisC"  # http://192.168.1.241:1216/
loginAccount = "test@123.com"
password = "abcd1234567"
console_JSON = {
    "Content-Type": "application/json;charset=UTF-8",
    "Connection": "keep-alive",
    "traceId": "862c0ed0-5aef-11eb-8806-81a3e151bf57",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/86.0.4240.183 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache"
}
# 测试环境192.168.1.241（iOS）('18379204795', '102522ql', '86')
phone = "18379204795"
pwd = "102522ql"
zrNo = '68904140'  # 卓锐号
nickname = 'ZrAutotest账号'  # 卓锐用户昵称
# phone = "13525219777"
# pwd = "a12345"
# JSON = {
#     "Content-Type": "application/json",
#     "appVersion": '0.1.5',
#     "deviceId": "5502AB11-CCDB-4B78-B139-71618170DE9C",
#     "osType": "ios",
#     "osVersion": '13.4.1'
# }
# print(BASE_DIR)
# 内网预发布环境192.168.1.121（Android）('15989434843', '123456QAZ', '86')
# phone="15989434843"
# pwd="123456QAZ"
JSON = {
    "Content-Type": "application/json",
    "appVersion": '0.1.3',
    "deviceId": "d41b071ca83ece28",
    "osType": "android",
    "osVersion": '7.1.2',
    "lang": "zh_CN"
}
