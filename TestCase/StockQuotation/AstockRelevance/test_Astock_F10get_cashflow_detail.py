import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockF10getCashflowDetail:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('A股F10获取现金流量报表详情数据')
    def test_Astock_F10get_cashflow_detail(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据')
        # print(response)
        assert_data(response, '000000', 'ok')
