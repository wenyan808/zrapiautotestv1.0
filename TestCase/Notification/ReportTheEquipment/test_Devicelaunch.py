
import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
# test_Devicelaunch

@allure.feature('消息通知')
class TestDevicelaunch:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取到个推clientId时执行上报设备信息')
    def test_Devicelaunch(self):
        response = zhuorui('消息通知', '获取到个推clientId时执行上报设备信息')
        assert response.status_code == 200
        if response.json().get("code") == '000000':
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == '030102':
            assert_data(response, '030102', '上报设备信息失败')
        else:
            raise ("服务器错误")

        # print(response.json())

    @allure.story('获取到个推clientId时执行上报设备信息_个推id为空')
    def test_Devicelaunch_clientIdNone(self):
        response = zhuorui('消息通知', '获取到个推clientId时执行上报设备信息_个推id为空')
        assert response.status_code == 200
        assert_data(response, '000103', 'must not be blank')
        # print(response.json())