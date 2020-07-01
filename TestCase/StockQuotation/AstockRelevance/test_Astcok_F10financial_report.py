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
        # print(response.text)

    @allure.story('A股获取F10财报信息_token为0')
    def test_Astock_F10financial_report_notoken(self):
        response = zhuorui('A股', 'A股获取F10财报信息_token为0')
        # assert_data(response, '000101', 'token不能为空')
        # if response ==None:
        print(response)
            # raise NameError("没有token")


    @allure.story('A股获取F10财报信息_id为None')
    def test_Astock_F10financial_report_idNone(self):
        response = zhuorui('A股', 'A股获取F10财报信息_id为None')
        # assert_data(response, '000000', 'ok')
        # if response == None:
        print(response)
            # raise NameError("id为None")
