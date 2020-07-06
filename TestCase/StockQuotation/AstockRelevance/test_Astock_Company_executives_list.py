import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockCompanyExecutivesList:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('公司高管列表-详情页_token为0')
    def test_Astock_Company_executives_list_notoken(self):
        response = zhuorui('A股', '公司高管列表-详情页_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('公司高管列表-详情页_ts为空')
    def test_Astock_Company_executives_list_tsNone(self):
        response = zhuorui('A股', '公司高管列表-详情页_ts为空')
        assert_data(response, '000103', 'ts不能为空')
        # print(response.text)

    @allure.story('公司高管列表-详情页_ts为异常')
    def test_Astock_Company_executives_list_tsException(self):
        response = zhuorui('A股', '公司高管列表-详情页_ts为异常')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('公司高管列表-详情页_ts为错误')
    def test_Astock_Company_executives_list_tsError(self):
        response = zhuorui('A股', '公司高管列表-详情页_ts为错误')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('公司高管列表-详情页_只传值ts')
    def test_Astock_Company_executives_list_Onlyvalts(self):
        response = zhuorui('A股', '公司高管列表-详情页_只传值ts')
        assert_data(response, '000103', 'code不能为空')
        # print(response.text)

    @allure.story('公司高管列表-详情页_code为空')
    def test_Astock_Company_executives_list_codeNone(self):
        response = zhuorui('A股', '公司高管列表-详情页_code为空')
        assert_data(response, '000103', 'code不能为空')
        # print(response.text)

    @allure.story('公司高管列表-详情页_code为异常')
    def test_Astock_Company_executives_list_codeException(self):
        response = zhuorui('A股', '公司高管列表-详情页_code为异常')
        assert_data(response, '000103', 'code格式有误')
        # print(response.text)

    @allure.story('公司高管列表-详情页_code为错误')
    def test_Astock_Company_executives_list_codeError(self):
        response = zhuorui('A股', '公司高管列表-详情页_code为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('公司高管列表-详情页_只传值code')
    def test_Astock_Company_executives_list_Onlyvalcode(self):
        response = zhuorui('A股', '公司高管列表-详情页_只传值code')
        assert_data(response, '000103', 'ts不能为空')
        # print(response.text)

    @allure.story('公司高管列表-详情页_pageSize为空')
    def test_Astock_Company_executives_list_pageSizeNone(self):
        response = zhuorui('A股', '公司高管列表-详情页_pageSize为空')
        assert_data(response, '000103', 'must not be null')
        # print(response.text)

    @allure.story('公司高管列表-详情页_pageSize为异常')
    def test_Astock_Company_executives_list_pageSizeException(self):
        response = zhuorui('A股', '公司高管列表-详情页_pageSize为异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('公司高管列表-详情页_pageSize为错误')
    def test_Astock_Company_executives_list_pageSizeError(self):
        response = zhuorui('A股', '公司高管列表-详情页_pageSize为错误')
        assert_data(response, '000103', 'pageSize参数不合法1-50')
        # print(response.text)

    @allure.story('公司高管列表-详情页_只传值pageSize')
    def test_Astock_Company_executives_list_OnlyvalpageSize(self):
        response = zhuorui('A股', '公司高管列表-详情页_只传值pageSize')
        assert_data(response, '000103', 'ts不能为空')
        # print(response.text)

    @allure.story('公司高管列表-详情页_currentPage为空')
    def test_Astock_Company_executives_list_currentPageNone(self):
        response = zhuorui('A股', '公司高管列表-详情页_currentPage为空')
        assert_data(response, '000103', 'must not be null')
        # print(response.text)

    @allure.story('公司高管列表-详情页_currentPage为异常')
    def test_Astock_Company_executives_list_currentPageException(self):
        response = zhuorui('A股', '公司高管列表-详情页_currentPage为异常')
        assert_data(response, '000103', 'currentPage参数不合法>1')
        # print(response.text)

    @allure.story('公司高管列表-详情页_currentPage为错误')
    def test_Astock_Company_executives_list_currentPageError(self):
        response = zhuorui('A股', '公司高管列表-详情页_currentPage为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('公司高管列表-详情页_只传值currentPage')
    def test_Astock_Company_executives_list_OnlyvalcurrentPage(self):
        response = zhuorui('A股', '公司高管列表-详情页_只传值currentPage')
        assert_data(response, '000103', 'ts不能为空')
        # print(response.text)

    @allure.story('公司高管列表-详情页_参数为空')
    def test_Astock_Company_executives_list_ParameterNull(self):
        response = zhuorui('A股', '公司高管列表-详情页_参数为空')
        assert_data(response, '000103', 'ts不能为空')
        # print(response.text)
