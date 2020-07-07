import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_xlsx_exampleshuju import shuju


@allure.feature('k线')
class TestNewdayKlineSHtape:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('最新日K_SH大盘_000001')
    def test_newdayKline_SHtape_000001(self):
        response = zhuorui('k线', '最新日K_SH大盘_000001')
        assert_data(response, '000000', 'ok')
        # print(response.json())
        # if "data" in response.json():
        #     # assert response.json().get("data")
        #     # print(response.json().get("data")[1])
        #     if len(response.json().get("data")) != 0:
        #         for info in response.json().get("data"):
        #             for i in shuju('k线'):
        #                 if '最新日K_SH大盘_000001' in i:
        #                     calculate1 = i[9]
        #                     calculate = eval(calculate1)
        #                     print(calculate)
        #                     # print(calculate.get("type"))
        #                     # assert info.get("ts") == calculate.get("ts")
        #                     # print(calculate.get("ts"))
        #                     # assert info.get("code") == calculate.get("code")
        #                     # assert info.get("type") == int(calculate.get("type"))
        #                     # assert info.get("adjType") == calculate.get("adjType")
        #                     # print(info)
        #                     # print(info.get("adj"))
        #                     adj = info.get("adj")
        #                     if adj != None:
        #                         assert info.get("adj") == calculate.get("adj")
        #                     # else:
        #                     #     raise NameError
        #     elif len(response.json().get("data")) == 0:
        #         print("data无数据")
        #     else:
        #
        #         raise TypeError

    @allure.story('最新日K_SH大盘_000159')
    def test_newdayKline_SHtape_000159(self):
        response = zhuorui('k线', '最新日K_SH大盘_000159')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_SH大盘_token为0')
    def test_newdayKline_SHtape_notoken(self):
        response = zhuorui('k线', '最新日K_SH大盘_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.json())


    @allure.story('最新日K_SH大盘_type类型为2股票')
    def test_newdayKline_SHtape_typeof2(self):
        response = zhuorui('k线', '最新日K_SH大盘_type类型为2股票')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_SH大盘_type不正确')
    def test_newdayKline_SHtape_typeError(self):
        response = zhuorui('k线', '最新日K_SH大盘_type不正确')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.json())

    @allure.story('最新日K_SH大盘_type为空')
    def test_newdayKline_SHtape_typeNone(self):
        response = zhuorui('k线', '最新日K_SH大盘_type为空')
        assert_data(response, '000103', 'type is not null')
        # print(response.json())

    @allure.story('最新日K_SH大盘_adjType为空')
    def test_newdayKline_SHtape_adjTypeNone(self):
        response = zhuorui('k线', '最新日K_SH大盘_adjType为空')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.text)

    @allure.story('最新日K_SH大盘_adjType类型为2前复权')
    def test_newdayKline_SHtape_adjTypeof2(self):
        response = zhuorui('k线', '最新日K_SH大盘_adjType类型为2前复权')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_SH大盘_adjType类型为3后复权')
    def test_newdayKline_SHtape_adjTypeof3(self):
        response = zhuorui('k线', '最新日K_SH大盘_adjType类型为3后复权')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('最新日K_SH大盘_ts为空')
    def test_newdayKline_SHtape_tsNone(self):
        response = zhuorui('k线', '最新日K_SH大盘_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('最新日K_SH大盘_ts为其他string')
    def test_newdayKline_SHtape_tsotherstring(self):
        response = zhuorui('k线', '最新日K_SH大盘_ts为其他string')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('最新日K_SH大盘_code为空')
    def test_newdayKline_SHtape_codeNone(self):
        response = zhuorui('k线', '最新日K_SH大盘_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('最新日K_SH大盘_code异常')
    def test_newdayKline_SHtape_codeException(self):
        response = zhuorui('k线', '最新日K_SH大盘_code异常')
        # assert_data(response, '000000', 'ok')
        print(response.json())

    @allure.story('最新日K_SH大盘_code不正确')
    def test_newdayKline_SHtape_codeError(self):
        response = zhuorui('k线', '最新日K_SH大盘_code不正确')
        # assert_data(response, '000000', 'ok')
        print(response.json())

    @allure.story('最新日K_SH大盘_只传ts')
    def test_newdayKline_SHtape_onlyvalts(self):
        response = zhuorui('k线', '最新日K_SH大盘_只传ts')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('最新日K_SH大盘_只传code')
    def test_newdayKline_SHtape_onlyvalcode(self):
        response = zhuorui('k线', '最新日K_SH大盘_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('最新日K_SH大盘_只传type')
    def test_newdayKline_SHtape_onlyvaltype(self):
        response = zhuorui('k线', '最新日K_SH大盘_只传type')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('最新日K_SH大盘只传adjType')
    def test_newdayKline_SHtapeonlyvaladjType(self):
        response = zhuorui('k线', '最新日K_SH大盘只传adjType')
        # assert_data(response, '000103', 'ts格式有误')
        print(response)
    #
    # @allure.story('最新日K_SH大盘')
    # def test_newdayKline_SHtape(self):
    #     response = zhuorui('k线', '最新日K_SH大盘')
    #     assert_data(response, '000000', 'ok')
    #     # print(response.json())







