import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
# test_Push
@pytest.mark.skip(reason="目前无法运行")
@allure.feature('推送')
class TestPush:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('公告推送-业务类')
    def test_Push_Notice(self):
        response = zhuorui('消息通知', '公告推送-业务类')
        assert response.status_code == 200
        # if response.json().get("code") == '000000':
        #     assert_data(response, '000000', 'ok')
        # elif response.json().get("code") == '030102':
        #     assert_data(response, '030102', '上报设备信息失败')
        # else:
        #     raise ("服务器错误")

        # print(response.json())

    @allure.story('股价涨跌提醒推送-通知类')
    def test_Push_Shares_of_remind(self):
        response = zhuorui('消息通知', '股价涨跌提醒推送-通知类')
        assert response.status_code == 200
        # if response.json().get("code") == '000000':
        #     assert_data(response, '000000', 'ok')
        # elif response.json().get("code") == '030102':
        #     assert_data(response, '030102', '上报设备信息失败')
        # else:
        #     raise ("服务器错误")

        # print(response.json())

    @allure.story('开户成功-通知类')
    def test_Push_accountSuccesse(self):
        response = zhuorui('消息通知', '开户成功-通知类')
        assert response.status_code == 200
        # if response.json().get("code") == '000000':
        #     assert_data(response, '000000', 'ok')
        # elif response.json().get("code") == '030102':
        #     assert_data(response, '030102', '上报设备信息失败')
        # else:
        #     raise ("服务器错误")

        # print(response.json())

    @allure.story('开户失败-通知类')
    def test_Push_accountFailure(self):
        response = zhuorui('消息通知', '开户失败-通知类')
        assert response.status_code == 200
        # if response.json().get("code") == '000000':
        #     assert_data(response, '000000', 'ok')
        # elif response.json().get("code") == '030102':
        #     assert_data(response, '030102', '上报设备信息失败')
        # else:
        #     raise ("服务器错误")

        # print(response.json())

    @allure.story('欢迎加入-通知类')
    def test_Push_welcomejoin(self):
        response = zhuorui('消息通知', '欢迎加入-通知类')
        assert response.status_code == 200
        # if response.json().get("code") == '000000':
        #     assert_data(response, '000000', 'ok')
        # elif response.json().get("code") == '030102':
        #     assert_data(response, '030102', '上报设备信息失败')
        # else:
        #     raise ("服务器错误")

        # print(response.json())