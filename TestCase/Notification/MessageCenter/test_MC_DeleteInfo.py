import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_MC_DeleteInfo

@allure.feature('消息通知')
class TestMCDeleteInfo:
    @classmethod
    def setup_class(cls) -> None:
        login()
    @pytest.mark.skip(reason="等待功能实现")
    @allure.story('删除消息-系统通知模块')
    def test_MC_DeleteInfo_type02(self):
        response = zhuorui('消息通知', '删除消息-系统通知模块')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @pytest.mark.skip(reason="等待功能实现")
    @allure.story('删除消息-订阅提醒模块')
    def test_MC_DeleteInfo_type03(self):
        response = zhuorui('消息通知', '删除消息-订阅提醒模块')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response)
