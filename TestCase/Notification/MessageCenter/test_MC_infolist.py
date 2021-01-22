import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_MC_infolist

@allure.feature('消息通知')
class TestMCinfolist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('消息列表_订单消息模块')
    def test_MC_infolist_type01(self):
        response = zhuorui('消息通知', '消息列表_订单消息模块')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('消息列表_系统通知模块')
    def test_MC_infolist_type02(self):
        response = zhuorui('消息通知', '消息列表_系统通知模块')
        # assert response.status_code == 200
        # assert_data(response, '000000', 'ok')
        print(response.json())

    @allure.story('消息列表_订阅提醒模块')
    def test_MC_infolist_type03(self):
        response = zhuorui('消息通知', '消息列表_订阅提醒模块')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('社区-相关通知消息模块')
    def test_MC_infolist(self):
        response = zhuorui('消息通知', '社区-相关通知消息模块')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    # @allure.story('消息列表_all')
    # def test_MC_infolist_all(self):
    #     response = zhuorui('消息通知', '消息列表_all')
    #     assert response.status_code == 200
    #     assert_data(response, '000000', 'ok')
    #     # print(response.json())
    #
    # @allure.story('消息列表_createTime为空')
    # def test_MC_infolist_createTimeNone(self):
    #     response = zhuorui('消息通知', '消息列表_createTime为空')
    #     assert response.status_code == 200
    #     assert_data(response, '000000', 'ok')
    #     # print(response.json())