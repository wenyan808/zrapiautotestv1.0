import json

import allure
import pytest
import requests
from Common.login import login
from Common.show_sql import OperationSql, MongoDB
from Common.sign import get_sign
from Common.tools.read_yaml import yamltoken

from Common.tools.unique_text import get_unique_username
from glo import JSON, HTTP


# @pytest.mark.skip(reason="状态显示未完成，目前无法运行")
@allure.feature('选股器')
class TestStockSelectionDeviceList:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('用户所有策略列表查询')
    def test_StockSelectionDevice_list(self):
        # 通过传入数据库的IP地址address，用户名user，密码password，数据库名database连接到后台数据库
        # q = OperationSql("192.168.1.237", "root", "123456", "user_account")
        # 通过查询语句找到用户id
        # userId = q.show_sql("select user_id from t_user_account where `zr_no`= '68904140';")
        # 传入键key，值price，数据库名database，表名surface到MongoDB数据库
        # id = MongoDB("user_id", str(userId)[3:-5:], "stock_selector", "t_tactic6")
        # print(str(userId)[3:-5:])
        # _id = str(id[-1].get('_id'))
        # print(_id)
        url = HTTP + "/as_market/api/stock_selector/v1/tactic/list"
        headers = JSON

        # 拼装参数
        # name = get_unique_username(1)[0]
        # print(name)
        paylo = {}
        # paylo.update(_id)
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = headers
        # print(token)
        # print(type(token))

        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)
        # print(headers)
        payload = json.dumps(dict(payload1))
        # print(payload)

        r = requests.post(url=url, headers=headers, data=payload)
        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in r.json():
            if len(j.get("data")) != 0:
                for info in j.get("data"):
                    pass