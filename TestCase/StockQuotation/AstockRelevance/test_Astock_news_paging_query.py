"""
@File  ：test_ModifyLoginPassword02.py
@Author: yishouquan
@Time  : 2020/7/29
@Desc  :  A股-个股新闻分页查询（废除）
"""
import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
@pytest.mark.skip(reason="已废弃")
class TestAstockNewsPagingQuery:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('个股新闻分页查询')
    def test_Astock_news_paging_query(self):
        response = zhuorui('A股', '个股新闻分页查询')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('个股新闻分页查询_token为0')
    def test_Astock_news_paging_query_notoken(self):
        response = zhuorui('A股', '个股新闻分页查询_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('个股新闻分页查询_ts为空')
    def test_Astock_news_paging_query_tsNone(self):
        response = zhuorui('A股', '个股新闻分页查询_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('个股新闻分页查询_ts为异常')
    def test_Astock_news_paging_query_tsException(self):
        response = zhuorui('A股', '个股新闻分页查询_ts为异常')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('个股新闻分页查询_ts为错误')
    def test_Astock_news_paging_query_tsError(self):
        response = zhuorui('A股', '个股新闻分页查询_ts为错误')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('个股新闻分页查询_code为空')
    def test_Astock_news_paging_query_codeNone(self):
        response = zhuorui('A股', '个股新闻分页查询_code为空')
        assert_data(response, '000103', 'code不能为空')
        # print(response.json())

    @allure.story('个股新闻分页查询_code为异常')
    def test_Astock_news_paging_query_codeException(self):
        response = zhuorui('A股', '个股新闻分页查询_code为异常')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('个股新闻分页查询_code为错误')
    def test_Astock_news_paging_query_codeError(self):
        response = zhuorui('A股', '个股新闻分页查询_code为错误')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('个股新闻分页查询_pageSize为空')
    def test_Astock_news_paging_query_pageSizeNone(self):
        response = zhuorui('A股', '个股新闻分页查询_pageSize为空')
        assert_data(response, '000103', 'must not be null')
        # print(response.json())

    @allure.story('个股新闻分页查询_pageSize为异常')
    def test_Astock_news_paging_query_pageSizeException(self):
        response = zhuorui('A股', '个股新闻分页查询_pageSize为异常')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.json())

    @allure.story('个股新闻分页查询_pageSize为错误')
    def test_Astock_news_paging_query_pageSizeError(self):
        response = zhuorui('A股', '个股新闻分页查询_pageSize为错误')
        assert_data(response, '000103', '超过限制')
        # print(response.json())

    @allure.story('个股新闻分页查询_currentPage为空')
    def test_Astock_news_paging_query_currentPageError(self):
        response = zhuorui('A股', '个股新闻分页查询_currentPage为空')
        assert_data(response, '000000', 'ok')
        # print(response.json())
    #
    @allure.story('个股新闻分页查询_currentPage为异常')
    def test_Astock_news_paging_query_currentPageException(self):
        response = zhuorui('A股', '个股新闻分页查询_currentPage为异常')
        assert_data(response, '000103', '参数不合法')
        # print(response.json())

    @allure.story('个股新闻分页查询_currentPage为错误')
    def test_Astock_news_paging_query_currentPageError(self):
        response = zhuorui('A股', '个股新闻分页查询_currentPage为错误')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.json())

    @allure.story('个股新闻分页查询_必填项')
    def test_Astock_news_paging_query_required(self):
        response = zhuorui('A股', '个股新闻分页查询_必填项')
        assert_data(response, '000000', 'ok')
        # print(response.json())




