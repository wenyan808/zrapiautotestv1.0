import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestNewdayKlineHKtape:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('最新日K_HK大盘_HSI')
    def test_newdayKline_HKtape_HSI(self):
        response = zhuorui('k线', '最新日K_HK大盘_HSI')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_HK大盘_HSCEI')
    def test_newdayKline_HKtape_HSCEI(self):
        response = zhuorui('k线', '最新日K_HK大盘_HSCEI')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_HK大盘_HSCCI')
    def test_newdayKline_HKtape_HSCCI(self):
        response = zhuorui('k线', '最新日K_HK大盘_HSCCI')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_HK大盘_CES100')
    def test_newdayKline_HKtape_CES100(self):
        response = zhuorui('k线', '最新日K_HK大盘_CES100')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_HK大盘_CES300')
    def test_newdayKline_HKtape_CES300(self):
        response = zhuorui('k线', '最新日K_HK大盘_CES300')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_HK大盘_token为0')
    def test_newdayKline_HKtape_notoken(self):
        response = zhuorui('k线', '最新日K_HK大盘_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    # @allure.story('最新日K_HK大盘_type类型为2股票')
    # def test_newdayKline_HKtape_typeof2(self):
    #     response = zhuorui('k线', '最新日K_HK大盘_type类型为2股票')
    #     # assert_data(response, '000000', 'ok')
    #     print(response.json())

    @allure.story('最新日K_HK大盘_type不正确')
    def test_newdayKline_HKtape_typeError(self):
        response = zhuorui('k线', '最新日K_HK大盘_type不正确')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.json())

    @allure.story('最新日K_HK大盘_type为空')
    def test_newdayKline_HKtape_typeNone(self):
        response = zhuorui('k线', '最新日K_HK大盘_type为空')
        assert_data(response, '000103', 'type is not null')
        # print(response.json())

    @allure.story('最新日K_HK大盘_adjType为空')
    def test_newdayKline_HKtape_adjTypeNone(self):
        response = zhuorui('k线', '最新日K_HK大盘_adjType为空')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.text)

    @allure.story('最新日K_HK大盘_adjType类型为2前复权')
    def test_newdayKline_HKtape_adjTypeof2(self):
        response = zhuorui('k线', '最新日K_HK大盘_adjType类型为2前复权')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_HK大盘_adjType类型为3后复权')
    def test_newdayKline_HKtape_adjTypeof3(self):
        response = zhuorui('k线', '最新日K_HK大盘_adjType类型为3后复权')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_HK大盘_ts为空')
    def test_newdayKline_HKtape_tsNone(self):
        response = zhuorui('k线', '最新日K_HK大盘_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('最新日K_HK大盘_ts为其他string')
    def test_newdayKline_HKtape_tsotherstring(self):
        response = zhuorui('k线', '最新日K_HK大盘_ts为其他string')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('最新日K_HK大盘_code为空')
    def test_newdayKline_HKtape_codeNone(self):
        response = zhuorui('k线', '最新日K_HK大盘_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    # @allure.story('最新日K_HK大盘_code异常')
    # def test_newdayKline_HKtape_codeException(self):
    #     response = zhuorui('k线', '最新日K_HK大盘_code异常')
    #     # assert_data(response, '000103', 'code格式有误')
    #     print(response.json())

    # @allure.story('最新日K_HK大盘_code不正确')
    # def test_newdayKline_HKtape_codeError(self):
    #     response = zhuorui('k线', '最新日K_HK大盘_code不正确')
    #     # assert_data(response, '000103', 'code格式有误')
    #     print(response.json())

    @allure.story('最新日K_HK大盘_只传ts')
    def test_newdayKline_HKtape_onlyvalts(self):
        response = zhuorui('k线', '最新日K_HK大盘_只传ts')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('最新日K_HK大盘_只传code')
    def test_newdayKline_HKtape_onlyvalcode(self):
        response = zhuorui('k线', '最新日K_HK大盘_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('最新日K_HK大盘_只传type')
    def test_newdayKline_HKtape_onlyvaltype(self):
        response = zhuorui('k线', '最新日K_HK大盘_只传type')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    # @allure.story('最新日K_HK大盘只传adjType')
    # def test_newdayKline_HKtapeonlyvaladjType(self):
    #     response = zhuorui('k线', '最新日K_HK大盘只传adjType')
    #     # assert_data(response, '000103', 'ts格式有误')
    #     print(response)






    # @allure.story('最新日K_HK大盘')
    # def test_newdayKline_HKtape(self):
    #     response = zhuorui('k线', '最新日K_HK大盘')
    #     assert_data(response, '000000', 'ok')
    #     # print(response.json())
