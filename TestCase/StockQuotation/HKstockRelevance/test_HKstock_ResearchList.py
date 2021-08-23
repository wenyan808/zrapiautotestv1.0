import time

import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@pytest.mark.skip(reason="该接口已被删除，接口地址错误")
@allure.feature('港股')
class TestHKstockResearchList:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('资讯研报')
    def test_HKstock_ResearchList(self):
        # time.sleep(3)
        response = zhuorui('港股', '资讯研报')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('资讯研报_无token')
    def test_HKstock_ResearchList_notoken(self):
        # time.sleep(3)
        response = zhuorui('港股', '资讯研报_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())