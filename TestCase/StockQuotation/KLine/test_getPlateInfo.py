import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('板块信息')
class TestgetPlateInfo:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('根据ts和code获取板块信息_US行业')
    def test_getPlateInfo_US_business(self):
        response = zhuorui('板块信息', '根据ts和code获取板块信息_US行业')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据ts和code获取板块信息_US概念')
    def test_getPlateInfo_US_idea(self):
        response = zhuorui('板块信息', '根据ts和code获取板块信息_US概念')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据ts和code获取板块信息_SH行业')
    def test_getPlateInfo_SH_business(self):
        response = zhuorui('板块信息', '根据ts和code获取板块信息_SH行业')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据ts和code获取板块信息_SH概念')
    def test_getPlateInfo_SH_idea(self):
        response = zhuorui('板块信息', '根据ts和code获取板块信息_SH概念')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据ts和code获取板块信息_SZ行业')
    def test_getPlateInfo_SZ_business(self):
        response = zhuorui('板块信息', '根据ts和code获取板块信息_SZ行业')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据ts和code获取板块信息_SZ概念')
    def test_getPlateInfo_SZ_idea(self):
        response = zhuorui('板块信息', '根据ts和code获取板块信息_SZ概念')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据ts和code获取板块信息_HK行业')
    def test_getPlateInfo_HK_business(self):
        response = zhuorui('板块信息', '根据ts和code获取板块信息_HK行业')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据ts和code获取板块信息_HK概念')
    def test_getPlateInfo_HK_idea(self):
        response = zhuorui('板块信息', '根据ts和code获取板块信息_HK概念')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据板块code获取板块信息_US行业')
    def test_getPlateInfo_US_business(self):
        response = zhuorui('板块信息', '根据板块code获取板块信息_US行业')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据板块code获取板块信息_US概念')
    def test_getPlateInfo_US_idea(self):
        response = zhuorui('板块信息', '根据板块code获取板块信息_US概念')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据板块code获取板块信息_US行业')
    def test_getPlateInfo_US_business(self):
        response = zhuorui('板块信息', '根据板块code获取板块信息_US行业')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据板块code获取板块信息_US概念')
    def test_getPlateInfo_US_idea(self):
        response = zhuorui('板块信息', '根据板块code获取板块信息_US概念')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据板块code获取板块信息_HK行业')
    def test_getPlateInfo_HK_business(self):
        response = zhuorui('板块信息', '根据板块code获取板块信息_HK行业')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据板块code获取板块信息_HK概念')
    def test_getPlateInfo_HK_idea(self):
        response = zhuorui('板块信息', '根据板块code获取板块信息_HK概念')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据板块code获取板块信息_HS行业')
    def test_getPlateInfo_HS_business(self):
        response = zhuorui('板块信息', '根据板块code获取板块信息_HS行业')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('根据板块code获取板块信息_HS概念')
    def test_getPlateInfo_HS_idea(self):
        response = zhuorui('板块信息', '根据板块code获取板块信息_HS概念')
        assert_data(response, '000000', 'ok')
        # print(response.text)



