import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@allure.feature('A股')
class TestAstockF10Briefing:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('个股相关分红派息公告查询')
    def test_Astock_F10_briefing(self):
        response = zhuorui('A股', '个股相关分红派息公告查询')
        # print(response)
        assert_data(response, '000000', 'ok')



