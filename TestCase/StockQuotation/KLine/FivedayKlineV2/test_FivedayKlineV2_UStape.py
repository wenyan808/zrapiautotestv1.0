import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestFivedayKlinev2UStape:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_DIA')
    def test_fivedayKlinev2_UStape_DIA(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_DIA')
        # assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_SPY')
    def test_fivedayKlinev2_UStape_SPY(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_SPY')
        # assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_QQQ')
    def test_fivedayKlinev2_UStape_QQQ(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_QQQ')
        # assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    # @allure.story('五日查询_优化版本 Version 2.0_US大盘')
    # def test_fivedayKlinev2_UStape(self):
    #     response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘')
    #     # assert_data(response, '000000', 'ok')
    #     assert response.status_code == 200
    #     # print(response.json())
    #
    # @allure.story('五日查询_优化版本 Version 2.0_US大盘')
    # def test_fivedayKlinev2_UStape(self):
    #     response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘')
    #     assert_data(response, '000000', 'ok')
    #     assert response.status_code == 200
    #     # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_token为0')
    def test_fivedayKlinev2_UStape_notoken(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_token为0')
        # assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_type类型为2股票')
    def test_fivedayKlinev2_UStape_typeof2(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_type类型为2股票')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_type类型为3基金')
    def test_fivedayKlinev2_UStape_typeof3(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_type类型为3基金')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_adjType类型为2前复权')
    def test_fivedayKlinev2_UStape_adjTypeof2(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_adjType类型为2前复权')
        # assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_adjType类型为3后复权')
    def test_fivedayKlinev2_UStape_adjTypeof3(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_adjType类型为3后复权')
        # assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_ts为空')
    def test_fivedayKlinev2_UStape_tsNone(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_ts为中文')
    def test_fivedayKlinev2_UStape_tschinese(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_code为空')
    def test_fivedayKlinev2_UStape_codeNone(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_code不正确')
    def test_fivedayKlinev2_UStape_codeError(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_code不正确')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_type不正确')
    def test_fivedayKlinev2_UStape_typeError(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_type不正确')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_type为空')
    def test_fivedayKlinev2_UStape_typeNone(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_type为空')
        # assert_data(response, '000103', 'type is not null')
        assert_data(response, "000000", "ok")
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_adjType为空')
    def test_fivedayKlinev2_UStape_adjTypeNone(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_adjType为空')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_pageSize条数为0')
    def test_fivedayKlinev2_UStape_pageSizeofzero(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_pageSize条数为0')
        # assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_pageSize条数为负数')
    def test_fivedayKlinev2_UStape_pageSizeofminus(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_pageSize条数为负数')
        # assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_只传ts')
    def test_fivedayKlinev2_UStape_onlyvalts(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_只传ts')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_只传code')
    def test_fivedayKlinev2_UStape_onlyvalcode(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_只传type')
    def test_fivedayKlinev2_UStape_onlyvaltype(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_只传type')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_只传adjType')
    def test_fivedayKlinev2_UStape_onlyvaladjType(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_只传adjType')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US大盘_只传pageSize')
    def test_fivedayKlinev2_UStape_onlyvalpageSize(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US大盘_只传pageSize')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())
