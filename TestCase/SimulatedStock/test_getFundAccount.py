import re

import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

# test_getFundAccount
from Common.show_sql import showsql


@pytest.mark.skip(reason="调试中 ")
class TestgetFundAccount:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询资金账户接口')
    def test_getFundAccount(self):
        response = zhuorui('模拟炒股', '查询资金账户接口')
        assert response.status_code == 200
        assert_data(response, '000103', 'stockMarket is error')
        # print(response.json())

    @allure.story('查询资金账户接口_1-港股')
    def test_getFundAccount_HK(self):
        userId = showsql(
            '192.168.1.237', 'root', '123456', "user_account",
            "select user_id from t_user_account where `zr_no`= '68904140';"
        )
        # print(userId)
        response = zhuorui('模拟炒股', '查询资金账户接口_1-港股')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert response.json().get("data").get("userId") == userId[0][0]
                # print(response.json().get("data").get("userId"))
                # print(userId[0][0])

    @allure.story('查询资金账户接口_2-美股')
    def test_getFundAccount_US(self):
        response = zhuorui('模拟炒股', '查询资金账户接口_2-美股')
        assert response.status_code == 200
        assert_data(response, '060003', '模拟炒股资金账户不存在')
        # print(response.json())

    @allure.story('查询资金账户接口_3-A股')
    def test_getFundAccount_A(self):
        response = zhuorui('模拟炒股', '查询资金账户接口_3-A股')
        assert response.status_code == 200
        assert_data(response, '060003', '模拟炒股资金账户不存在')
        # print(response.json())
