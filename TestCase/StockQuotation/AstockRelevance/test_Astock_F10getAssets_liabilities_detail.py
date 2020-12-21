import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockF10getAssetsLiabilitiesDetail:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('A股F10获取资产负债详情页数据_SZ')
    def test_Astock_F10getAssets_liabilities_detail_SZ(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_SZ')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_SH')
    def test_Astock_F10getAssets_liabilities_detail_SH(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_SH')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_HK')
    def test_Astock_F10getAssets_liabilities_detail_HK(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_HK')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_US')
    def test_Astock_F10getAssets_liabilities_detail_US(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_US')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_token为0')
    def test_Astock_F10getAssets_liabilities_detail_Notoken(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_ts为空')
    def test_Astock_F10getAssets_liabilities_detail_tsNone(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_ts为空')
        assert_data(response, '000103', 'ts不能为空')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_ts为错误')
    def test_Astock_F10getAssets_liabilities_detail_tsError(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_ts为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_ts为异常')
    def test_Astock_F10getAssets_liabilities_detail_tsException(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_ts为异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_code为空')
    def test_Astock_F10getAssets_liabilities_detail_codeNone(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_code为空')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_code为异常')
    def test_Astock_F10getAssets_liabilities_detail_codeException(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_code为异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_code为错误')
    def test_Astock_F10getAssets_liabilities_detail_codeError(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_code为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_pageSize为空')
    def test_Astock_F10getAssets_liabilities_detail_pageSizeNone(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_pageSize为空')
        assert_data(response, '000103', 'must not be null')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_pageSize为错误')
    def test_Astock_F10getAssets_liabilities_detail_pageSizeError(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_pageSize为错误')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_pageSize为异常')
    def test_Astock_F10getAssets_liabilities_detail_pageSizeException(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_pageSize为异常')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_currentPage为空')
    def test_Astock_F10getAssets_liabilities_detail_currentPageNone(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_currentPage为空')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_currentPage为错误')
    def test_Astock_F10getAssets_liabilities_detail_currentPageError(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_currentPage为错误')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_currentPage为异常')
    def test_Astock_F10getAssets_liabilities_detail_currentPageException(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_currentPage为异常')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_type全部')
    def test_Astock_F10getAssets_liabilities_detail_typeall(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_type全部')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_type年报')
    def test_Astock_F10getAssets_liabilities_detail_typeyear(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_type年报')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_type中报')
    def test_Astock_F10getAssets_liabilities_detail_typeOf2(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_type中报')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_type一季度')
    def test_Astock_F10getAssets_liabilities_detail_typeOf3(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_type一季度')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_type三季度')
    def test_Astock_F10getAssets_liabilities_detail_typeOf4(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_type三季度')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_type中报')
    def test_Astock_F10getAssets_liabilities_detail_typeOf2(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_type中报')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取资产负债详情页数据_必传值')
    def test_Astock_F10getAssets_liabilities_detail_require(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据_必传值')
        assert_data(response, '000000', 'ok')
        # print(response.text)
