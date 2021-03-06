import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestNewdayKlineUSshare:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('最新日K_US个股')
    def test_newdayKline_USshare(self):
        response = zhuorui('k线', '最新日K_US个股')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_US个股_token为0')
    def test_newdayKline_USshare_notoken(self):
        response = zhuorui('k线', '最新日K_US个股_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('最新日K_US个股_type类型为1指数')
    def test_newdayKline_USshare_typeOf1(self):
        response = zhuorui('k线', '最新日K_US个股_type类型为1指数')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('最新日K_US个股_type不正确')
    def test_newdayKline_USshare_typeError(self):
        response = zhuorui('k线', '最新日K_US个股_type不正确')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('最新日K_US个股_type为空')
    def test_newdayKline_USshare_typeError(self):
        response = zhuorui('k线', '最新日K_US个股_type为空')
        # assert_data(response, '000103', 'type is not null')
        assert_data(response, "000000", "ok")
        # print(response.text)

    @allure.story('最新日K_US个股_adjType为空')
    def test_newdayKline_USshare_adjTypeError(self):
        response = zhuorui('k线', '最新日K_US个股_adjType为空')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.text)

    @allure.story('最新日K_US个股_adjType类型为2前复权')
    def test_newdayKline_USshare_adjTypeOf2(self):
        response = zhuorui('k线', '最新日K_US个股_adjType类型为2前复权')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('最新日K_US个股_adjType类型为3后复权')
    def test_newdayKline_USshare_adjTypeOf3(self):
        response = zhuorui('k线', '最新日K_US个股_adjType类型为3后复权')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('最新日K_US个股_ts为空')
    def test_newdayKline_USshare_tsNone(self):
        response = zhuorui('k线', '最新日K_US个股_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('最新日K_US个股_ts为其他string')
    def test_newdayKline_USshare_tsotherstring(self):
        response = zhuorui('k线', '最新日K_US个股_ts为其他string')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('最新日K_US个股_code为空')
    def test_newdayKline_USshare_codeNone(self):
        response = zhuorui('k线', '最新日K_US个股_code为空')
        # assert_data(response, '000103', 'code格式有误')
        assert_data(response, '000103', 'code is not null')
        assert response.status_code == 200
        # print(response.text)

    # @allure.story('最新日K_US个股_code异常')
    # def test_newdayKline_USshare_codeException(self):
    #     response = zhuorui('k线', '最新日K_US个股_code异常')
    #     # assert_data(response, '000000', 'ok')
    #     print(response.text)
    #
    # @allure.story('最新日K_US个股_code不正确')
    # def test_newdayKline_USshare_codeError(self):
    #     response = zhuorui('k线', '最新日K_US个股_code不正确')
    #     # assert_data(response, '000000', 'ok')
    #     print(response.text)

    @allure.story('最新日K_US个股_只传ts')
    def test_newdayKline_USshare_onlyts(self):
        response = zhuorui('k线', '最新日K_US个股_只传ts')
        # assert_data(response, '000103', 'code格式有误')
        assert_data(response, '000103', 'code is not null')
        assert response.status_code == 200
        # print(response.text)

    @allure.story('最新日K_US个股_只传code')
    def test_newdayKline_USshare_onlycode(self):
        response = zhuorui('k线', '最新日K_US个股_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('最新日K_US个股_只传type')
    def test_newdayKline_USshare_onlytype(self):
        response = zhuorui('k线', '最新日K_US个股_只传type')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('最新日K_US个股_只传adjType')
    def test_newdayKline_USshare_onlyadjType(self):
        response = zhuorui('k线', '最新日K_US个股_只传adjType')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

