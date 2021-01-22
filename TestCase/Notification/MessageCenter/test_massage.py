import os
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
import pytest

@allure.feature('消息通知')
class TestMessage():

    @classmethod
    def setup_class(cls):
        login()
        pass

    def teardown(cls):
        pass
    @allure.story("查询最新一条消息无token")
    def test_message_01last1(self):
        response = zhuorui("消息通知", "查询最新一条消息无token")
        assert_data(response, "000101", "token不能为空")

    @allure.story("查询最新一条消息")
    def test_message_01last2(self):
        response = zhuorui("消息通知", "查询最新一条消息")
        assert_data(response, "000000", "ok")

    @allure.story("查询最新一条消息_参数为空")
    def test_message_01last3(self):
        response = zhuorui("消息通知", "查询最新一条消息_参数为空")
        assert_data(response, "000000", "ok")

    @allure.story("查询最新一条消息_参数为string")
    def test_message_01last4(self):
        response = zhuorui("消息通知", "查询最新一条消息_参数为string")
        assert_data(response, "000103", "参数校验不通过")

    @allure.story("消息详情")
    def test_message_detail(self):
        response = zhuorui("消息通知", "消息详情")
        assert_data(response, "000000", "ok")

    @allure.story("消息详情无koen")
    def test_message_detai2(self):
        response = zhuorui("消息通知", "消息详情无token")
        assert_data(response, "000101", "token不能为空")

    @allure.story("消息详情_参数为空")
    def test_message_detai3(self):
        response = zhuorui("消息通知", "消息详情_参数为空")
        assert_data(response, '000103', 'messageId can not be null')

    @allure.story("消息详情_参数不存在")
    def test_message_detai4(self):
        response = zhuorui("消息通知", "消息详情_参数不存在")
        assert_data(response, '000105', '参数错误')

    @allure.story("推送设置_关闭股价提醒")
    def test_message_setting2(self):
        response = zhuorui("消息通知", "推送设置_关闭股价提醒")
        assert_data(response, "000000", "ok")

    @allure.story("推送设置无token")
    def test_message_setting1(self):
        response = zhuorui("消息通知", "推送设置无token")
        assert_data(response, "000101", "token不能为空")

    @allure.story("推送设置参数为空")
    def test_message_setting3(self):
        response = zhuorui("消息通知", "推送设置参数为空")
        assert_data(response, '000104', '参数为空')

    @allure.story("推送设置参数为string")
    def test_message_setting4(self):
        response = zhuorui("消息通知", "推送设置参数为string")

        assert_data(response, '000103','参数校验不通过')

    @allure.story("获取用户推送设置")
    def test_message_getsetting1(self):
        response = zhuorui("消息通知", "获取用户推送设置")
        assert_data(response, "000000", "ok")
    @allure.story("获取用户推送设置无token")
    def test_message_getsetting2(self):
        response = zhuorui("消息通知", "获取用户推送设置无token")
        assert_data(response, "000101", "token不能为空")

    @allure.story("获取用户推送设置_不存在参数")
    def test_message_getsetting3(self):
        response = zhuorui("消息通知", "获取用户推送设置_不存在参数")
        assert_data(response, '000000', 'ok')

    @allure.story("未读消息数")
    def test_message_unreadcount1(self):
        response = zhuorui("消息通知", "未读消息数")
        assert_data(response, "000000", "ok")

    @allure.story("未读消息数无token")
    def test_message_unreadcount2(self):
        response = zhuorui("消息通知", "未读消息数无token")
        assert_data(response, "000101", "token不能为空")

    @allure.story("未读消息数_不存在参数")
    def test_message_unreadcount3(self):
        response = zhuorui("消息通知", "未读消息数_不存在参数")
        assert_data(response, '000000', 'ok')

    @allure.story("设置消息为已读")
    def test_message_read1(self):
        response = zhuorui("消息通知", "设置消息为已读")
        assert_data(response, "000000", "ok")

    @allure.story("设置消息为已读无token")
    def test_message_read2(self):
        response = zhuorui("消息通知", "设置消息为已读无token")
        assert_data(response, "000101", "token不能为空")

    @allure.story("设置消息为已读_参数为空")
    def test_message_read3(self):
        response = zhuorui("消息通知", "设置消息为已读_参数为空")
        assert_data(response, '000103', "type can not be null")

    @allure.story("设置消息为已读_参数不存在")
    def test_message_read4(self):
        response = zhuorui("消息通知", "设置消息为已读_参数不存在")
        assert_data(response, '000000', 'ok')

    @allure.story("消息列表")
    def test_message_list1(self):
        response = zhuorui("消息通知", "消息列表")
        assert_data(response, "000000", "ok")

    @allure.story("消息列表无token")
    def test_message_list2(self):
        response = zhuorui("消息通知", "消息列表无token")
        assert_data(response, "000101", "token不能为空")

    @allure.story("消息列表参数为空")
    def test_message_list3(self):
        response = zhuorui("消息通知", "消息列表参数为空")
        assert_data(response, '000103', 'type can not be null')

    @allure.story("消息列表参数不存在")
    def test_message_list4(self):
        response = zhuorui("消息通知", "消息列表参数不存在")
        assert_data(response, '000000', 'ok')

    @allure.story("删除消息")
    def test_message_delete1(self):
        response = zhuorui("消息通知", "删除消息")
        assert_data(response, "000000", "ok")

    @allure.story("删除消息无token")
    def test_message_delete2(self):
        response = zhuorui("消息通知", "删除消息无token")
        assert_data(response, "000101", "token不能为空")

    @allure.story("删除消息_不存在数据")
    def test_message_delete3(self):
        response =zhuorui("消息通知", "删除消息_不存在数据")
        assert_data(response, '000000', 'ok')

    @allure.story("删除消息_参数为空")
    def test_message_delete4(self):
        response = zhuorui("消息通知", "删除消息_参数为空")
        assert_data(response, '000103', 'messageId can not be null')
