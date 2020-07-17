import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestFivedayKlinev2USshare:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('五日查询_优化版本 Version 2.0_US个股')
    def test_fivedayKlinev2_USshare(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response)

    @allure.story('五日查询_优化版本 Version 2.0_US个股_token为0')
    def test_fivedayKlinev2_USshare_notoken(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_token为0')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
    #
    # @allure.story('五日查询_优化版本 Version 2.0_US个股_type类型为1指数')
    # def test_fivedayKlinev2_USshare_typeof1(self):
    #     response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_type类型为1指数')
    #     assert_data(response, '000000', 'ok')
    #     assert response.status_code == 200
    #     # print(response)

    @allure.story('五日查询_优化版本 Version 2.0_US个股_type类型为3基金')
    def test_fivedayKlinev2_USshare_typeof3(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_type类型为3基金')
        assert_data(response, '000000', 'ok')
        # assert_data(response, '000001', '系统繁忙,请稍候再试')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_adjType类型为2前复权')
    def test_fivedayKlinev2_USshare_adjTypeof2(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_adjType类型为2前复权')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_adjType类型为3后复权')
    def test_fivedayKlinev2_USshare_adjTypeof3(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_adjType类型为3后复权')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_ts为空')
    def test_fivedayKlinev2_USshare_tsNone(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_ts为中文')
    def test_fivedayKlinev2_USshare_tschinese(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_code为空')
    def test_fivedayKlinev2_USshare_codeNone(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_code不正确')
    def test_fivedayKlinev2_USshare_codeError(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_code不正确')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_type不正确')
    def test_fivedayKlinev2_USshare_typeError(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_type不正确')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_type为空')
    def test_fivedayKlinev2_USshare_typeNone(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_type为空')
        assert_data(response, '000103', 'type is not null')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_adjType为空')
    def test_fivedayKlinev2_USshare_adjTypeNone(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_adjType为空')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_pageSize条数为0')
    def test_fivedayKlinev2_USshare_pageSizeofzero(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_pageSize条数为0')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_pageSize条数为负数')
    def test_fivedayKlinev2_USshare_pageSizeofminus(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_pageSize条数为负数')
        assert_data(response, '000000', 'ok')
        # assert_data(response, '000001', '系统繁忙,请稍候再试')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_只传ts')
    def test_fivedayKlinev2_USshare_onlyvalts(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_只传ts')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_只传code')
    def test_fivedayKlinev2_USshare_onlyvalcode(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    # @allure.story('五日查询_优化版本 Version 2.0_US个股_只传type')
    # def test_fivedayKlinev2_USshare_onlyvaltype(self):
    #     response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US股_只传type')
    #     # assert_data(response, '000103', 'ts格式有误')
    #     print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US股_只传adjType')
    def test_fivedayKlinev2_USshare_onlyvaladjType(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_只传adjType')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('五日查询_优化版本 Version 2.0_US个股_只传pageSize')
    def test_fivedayKlinev2_USshare_onlyvalpageSize(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_US个股_只传pageSize')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())