import os
from typing import Union

FALG = True  # 社区，如果为True则不执行time.sleep(),反之则执行
# headPhoto = "http://zhuorui-public-test.oss-cn-shenzhen.aliyuncs.com/" \
#             "head_photo/images/2021/01/11/16103477341540274.jpeg"
headPhoto = 'http://zhuorui-public-test.oss-cn-shenzhen.aliyuncs.com/' \
            'head_photo/images/2021/01/11/16103477341540274.jpeg'  # 用户头像发生变化，请在这里修改头像地址
BASE_DIR: Union[bytes, str] = os.path.dirname(os.path.abspath(__file__))

# 测试环境地址管理：
HTTP = "http://192.168.1.241"
http = "http://192.168.1.241"

console_HTTP = "http://192.168.1.239:8080/apisC"
# 测试环境账户管理：
loginAccount = "test@123.com"
password = "abcd1234567"
# 测试环境未开户帐号（手机号密码管理）：
phone = "18379204795"  # 手机号
pwd = "102522ql"  # 密码
zrNo = '68904140'  # 卓锐号
nickname = 'ZrAutotest账号'  # 卓锐用户昵称

# 测试环境开户登录账号（修改）
loginAccount_phone = "15989434843"
Accountlogin_password = "zr123456"

# 测试环境已开户账号管理
# 手机号1用于变更（修改）密码   警告不要乱动
phone1 = "15816263998"  # login手机号
pwd1 = "zr123456"  # login密码
clientId1 = "3023121393"
# passwords1 = "123456"  # 卓锐行情交易密码（已变）  密码已经放入json文件中 test_HSCustomerInfo_ChangeTradePwddata.json
zrNo1 = '23121393'  # 卓锐号
nickname1 = '卓锐测试一号'  # 卓锐用户昵称
userId1 = "f3d9c946caf842fdbddd1c748ce7163a"

# 手机号2用于公用的登录认证
phone2 = "15816263996"  # login手机号
pwd2 = "zr123456"  # login密码
clientId2 = "3090959308"
passwords2 = "123456"  # 卓锐行情交易密码
zrNo2 = '90959308'  # 卓锐号
nickname2 = '卓锐测试二号'  # 卓锐用户昵称
userId2 = "e17f8fd374334995ac02df1ad6cc7872"

phone3 = "15816263997"  # login手机号
pwd3 = "zr123456"  # login密码
clientId3 = "3078791478"
passwords3 = "123456"  # 卓锐行情交易密码
zrNo3 = '78791478'  # 卓锐号
nickname3 = '卓锐测试三号'  # 卓锐用户昵称
userId3 = "cf7999ea09f34657a870a2d44e3c026a"

phone4 = "15816263999"  # login手机号
pwd4 = "zr123456"  # login密码
clientId4 = "3052877539"
passwords4 = "123456"  # 卓锐行情交易密码
zrNo4 = '52877539'  # 卓锐号
nickname4 = '卓锐测试四号'  # 卓锐用户昵称
userId4 = "5497496d0450408484e18f39aac10ae9"

phone5 = "15814213200"
pwd5 = "zr123456"
phoneArea = "86"

# header管理：
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

JSON = {
    "Content-Type": "application/json",
    "appVersion": '0.1.3',
    "deviceId": "d41b071ca83ece28",
    "osType": "android",
    "osVersion": '7.1.2',
    "lang": "zh_CN"
}

JSON1 = {
    "Content-Type": "application/json",
    "appVersion": '0.1.5',
    "deviceId": "5502AB11-CCDB-4B78-B139-71618170DE9C",
    "osType": "ios",
    "osVersion": '13.4.1'
}

JSON2 = {
    "Content-Type": "application/json",
    "appVersion": '0.2.5',
    "deviceId": "58CAB9A3-172A-43CB-9750-AAA6E45F2043",
    "osType": "ios",
    "osVersion": '14.4',
    "lang": "zh_CN"
}

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
