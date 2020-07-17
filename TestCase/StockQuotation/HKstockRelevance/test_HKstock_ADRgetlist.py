import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class testHKstockADRgetlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('ADR列表 -港股ADR')
    def test_HKstock_ADRgetlist(self):
        response = zhuorui('港股', 'ADR列表-港股ADR')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表 -港股ADR_无token')
    def test_HKstock_ADRgetlist_notoken(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表-港股ADR_currentPage为2')
    def test_HKstock_ADRgetlist_currentPageoftwo(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_currentPage为2')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表-港股ADR_currentPage为空')
    def test_HKstock_ADRgetlist_currentPageNone(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_currentPage为空')
        # assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表-港股ADR_pageSize为空')
    def test_HKstock_ADRgetlist_pageSizeNone(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_pageSize为空')
        # assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表-港股ADR_asc为空')
    def test_HKstock_ADRgetlist_ascNone(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_asc为空')
        assert_data(response, '000103', 'asc is null')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表-港股ADR_pageSize为1')
    def test_HKstock_ADRgetlist_pageSizeofone(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_pageSize为1')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表-港股ADR_currentPage不正确')
    def test_HKstock_ADRgetlist_currentPageError(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_currentPage不正确')
        assert_data(response, '000103', '参数校验不通过')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表-港股ADR_pageSize不正确')
    def test_HKstock_ADRgetlist_pageSizeError(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_pageSize不正确')
        assert_data(response, '000103', '参数校验不通过')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表-港股ADR_asc不正确')
    def test_HKstock_ADRgetlist_ascError(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_asc不正确')
        assert_data(response, '000103', '参数校验不通过')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表-港股ADR_只传currentPage')
    def test_HKstock_ADRgetlist_onlyvalcurrentPage(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_只传currentPage')
        assert_data(response, '000103', 'asc is null')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表-港股ADR_只传pageSize')
    def test_HKstock_ADRgetlist_onlyvalpageSize(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_只传pageSize')
        assert_data(response, '000103', 'asc is null')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('ADR列表-港股ADR_只传asc')
    def test_HKstock_ADRgetlist_onlyvalasc(self):
        response = zhuorui('港股', 'ADR列表-港股ADR_只传asc')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    # @allure.story('ADR列表-港股ADR')
    # def test_HKstock_ADRgetlist(self):
    #     response = zhuorui('港股', 'ADR列表-港股ADR')
    #     assert_data(response, '000000', 'ok')
    #     assert response.status_code == 200
    #     # print(response.json())

    # @allure.story('ADR列表-港股ADR')
    # def test_HKstock_ADRgetlist(self):
    #     response = zhuorui('港股', 'ADR列表-港股ADR')
    #     assert_data(response, '000000', 'ok')
    #     assert response.status_code == 200
    #     # print(response.json())
