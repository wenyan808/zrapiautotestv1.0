import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockProfitDetail:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('A股F10获取利润表详情页数据')
    def test_Astock_profit_detail(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据')
        assert_data(response, '000000', 'ok')
