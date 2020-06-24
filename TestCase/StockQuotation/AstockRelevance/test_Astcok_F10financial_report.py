import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockF10financialreport:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('A股获取F10财报信息')
    def test_Astock_F10financial_report(self):
        response = zhuorui('A股', 'A股获取F10财报信息')
        assert_data(response, '000000', 'ok')
