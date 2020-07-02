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
        assert_data(response, '000000', 'ok')
        # if response ==None:
        # print(response.text)
            # raise NameError("没有token")


    @allure.story('A股获取F10财报信息_ts为空')
    def test_Astock_F10financial_report_tsNone(self):
        response = zhuorui('A股', 'A股获取F10财报信息_ts为空')
        assert_data(response, '000103', 'ts不能为空')
        # print(response.text)

    @allure.story('A股获取F10财报信息_ts为异常')
    def test_Astock_F10financial_report_tsException(self):
        response = zhuorui('A股', 'A股获取F10财报信息_ts为异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股获取F10财报信息_ts为错误')
    def test_Astock_F10financial_report_tsError(self):
        response = zhuorui('A股', 'A股获取F10财报信息_ts为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股获取F10财报信息_code为空')
    def test_Astock_F10financial_report_codeNone(self):
        response = zhuorui('A股', 'A股获取F10财报信息_code为空')
        assert_data(response, '000103', 'code不能为空')
        # print(response.text)

    @allure.story('A股获取F10财报信息_code为异常')
    def test_Astock_F10financial_report_codeException(self):
        response = zhuorui('A股', 'A股获取F10财报信息_code为异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股获取F10财报信息_code为错误')
    def test_Astock_F10financial_report_codeError(self):
        response = zhuorui('A股', 'A股获取F10财报信息_code为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股获取F10财报信息_只传值ts')
    def test_Astock_F10financial_report_onlyvalts(self):
        response = zhuorui('A股', 'A股获取F10财报信息_只传值ts')
        assert_data(response, '000103', 'code不能为空')
        # print(response.text)

    @allure.story('A股获取F10财报信息_只传值code')
    def test_Astock_F10financial_report_onlyvalcode(self):
        response = zhuorui('A股', 'A股获取F10财报信息_只传值code')
        assert_data(response, '000103', 'ts不能为空')
        # print(response.text)






