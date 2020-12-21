import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockF10getCashflowDetail:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('A股F10获取现金流量报表详情数据_SZ')
    def test_Astock_F10getCashflowDeta_SZ(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_SZ')
        # print(response.json())
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_SH')
    def test_Astock_F10getCashflowDeta_SH(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_SH')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_HK')
    def test_Astock_F10getCashflowDeta_HK(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_HK')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_US')
    def test_Astock_F10getCashflowDeta_US(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_US')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_token为0')
    def test_Astock_F10getCashflowDeta_notoken(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_token为0')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_ts为空')
    def test_Astock_F10getCashflowDeta_tsNone(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_ts为空')
        # print(response.text)
        assert_data(response, '000103', 'ts不能为空')

    @allure.story('A股F10获取现金流量报表详情数据_ts为错误')
    def test_Astock_F10getCashflowDeta_tsError(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_ts为错误')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_ts为异常')
    def test_Astock_F10getCashflowDeta_tsException(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_ts为异常')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_code为空')
    def test_Astock_F10getCashflowDeta_codeNone(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_code为空')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_code为错误')
    def test_Astock_F10getCashflowDeta_codeNone(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_code为错误')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_code为异常')
    def test_Astock_F10getCashflowDeta_codeException(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_code为异常')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_pageSize为空')
    def test_Astock_F10getCashflowDeta_pageSizeNone(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_pageSize为空')
        # print(response.text)
        assert_data(response, '000103', 'must not be null')

    @allure.story('A股F10获取现金流量报表详情数据_pageSize为异常')
    def test_Astock_F10getCashflowDeta_pageSizeException(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_pageSize为异常')
        # print(response.text)
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('A股F10获取现金流量报表详情数据_pageSize为错误')
    def test_Astock_F10getCashflowDeta_pageSizeError(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_pageSize为错误')
        # print(response.text)
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('A股F10获取现金流量报表详情数据_type全部')
    def test_Astock_F10getCashflowDeta_typeAll(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_type全部')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_type年报')
    def test_Astock_F10getCashflowDeta_typeyear(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_type年报')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_type中报')
    def test_Astock_F10getCashflowDeta_typeOf2(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_type中报')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_type一季度')
    def test_Astock_F10getCashflowDeta_typeOf3(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_type一季度')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_type三季度')
    def test_Astock_F10getCashflowDeta_typeOf4(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_type三季度')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_必传值')
    def test_Astock_F10getCashflowDeta_require(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_必传值')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_currentPage为空')
    def test_Astock_F10getCashflowDeta_currentPageNone(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_currentPage为空')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('A股F10获取现金流量报表详情数据_currentPage为错误')
    def test_Astock_F10getCashflowDeta_currentPageError(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_currentPage为错误')
        # print(response.text)
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('A股F10获取现金流量报表详情数据_currentPage为异常')
    def test_Astock_F10getCashflowDeta_currentPageException(self):
        response = zhuorui('A股', 'A股F10获取现金流量报表详情数据_currentPage为异常')
        # print(response.text)
        assert_data(response, '000103', '参数校验不通过')





