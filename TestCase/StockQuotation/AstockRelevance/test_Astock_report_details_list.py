import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockReportDetailsList:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('个股研报分页查询')
    def test_Astock_report_details_list(self):
        response = zhuorui('A股', '个股研报分页查询')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('个股研报分页查询_token为0')
    def test_Astock_report_details_list_notoken(self):
        response = zhuorui('A股', '个股研报分页查询_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('个股研报分页查询_ts为空')
    def test_Astock_report_details_list_tsNone(self):
        response = zhuorui('A股', '个股研报分页查询_ts为空')
        assert_data(response, '000103', 'ts不能为空')
        # print(response.text)

    @allure.story('个股研报分页查询_ts为错误')
    def test_Astock_report_details_list_tsError(self):
        response = zhuorui('A股', '个股研报分页查询_ts为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('个股研报分页查询_ts为异常')
    def test_Astock_report_details_list_tsException(self):
        response = zhuorui('A股', '个股研报分页查询_ts为异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('个股研报分页查询_code为空')
    def test_Astock_report_details_list_codeNone(self):
        response = zhuorui('A股', '个股研报分页查询_code为空')
        assert_data(response, '000103', 'code不能为空')
        # print(response.text)

    @allure.story('个股研报分页查询_code为异常')
    def test_Astock_report_details_list_codeException(self):
        response = zhuorui('A股', '个股研报分页查询_code为异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('个股研报分页查询_code为错误')
    def test_Astock_report_details_list_codeError(self):
        response = zhuorui('A股', '个股研报分页查询_code为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('个股研报分页查询_pageSize为空')
    def test_Astock_report_details_list_pageSizeNone(self):
        response = zhuorui('A股', '个股研报分页查询_pageSize为空')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('个股研报分页查询_pageSize为异常')
    def test_Astock_report_details_list_pageSizeException(self):
        response = zhuorui('A股', '个股研报分页查询_pageSize为异常')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('个股研报分页查询_pageSize为错误')
    def test_Astock_report_details_list_pageSizeError(self):
        response = zhuorui('A股', '个股研报分页查询_pageSize为错误')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('个股研报分页查询_currentPage为空')
    def test_Astock_report_details_list_currentPageNone(self):
        response = zhuorui('A股', '个股研报分页查询_currentPage为空')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('个股研报分页查询_currentPage为错误')
    def test_Astock_report_details_list_currentPageError(self):
        response = zhuorui('A股', '个股研报分页查询_currentPage为错误')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('个股研报分页查询_currentPage为异常')
    def test_Astock_report_details_list_currentPageException(self):
        response = zhuorui('A股', '个股研报分页查询_currentPage为异常')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('个股研报分页查询_必填项')
    def test_Astock_report_details_list_required(self):
        response = zhuorui('A股', '个股研报分页查询_必填项')
        assert_data(response, '000000', 'ok')
        # print(response.text)











