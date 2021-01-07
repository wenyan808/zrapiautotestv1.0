import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_MessagesApi

@allure.feature('消息通知')
class TestMessagesApi:
    @classmethod
    def setup_class(cls) -> None:
        login()
    # @pytest.mark.skip(reason="等待功能实现")
    @allure.story('发送登陆短信验证码')
    def test_MessagesApi01_send_login_code(self):
        response = zhuorui('消息通知', '发送登陆短信验证码')
        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == "030002":
            assert_data(response, '030002', '当天短信验证码超过次数')
        else:
            raise AssertionError("您已超出今日验证次数，请明日再试")
        # print(response.json())

    # @pytest.mark.skip(reason="等待功能实现")
    @allure.story('找回密码发送短信验证码')
    def test_MessagesApi02_send_forget_code(self):
        response = zhuorui('消息通知', '找回密码发送短信验证码')
        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == "030002":
            assert_data(response, '030002', '当天短信验证码超过次数')
        else:
            raise AssertionError("当天短信验证码超过次数")
        # print(response.json())

    # @pytest.mark.skip(reason="等待功能实现")
    @allure.story('修改手机号发送短信验证码-当前手机号')
    def test_MessagesApisend03_old_replace_code(self):
        response = zhuorui('消息通知', '修改手机号发送短信验证码-当前手机号')
        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == "030002":
            assert_data(response, '030002', '当天短信验证码超过次数')
        else:
            raise AssertionError("当天短信验证码超过次数")
        # print(response.json())

    # @pytest.mark.skip(reason="等待功能实现")
    @allure.story('修改手机号发送短信验证码-新手机号')
    def test_MessagesApi04_send_new_replace_code(self):
        response = zhuorui('消息通知', '修改手机号发送短信验证码-新手机号')
        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == "030002":
            assert_data(response, '030002', '当天短信验证码超过次数')
        else:
            raise AssertionError("当天短信验证码超过次数")
        # print(response.json())