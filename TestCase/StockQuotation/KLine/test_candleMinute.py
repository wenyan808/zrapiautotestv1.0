import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestCandleMinute:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('带蜡烛图的分钟查询')
    def test_candle_minute(self):
        response = zhuorui('k线', '带蜡烛图的分钟查询')
        assert_data(response, '000000', 'ok')
        # print(response.text)