import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestTimeSharev2SZtape:
    @classmethod
    def setup_class(cls) -> None:
        login()

    # @allure.story('分时查询_优化版本 Version 2.0_SZ大盘')
    # def test_timeSharev2_SZtape(self):
    #     response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘')
    #     assert_data(response, '000000', 'ok')

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_399001')
    def test_timeSharev2_SZtape_399001(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_399001')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_399006')
    def test_timeSharev2_SZtape_399006(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_399006')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_token为0')
    def test_timeSharev2_SZtape_notoken(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_token为0')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ盘_type类型为2股票')
    def test_timeSharev2_SZtape_typeof2(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_type类型为2股票')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_type类型为3基金')
    def test_timeSharev2_SZtape_typeof3(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_type类型为3基金')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_adjType类型为2前复权')
    def test_timeSharev2_SZtape_adjTypeof2(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_adjType类型为2前复权')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_adjType类型为3后复权')
    def test_timeSharev2_SZtape_adjTypeof3(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_adjType类型为3后复权')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_ts为空')
    def test_timeSharev2_SZtape_tsNone(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_ts为中文')
    def test_timeSharev2_SZtapetschinese(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_code为空')
    def test_timeSharev2_SZtape_codeNone(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_code不正确')
    def test_timeSharev2_SZtape_codeError(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_code不正确')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_type不正确')
    def test_timeSharev2_SZtape_typeError(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_type不正确')
        # assert_data(response, '000103', '参数校验不通过')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_type为空')
    def test_timeSharev2_SZtape_typeNone(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_type为空')
        # assert_data(response, '000103', 'type is not null')
        assert_data(response, "000000", "ok")
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_adjType为空')
    def test_timeSharev2_SZtape_adjTypeNone(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_adjType为空')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.json())

    # @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_pageSize条数为0')
    # def test_timeSharev2_SZtape_pageSizeofzero(self):
    #     response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_pageSize条数为0')
    #     assert_data(response, '000000', 'ok')
    #     # print(response.json())

    # @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_pageSize条数为负数')
    # def test_timeSharev2_SZtape_pageSizeofminus(self):
    #     response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_pageSize条数为负数')
    #     # assert_data(response, '000000', 'ok')
    #     print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_只传ts')
    def test_timeSharev2_SZtape_onlyvalts(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_只传ts')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_只传code')
    def test_timeSharev2_SZtape_onlyvalcode(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_只传type')
    def test_timeSharev2_SZtape_onlyvaltype(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_只传type')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘_只传adjType')
    def test_timeSharev2_SZtape_onlyvaladjType(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘_只传adjType')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

