import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason='调试中')
@allure.feature('港股')
class TestHKstockF10F10cashflowdetail:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('港股F10获取现金流量报表详情数据')
    def test_HKstock_F10cashflowdetail(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_无token')
    def test_HKstock_F10cashflowdetail_notoken(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_ts为空')
    def test_HKstock_F10cashflowdetail_tsNone(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_code为空')
    def test_HKstock_F10cashflowdetail_codeNone(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_code为空')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_ts为中文')
    def test_HKstock_F10cashflowdetail_tsofchinese(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_code为中文')
    def test_HKstock_F10cashflowdetail_codeofchinese(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_code为中文')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_只传ts')
    def test_HKstock_F10cashflowdetail_onlyvalts(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_只传ts')
        assert_data(response, '000103', 'must not be null')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_只传code')
    def test_HKstock_F10cashflowdetail_onlyvalcode(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_只传code')
        # assert_data(response, '000103', 'must not be null')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_参数为空')
    def test_HKstock_F10cashflowdetail_bobyNone(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_参数为空')
        assert_data(response, '000103', 'must not be null')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_all')
    def test_HKstock_F10cashflowdetail_all(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_all')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_currentPage为空')
    def test_HKstock_F10cashflowdetail_currentPageNone(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_currentPage为空')
        # assert_data(response, '000103', 'must not be null')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_currentPage不正确')
    def test_HKstock_F10cashflowdetail_currentPageError(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_currentPage不正确')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_pageSize为空')
    def test_HKstock_F10cashflowdetail_pageSizeNone(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_pageSize为空')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_pageSize不正确')
    def test_HKstock_F10cashflowdetail_pageSizeError(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_pageSize不正确')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_只传currentPage')
    def test_HKstock_F10cashflowdetail_onlyvalcurrentPage(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_只传currentPage')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_只传pageSize')
    def test_HKstock_F10cashflowdetail_onlyvalpageSize(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_只传pageSize')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_type为0')
    def test_HKstock_F10cashflowdetail_typeofzero(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_type为0')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_type为1')
    def test_HKstock_F10cashflowdetail_typeofone(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_type为1')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_type为2')
    def test_HKstock_F10cashflowdetail_typeoftwo(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_type为2')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_type为3')
    def test_HKstock_F10cashflowdetail_typeofthree(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_type为3')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_type为4')
    def test_HKstock_F10cashflowdetail_typeoffour(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_type为4')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_type为空')
    def test_HKstock_F10cashflowdetail_typeNone(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_type为空')
        assert_data(response, '000103', 'must not be null')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_type为10')
    def test_HKstock_F10cashflowdetail_typeoften(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_type为10')
        assert_data(response, '000103', 'type请求不符')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10获取现金流量报表详情数据_type负数')
    def test_HKstock_F10cashflowdetail_typeofminus(self):
        response = zhuorui('港股', '港股F10获取现金流量报表详情数据_type负数')
        assert_data(response, '000103', 'type请求不符')
        assert response.status_code == 200
        # print(response.json())
