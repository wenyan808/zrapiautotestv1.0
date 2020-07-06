import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('搜索')
class TestKeywordSearch:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('关键字查询股票_数字个股')
    def test_KeywordSearch_digitshare(self):
        response = zhuorui('搜索', '关键字查询股票_数字个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('关键字查询股票_必须参数数字')
    def test_KeywordSearch_onlydigit(self):
        response = zhuorui('搜索', '关键字查询股票_必须参数数字')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('关键字查询股票_必须参数字母')
    def test_KeywordSearch_onlyletter(self):
        response = zhuorui('搜索', '关键字查询股票_必须参数字母')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('关键字查询股票_必须参数中文')
    def test_KeywordSearch_onlychinese(self):
        response = zhuorui('搜索', '关键字查询股票_必须参数中文')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('关键字查询股票_字母大盘')
    def test_KeywordSearch_chinesetape(self):
        response = zhuorui('搜索', '关键字查询股票_字母大盘')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('关键字查询股票_字母个股')
    def test_KeywordSearch_chineseshare(self):
        response = zhuorui('搜索', '关键字查询股票_字母个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('关键字查询股票_数字大盘')
    def test_KeywordSearch_digittape(self):
        response = zhuorui('搜索', '关键字查询股票_数字大盘')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('关键字查询股票_中文个股')
    def test_KeywordSearch_chineseshare(self):
        response = zhuorui('搜索', '关键字查询股票_中文个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('关键字查询股票_中文大盘')
    def test_KeywordSearch_chinesetape(self):
        response = zhuorui('搜索', '关键字查询股票_中文大盘')
        assert_data(response, '000000', 'ok')
        # print(response.text)


