import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestNewdayKlineUStape:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('最新日K_US大盘_DIA')
    def test_newdayKline_UStape_DIA(self):
        response = zhuorui('k线', '最新日K_US大盘_DIA')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_US大盘_QQQ')
    def test_newdayKline_UStape_QQQ(self):
        response = zhuorui('k线', '最新日K_US大盘_QQQ')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_US大盘_SPY')
    def test_newdayKline_UStape_SPY(self):
        response = zhuorui('k线', '最新日K_US大盘_SPY')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_US大盘_token为0')
    def test_newdayKline_UStape_notoken(self):
        response = zhuorui('k线', '最新日K_US大盘_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_US大盘_type类型为2股票')
    def test_newdayKline_UStape__typeof2(self):
        response = zhuorui('k线', '最新日K_US大盘_type类型为2股票')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_US大盘_type不正确')
    def test_newdayKline_UStape_typeError(self):
        response = zhuorui('k线', '最新日K_US大盘_type不正确')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.json())

    @allure.story('最新日K_US大盘_type为空')
    def test_newdayKline_UStape_typeNone(self):
        response = zhuorui('k线', '最新日K_US大盘_type为空')
        assert_data(response, '000103', 'type is not null')
        # print(response.json())

    @allure.story('最新日K_US大盘_adjType类型为2前复权')
    def test_newdayKline_UStape_adjTypeof2(self):
        response = zhuorui('k线', '最新日K_US大盘_adjType类型为2前复权')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_US大盘_adjType类型为3后复权')
    def test_newdayKline_UStape_adjTypeof3(self):
        response = zhuorui('k线', '最新日K_US大盘_adjType类型为3后复权')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_US大盘_code异常')
    def test_newdayKline_UStape_codeException(self):
        response = zhuorui('k线', '最新日K_US大盘_code异常')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_US大盘_code不正确')
    def test_newdayKline_UStape_codeError(self):
        response = zhuorui('k线', '最新日K_US大盘_code不正确')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_US大盘_只传ts')
    def test_newdayKline_UStape_onlyvalts(self):
        response = zhuorui('k线', '最新日K_US大盘_只传ts')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('最新日K_US大盘_只传code')
    def test_newdayKline_UStape_onlyvalcode(self):
        response = zhuorui('k线', '最新日K_US大盘_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('最新日K_US大盘_只传type')
    def test_newdayKline_UStape_onlyvaltype(self):
        response = zhuorui('k线', '最新日K_US大盘_只传type')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('最新日K_US大盘只传adjType')
    def test_newdayKline_UStapeonlyvaladjType(self):
        response = zhuorui('k线', '最新日K_US大盘只传adjType')
        # assert_data(response, '000000', 'ok')
        print(response)

    @allure.story('最新日K_US大盘_code为空')
    def test_newdayKline_UStape_codeNone(self):
        response = zhuorui('k线', '最新日K_US大盘_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('最新日K_US大盘_ts为其他string')
    def test_newdayKline_UStape_tsotherstring(self):
        response = zhuorui('k线', '最新日K_US大盘_ts为其他string')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('最新日K_US大盘_ts为空')
    def test_newdayKline_UStape_tsNone(self):
        response = zhuorui('k线', '最新日K_US大盘_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    # @allure.story('最新日K_US大盘')
    # def test_newdayKline_UStape(self):
    #     response = zhuorui('k线', '最新日K_US大盘')
    #     # assert_data(response, '000000', 'ok')
    #     print(response.json())

