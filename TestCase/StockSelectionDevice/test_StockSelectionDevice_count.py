import json

import allure
import pytest
import requests

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import MongoDB, showsql
from Common.sign import get_sign
from Common.tools.read_write_yaml import yamltoken

from Common.tools.unique_text import get_unique_username
from glo import JSON, HTTP


# @pytest.mark.skip(reason="状态显示未完成，目前无法运行")
@allure.feature('选股器')
class TestStockSelectionDeviceCount:
    @classmethod
    def setup_class(cls) -> None:
        login()
        # 通过传入数据库的IP地址address，用户名user，密码password，数据库名database连接到后台数据库
        userId = showsql(
            '192.168.1.237', 'root', '123456', "user_account",
            "select user_id from t_user_account where `zr_no`= '68904140';"
        )
        # 通过查询语句找到用户id
        # 传入键key，值price，数据库名database，表名surface到MongoDB数据库
        id = MongoDB("192.168.1.236", 27017, "stock_selector", "t_tactic6", "user_id", str(userId)[3:-5:])
        # print(str(userId)[3:-5:])
        cls._id = int(len(id))

    @allure.story('用户所有策略条数查询')
    def test_StockSelectionDevice_count(self):
        response = zhuorui('Allstock', '用户所有策略条数查询')
        assert_data(response, '000000', 'ok')
        if "data" in response.json():
            # print(type(j.get("data")))
            assert int(response.json().get("data")) == self._id
