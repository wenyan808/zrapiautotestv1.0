import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestCandleMinute:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('带蜡烛图的分钟查询_HK')
    def test_candleMinute_HK(self):
        response = zhuorui('k线', '带蜡烛图的分钟查询_HK')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('带蜡烛图的分钟查询_US')
    def test_candleMinute_US(self):
        response = zhuorui('k线', '带蜡烛图的分钟查询_US')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('带蜡烛图的分钟查询_SH')
    def test_candleMinute_SH(self):
        response = zhuorui('k线', '带蜡烛图的分钟查询_SH')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('带蜡烛图的分钟查询_SZ')
    def test_candleMinute_SZ(self):
        response = zhuorui('k线', '带蜡烛图的分钟查询_SZ')
        assert_data(response, '000000', 'ok')
        # print(response.text)