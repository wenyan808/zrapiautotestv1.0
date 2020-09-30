import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_MC_setinforead

@allure.feature('消息通知')
class TestMCsetinforead:
    @classmethod
    def setup_class(cls) -> None:
        login()
    @pytest.mark.skip(reason="等待功能实现")
    @allure.story('设置消息为已读-订单消息已读')
    def test_MC_setinforead_type01(self):
        response = zhuorui('消息通知', '设置消息为已读-订单消息已读')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @pytest.mark.skip(reason="等待功能实现")
    @allure.story('设置消息为已读-系统通知已读')
    def test_MC_setinforead_type02(self):
        response = zhuorui('消息通知', '设置消息为已读-系统通知已读')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('设置消息为已读-订阅提醒已读')
    def test_MC_setinforead_type03(self):
        response = zhuorui('消息通知', '设置消息为已读-订阅提醒已读')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('设置消息为已读-全部已读')
    def test_MC_setinforead_type00(self):
        response = zhuorui('消息通知', '设置消息为已读-全部已读')
        assert response.status_code == 200
        # assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('设置消息为已读-参数为空')
    def test_MC_setinforead_paramNone(self):
        response = zhuorui('消息通知', '设置消息为已读-参数为空')
        assert response.status_code == 200
        # assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('设置消息为已读-只传messageId')
    def test_MC_setinforead_onlyvalmessageId(self):
        response = zhuorui('消息通知', '设置消息为已读-只传messageId')
        assert response.status_code == 200
        # assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('设置消息为已读-只传type')
    def test_MC_setinforead_onlyvaltype(self):
        response = zhuorui('消息通知', '设置消息为已读-只传type')
        assert response.status_code == 200
        # assert_data(response, '000000', 'ok')
        # print(response.json())