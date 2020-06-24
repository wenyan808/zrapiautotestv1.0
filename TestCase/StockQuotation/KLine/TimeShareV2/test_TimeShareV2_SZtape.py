import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestKlinev2SZtapeTimeshare:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('分时查询_优化版本 Version 2.0_SZ大盘')
    def test_Kline_v2SZtape_timeshare(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_SZ大盘')
        assert_data(response, '000000', 'ok')