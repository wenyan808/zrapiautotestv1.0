import allure
# import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason="")
@allure.feature('A股')
class TestHKstockF10shareholderlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('F10获取持股变动列表分页')
    def test_HKstock_F10share_holderlist(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_无token')
    def test_HKstock_F10share_holderlist_notoken(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_ts为空')
    def test_HKstock_F10share_holderlist_tsNone(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_code为空')
    def test_HKstock_F10share_holderlist_codeNone(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_code为空')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_ts为中文')
    def test_HKstock_F10share_holderlist_tsofchinese(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_code为中文')
    def test_HKstock_F10share_holderlist_codeofchinese(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_code为中文')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())



    @allure.story('F10获取持股变动列表分页_只传ts')
    def test_HKstock_F10share_holderlist_onlyvalts(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_只传ts')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_只传code')
    def test_HKstock_F10share_holderlist_onlyvalcode(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_只传code')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_参数为空')
    def test_HKstock_F10share_holderlist_bobyNone(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_参数为空')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_all')
    def test_HKstock_F10share_holderlist_all(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_all')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_currentPage为空')
    def test_HKstock_F10share_holderlist_currentPageNone(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_currentPage为空')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_currentPage不正确')
    def test_HKstock_F10share_holderlist_currentPageError(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_currentPage不正确')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())



    @allure.story('F10获取持股变动列表分页_pageSize为空')
    def test_HKstock_F10share_holderlist_pageSizeNone(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_pageSize为空')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_pageSize不正确')
    def test_HKstock_F10share_holderlist_pageSizeError(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_pageSize不正确')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_只传currentPage')
    def test_HKstock_F10share_holderlist_onlyvalcurrentPage(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_只传currentPage')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取持股变动列表分页_只传pageSize')
    def test_HKstock_F10share_holderlist_onlyvalpageSize(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页_只传pageSize')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
