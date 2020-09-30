import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_MC_Unreadcount

@allure.feature('消息通知')
class TestMCUnreadcount:
    @classmethod
    def setup_class(cls) -> None:
        login()
    # @pytest.mark.skip(reason="等待功能实现")
    @allure.story('未读消息数')
    def test_MC_Unreadcount(self):
        response = zhuorui('消息通知', '未读消息数')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())
