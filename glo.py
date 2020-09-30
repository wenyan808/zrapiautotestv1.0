import os
from typing import Union

BASE_DIR: Union[bytes, str] = os.path.dirname(os.path.abspath(__file__))
HTTP = "http://192.168.1.241"
# JSON = {
#     "Content-Type": "application/json",
#     "appVersion": '0.1.4',
#     "deviceId": "d41b071ca83ece28",
#     "osType": "android",
#     "osVersion": '7.1.2'
# }
# 测试环境192.168.1.241（iOS）('18379204795', '102522ql', '86')
phone = "18379204795"
pwd = "102522ql"
# phone = "13525219777"
# pwd = "a12345"
JSON = {
    "Content-Type": "application/json",
    "appVersion": '0.1.5',
    "deviceId": "5502AB11-CCDB-4B78-B139-71618170DE9C",
    "osType": "ios",
    "osVersion": '13.4.1'
}
# print(BASE_DIR)
# 内网预发布环境192.168.1.121（Android）('15989434843', '123456QAZ', '86')
# phone="15989434843"
# pwd="123456QAZ"
# JSON= {
#     "Content-Type": "application/json",
#     "appVersion": '0.1.3',
#     "deviceId": "d41b071ca83ece28",
#     "osType": "android",
#     "osVersion": '7.1.2',
#     "lang": "zh_CN"
# }
