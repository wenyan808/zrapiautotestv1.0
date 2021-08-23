"""
@File  ：test_recommend_adddel.py
@Author: renfei
@Time  : 2021/7/26
@Desc  : 新增荐股
@last  : 最后一次修改 chenjialuo 2021/7/27
"""

import json
import allure
import requests

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import get_time_stamp13
from Common.login import login
from Common.sign import get_sign
from Common.tools.read_write_yaml import yamltoken
from TestCase.Recommendedstockconsole.recommend_delete import delete1
from glo import console_JSON, http,JSON

@allure.feature('新增和删除荐股')
class TestRecommendAdd():
    def setup(self):
        # 获取console端token
        login()
        self.token = getConsoleLogin_token()
    def teardowm(self):
        pass
    # 1 - HK,2 - US,3 -（SH,SZ)
    def test_addHK(self):
        if get_market_status(1) != 8:
            # 新增
            add(payloadHK,self.token)
            # 删除
            delete1(0,self.token)

    def test_addSH(self):
        if get_market_status(3) != 8:
            # 新增
            add(payloadSH,self.token)
            # 删除
            delete1(0,self.token)

    def test_adSZ(self):
        if get_market_status(3) != 8:
            # 新增
            add(payloadSZ,self.token)
            # 删除
            delete1(0,self.token)

    def test_adUS(self):
        if get_market_status(2) != 8:
            # 新增
            add(payloadUS,self.token)
            # print(payloadUS)
            # 删除
            delete1(0,self.token)

payloadHK = {
    "type": 2,
    "ts": "HK",
    "code": "00175",
    "operationType": 1,
    "recommendedTime": (int(get_time_stamp13())+120000),
    "recommendedPrice": "601.500",
    "referrerReason": "[{\"type\":\"消息面\",\"list\":[{\"title\":\"市场机会\",\"desc"
                      "\":\"/api/con_stock_recommend/v1/add\"}]}]",
    "name": "吉利汽车"
}
payloadSH = {
    "type": 2,
    "ts": "SH",
    "code": "600031",
    "operationType": 1,
    "recommendedTime": (int(get_time_stamp13())+120000),
    "recommendedPrice": "57.40",
    "referrerReason": "[{\"type\":\"消息面\",\"list\":[{\"title\":\"市场机会\",\"desc"
                      "\":\"/api/con_stock_recommend/v1/add\"}]}]",
    "name": "三一重工"
}

payloadSZ = {
    "type": 2,
    "ts": "SZ",
    "code": "300059",
    "operationType": 1,
    "recommendedTime": (int(get_time_stamp13())+120000),
    "recommendedPrice": "32.82",
    "referrerReason": "[{\"type\":\"消息面\",\"list\":[{\"title\":\"市场机会\",\"desc"
                      "\":\"/api/con_stock_recommend/v1/add\"}]}]",
    "name": "东方财富"
}

payloadUS = {
    "type": 2,
    "ts": "US",
    "code": "SNAP",
    "operationType": 1,
    "recommendedTime": str(int(get_time_stamp13())-43200000+120000),
    "recommendedPrice": "77.970",
    "referrerReason": "[{\"type\":\"消息面\",\"list\":[{\"title\":\"市场机会\",\"desc"
                      "\":\"/api/con_stock_recommend/v1/add\"}]}]",
    "name": "Snap, Inc."
}


def get_market_status(market):
    """
港股  美股 A股时间不一样  这里只是做一个展示  对于 美股的添加了盘前交易  盘后交易 盘前价 盘后价 的状态  是在别的地方展示的，接收数据的时候需要注意区分  不要改变等待开盘、交易中、收盘价的状态

对于A股  只有<span class="colour" style="color: rgb(17, 31, 44);">深证市场最后14:57-15:00有盘后竞价，上证市场没有盘后竞价</span><span class="colour" style="color: rgb(17, 31, 44);">美股没有收盘竞价</span>

NOT_OPEN("000000","090000",1,"未开盘"),
//盘前竞价
PRE_BIDDING("090000","092000",2,"盘前竞价"),
//等待开盘
WAITING_OPEN("092000","093000",3,"等待开盘"),
//交易中  上午
TRADING_IN_MORNING("093000","120000",4,"交易中"),
//午间休市
CLOSED_NOON("120000","130000",5,"午间休市"),
//交易中  下午
TRADING_IN_AFTERNOON("130000","160000",6,"交易中"),
//收盘竞价
CLOSE_BIDDING("160000","161000",7,"收盘竞价"),
//已收盘
HAD_CLOSED("161000","240000",8,"已收盘"),
RESET_BEFORE_OPEN("083000","090000",9,"盘前清零");
注意：
沪深科创板没有盘后竞价时间段，增加了盘后交易时间段 状态码为 10，其他的状态码与上面一致
AFTER_DISC("150000","153000",10,"科创板盘后交易");
    """
    header = {}
    header.update(JSON)
    header.update({"token": yamltoken()})
    response = requests.request("POST", http + "/as_market/api/market_trade_status/v1/get_market_status", headers=JSON, data=json.dumps({"sign": get_sign({})})).json()
    # 1 - HK,2 - US,3 -（SH,SZ)
    if market == 1:
        return response.get("data")[0].get("statusCode")
    elif market == 2:
        return response.get("data")[2].get("statusCode")
    elif market == 3:
        return response.get("data")[1].get("statusCode")


def add(payload1,token):
    # 新增荐股
    url = http + ":1216/api/con_stock_recommend/v1/add"
    payload = json.dumps(dict(payload1))

    head = {}
    head.update(console_JSON)
    token1 = {"token": token}
    head.update(token1)
    headers = head

    response = requests.request("POST", url=url, headers=headers, data=payload)

    r = response.json()

    assert response.status_code == 200
    try:
        assert r.get("code") == "000000"
        assert r.get("msg") == "ok"
        assert r.get("data") == False or True

    except:
        raise AssertionError(
            f"\n请求地址：{url}" 
            f"\nbody参数：{payload}"
            f"\n请求头部参数：{headers}"
            f"\n返回数据结果：{r}"
        )

    # schema = r
    # try:
    #     validate(instance=addresultschema, schema=schema, format_checker=draft7_format_checker)
    # except SchemaError as e:
    #     return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
    # except ValidationError as e:
    #     return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
    # else:
    #     return 0, "success!"
