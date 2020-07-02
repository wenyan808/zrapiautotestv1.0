import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockF10getIncomeStatementData:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('A股F10获取利润表详情页数据_SZ')
    def test_Astock_F10getIncomeStatementData_SZ(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_SZ')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_token为0')
    def test_Astock_F10getIncomeStatementData_notoken(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_ts为空')
    def test_Astock_F10getIncomeStatementData_tsNone(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_ts为空')
        assert_data(response, '000103', 'ts不能为空')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_ts为异常')
    def test_Astock_F10getIncomeStatementData_tsException(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_ts为异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_code为空')
    def test_Astock_F10getIncomeStatementData_codeNone(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_code为空')
        assert_data(response, '000103', 'code不能为空')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_ts为错误')
    def test_Astock_F10getIncomeStatementData_tsError(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_ts为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_code为异常')
    def test_Astock_F10getIncomeStatementData_codeException(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_code为异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_code为错误')
    def test_Astock_F10getIncomeStatementData_codeError(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_code为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_SH')
    def test_Astock_F10getIncomeStatementData_SH(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_SH')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_HK')
    def test_Astock_F10getIncomeStatementData_HK(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_HK')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_US')
    def test_Astock_F10getIncomeStatementData_US(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_US')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_pageSize为空')
    def test_Astock_F10getIncomeStatementData_pageSizeNone(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_pageSize为空')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_pageSize为异常')
    def test_Astock_F10getIncomeStatementData_pageSizeException(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_pageSize为异常')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_pageSize为错误')
    def test_Astock_F10getIncomeStatementData_pageSizeError(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_pageSize为错误')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_currentPage为空')
    def test_Astock_F10getIncomeStatementData_currentPageNone(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_currentPage为空')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_currentPage为错误')
    def test_Astock_F10getIncomeStatementData_currentPageError(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_currentPage为错误')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_SZ')
    def test_Astock_F10getIncomeStatementData_currentPageException(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_SZ')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_type全部')
    def test_Astock_F10getIncomeStatementData_typeall(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_type全部')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_type年报')
    def test_Astock_F10getIncomeStatementData_typeOf1(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_type年报')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_type中报')
    def test_Astock_F10getIncomeStatementData_typeOf2(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_type中报')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_type一季度')
    def test_Astock_F10getIncomeStatementData_typeOf3(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_type一季度')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_type三季度')
    def test_Astock_F10getIncomeStatementData_typeOf4(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_type三季度')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_必传值')
    def test_Astock_F10getIncomeStatementData_require(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_必传值')
        assert_data(response, '000000', 'ok')
        # print(response.text)














