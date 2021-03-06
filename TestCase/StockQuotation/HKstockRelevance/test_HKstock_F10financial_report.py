import allure
# import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason="")
@allure.feature('港股')
class TestHKstockF10financialreport:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('港股获取F10财报信息')
    def test_HKstock_F10financial_report(self):
        response = zhuorui('港股', '港股获取F10财报信息')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股获取F10财报信息_无token')
    def test_HKstock_F10financial_report_notoken(self):
        response = zhuorui('港股', '港股获取F10财报信息_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股获取F10财报信息_ts为空')
    def test_HKstock_F10financial_report_tsNone(self):
        response = zhuorui('港股', '港股获取F10财报信息_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股获取F10财报信息_code为空')
    def test_HKstock_F10financial_report_codeNone(self):
        response = zhuorui('港股', '港股获取F10财报信息_code为空')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股获取F10财报信息_ts为中文')
    def test_HKstock_F10financial_report_tsofchinese(self):
        response = zhuorui('港股', '港股获取F10财报信息_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股获取F10财报信息_code为中文')
    def test_HKstock_F10financial_report_codeofchinese(self):
        response = zhuorui('港股', '港股获取F10财报信息_code为中文')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股获取F10财报信息_ts不正确')
    def test_HKstock_F10financial_report_tsError(self):
        response = zhuorui('港股', '港股获取F10财报信息_ts不正确')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股获取F10财报信息_code不正确')
    def test_HKstock_F10financial_report_codeError(self):
        response = zhuorui('港股', '港股获取F10财报信息_code不正确')
        # assert_data(response, '000103', 'code格式有误')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股获取F10财报信息_只传ts')
    def test_HKstock_F10financial_report_onlyvalts(self):
        response = zhuorui('港股', '港股获取F10财报信息_只传ts')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股获取F10财报信息_只传code')
    def test_HKstock_F10financial_report_onlyvalcode(self):
        response = zhuorui('港股', '港股获取F10财报信息_只传code')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股获取F10财报信息_参数为空')
    def test_HKstock_F10financial_report_bobyNone(self):
        response = zhuorui('港股', '港股获取F10财报信息_参数为空')
        # assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    # @allure.story('港股获取F10财报信息')
    # def test_HKstock_F10financial_report(self):
    #     response = zhuorui('港股', '港股获取F10财报信息')
    #     assert_data(response, '000000', 'ok')
    #     assert response.status_code == 200
    #     # print(response.json())
    #
    # @allure.story('港股获取F10财报信息')
    # def test_HKstock_F10financial_report(self):
    #     response = zhuorui('港股', '港股获取F10财报信息')
    #     assert_data(response, '000000', 'ok')
    #     assert response.status_code == 200
    #     # print(response.json())
    #
    # @allure.story('港股获取F10财报信息')
    # def test_HKstock_F10financial_report(self):
    #     response = zhuorui('港股', '港股获取F10财报信息')
    #     assert_data(response, '000000', 'ok')
    #     assert response.status_code == 200
    #     # print(response.json())
