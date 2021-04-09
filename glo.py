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
phone = "18379204795"  # 手机号
pwd = "102522ql"  # 密码
zrNo = '68904140'  # 卓锐号
nickname = 'ZrAutotest账号'  # 卓锐用户昵称

JSON1 = {
    "Content-Type": "application/json",
    "appVersion": '0.1.5',
    "deviceId": "5502AB11-CCDB-4B78-B139-71618170DE9C",
    "osType": "ios",
    "osVersion": '13.4.1'
}

JSON = {
    "Content-Type": "application/json",
    "appVersion": '0.1.3',
    "deviceId": "d41b071ca83ece28",
    "osType": "android",
    "osVersion": '7.1.2',
    "lang": "zh_CN"
}

# 测试环境开户登录账号
loginAccount_phone = "15816262899"
Accountlogin_password = "zr1234567"

# 内网预发布环境192.168.1.121（Android）('15989434843', '123456QAZ', '86')
# phone="15989434843"
# pwd="123456QAZ"


# 内网开发环境（dev）192.168.1.181（Android）
http_dev = "http://192.168.1.181"
phone_dev = "13418923886"  # 手机号
pwd_dev = "zr123456"  # 密码
clientId_dev = "281866727"
passwordss = "271059"  # 卓锐交易密码
zrNo_dev = '81866727'  # 卓锐号
nickname_dev = '开车老司机'  # 卓锐用户昵称
userId = "fa2022cf17064889a6cc7e4dce8c988b"

JSON_dev = {
    "Content-Type": "application/json",
    "appVersion": '1.0',
    "deviceId": "29DA6F9A-DD0F-4C03-A3FE-3C0563B7092E",
    "osType": "ios",
    "osVersion": '14.4',
    "lang": "zh_CN"
}
consoledev_HTTP = "http://192.168.1.229:8080/apisC"
loginAccountdev = "all"
passworddev = "abcd12345"
consoledev_JSON = {
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


JSON2 = {
    "Content-Type": "application/json",
    "appVersion": '0.2.5',
    "deviceId": "58CAB9A3-172A-43CB-9750-AAA6E45F2043",
    "osType": "ios",
    "osVersion": '14.4',
    "lang": "zh_CN"
}