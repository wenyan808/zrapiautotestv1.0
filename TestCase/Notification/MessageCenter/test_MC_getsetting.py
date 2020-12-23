import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_MC_getsetting

@allure.feature('消息通知')
class TestMCgetsetting:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取用户推送设置')
    def test_MC_getsetting(self):
        response = zhuorui('消息通知', '获取用户推送设置')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())
        assert response.json().get("data").get('noticeColumn') == True
        assert response.json().get("data").get("sound") == True
        assert response.json().get("data").get("shock") == True
        assert "shutOffs" in response.json().get("data")
