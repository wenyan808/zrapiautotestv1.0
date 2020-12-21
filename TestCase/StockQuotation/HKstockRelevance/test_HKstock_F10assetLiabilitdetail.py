import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason='调试中')
@allure.feature('港股')
class TestHKstockF10assetLiabilitdetail:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('港股F10获取资产负债详情页数据')
    def test_HKstock_F10assetLiabilitdetail(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_无token')
    def test_HKstock_F10assetLiabilitdetail_notoken(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取利润表详情页数据_ts为空')
    def test_HKstock_F10assetLiabilitdetail_tsNone(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取利润表详情页数据_code为空')
    def test_HKstock_F10assetLiabilitdetail_codeNone(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_code为空')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_ts为中文')
    def test_HKstock_F10assetLiabilitdetail_tsofchinese(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_code为中文')
    def test_HKstock_F10assetLiabilitdetail_codeofchinese(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_code为中文')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_只传ts')
    def test_HKstock_F10assetLiabilitdetail_onlyvalts(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_只传ts')
        assert_data(response, '000103', 'must not be null')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_只传code')
    def test_HKstock_F10assetLiabilitdetail_onlyvalcode(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_只传code')
        assert_data(response, '000103', 'must not be null')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_参数为空')
    def test_HKstock_F10assetLiabilitdetail_bobyNone(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_参数为空')
        assert_data(response, '000103', 'must not be null')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_all')
    def test_HKstock_F10assetLiabilitdetail_all(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_all')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_currentPage为空')
    def test_HKstock_F10assetLiabilitdetail_currentPageNone(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_currentPage为空')
        # assert_data(response, '000103', 'must not be null')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_currentPage不正确')
    def test_HKstock_F10assetLiabilitdetail_currentPageError(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_currentPage不正确')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_pageSize为空')
    def test_HKstock_F10assetLiabilitdetail_pageSizeNone(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_pageSize为空')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_pageSize不正确')
    def test_HKstock_F10assetLiabilitdetail_pageSizeError(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_pageSize不正确')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据只传currentPage')
    def test_HKstock_F10assetLiabilitdetail_onlyvalcurrentPage(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_只传currentPage')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_只传pageSize')
    def test_HKstock_F10assetLiabilitdetail_onlyvalpageSize(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_只传pageSize')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_type为0')
    def test_HKstock_F10assetLiabilitdetail_typeofzero(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_type为0')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_type为1')
    def test_HKstock_F10assetLiabilitdetail_typeofone(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_type为1')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_type为2')
    def test_HKstock_F10assetLiabilitdetail_typeoftwo(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_type为2')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_type为3')
    def test_HKstock_F10assetLiabilitdetail_typeofthree(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_type为3')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_type为4')
    def test_HKstock_F10assetLiabilitdetail_typeoffour(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_type为4')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_type为空')
    def test_HKstock_F10assetLiabilitdetail_typeNone(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_type为空')
        assert_data(response, '000103', 'must not be null')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_type为10')
    def test_HKstock_F10assetLiabilitdetail_typeoften(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_type为10')
        assert_data(response, '000103', 'type请求不符')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取资产负债详情页数据_type负数')
    def test_HKstock_F10assetLiabilitdetail_typeofminus(self):
        response = zhuorui('港股', '港股F10获取资产负债详情页数据_type负数')
        assert_data(response, '000103', 'type请求不符')
        assert response.status_code == 200
        # print(response.json())
