import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@pytest.mark.skip(reason="状态显示未完成，目前无法运行")
@allure.feature('k线')
class TestCandleMinute1Min:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取行业列表_HK')
    def test_StockSelectionDevice_getlist_HK(self):
        response = zhuorui('选股器', '获取行业列表_HK')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
