import json

import allure
import pytest
import requests
from Common.login import login
from Common.show_sql import MongoDB, showsql
from Common.sign import get_sign
from Common.tools.read_yaml import yamltoken

from Common.tools.unique_text import get_unique_username
from glo import JSON, HTTP


# @pytest.mark.skip(reason="状态显示未完成，目前无法运行")
@allure.feature('选股器')
class TestStockSelectionDeviceDelete:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('删除策略_1-中国香港')
    def test_StockSelectionDevice_delete01(self):
        # 通过传入数据库的IP地址address，用户名user，密码password，
        userId = showsql(
            '192.168.1.237', 'root', '123456', "user_account",
            "select user_id from t_user_account where `zr_no`= '68904140';"
        )
        # 通过查询语句找到用户id
        # 传入键key，值price，数据库名database，表名surface到MongoDB数据库
        id = MongoDB("192.168.1.236", 27017, "stock_selector", "t_tactic6", "user_id", str(userId)[3:-5:])
        # print(str(userId)[3:-5:])
        _id = str(id[-1].get('_id'))
        # print(_id)
        url = HTTP + "/as_market/api/stock_selector/v1/tactic/delete"
        headers = JSON

        # 拼装参数
        # name = get_unique_username(1)[0]
        # print(name)
        paylo = {
            "region": 1,
            "tacticId": f"{_id}"
        }
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
