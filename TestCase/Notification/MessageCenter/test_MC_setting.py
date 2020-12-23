import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_MC_setting
# @pytest.mark.skip(reason="调试中 ")
@allure.feature('消息通知')
class TestMCsetting:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('推送设置_all')
    def test_MC_setting_allofTrue(self):
        response = zhuorui('消息通知', '推送设置_all')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())


    @allure.story('推送设置_全部为False')
    def test_MC_setting_allofFalse(self):
        response = zhuorui('消息通知', '推送设置_全部为False')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())


    @allure.story('推送设置_noticeColumn为False')
    def test_MC_setting_noticeColumnofFalse(self):
        response = zhuorui('消息通知', '推送设置_noticeColumn为False')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('推送设置_sound为False')
    def test_MC_setting_soundofFalse(self):
        response = zhuorui('消息通知', '推送设置_sound为False')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('推送设置_shock为False')
    def test_MC_setting_shockofFalse(self):
        response = zhuorui('消息通知', '推送设置_shock为False')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('推送设置_orderDeal为False')
    def test_MC_setting_orderDealofFalse(self):
        response = zhuorui('消息通知', '推送设置_orderDeal为False')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('推送设置_stockPrice为False')
    def test_MC_setting_stockPriceofFalse(self):
        response = zhuorui('消息通知', '推送设置_stockPrice为False')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('推送设置_参数为空')
    def test_MC_setting_ParamofNone(self):
        response = zhuorui('消息通知', '推送设置_参数为空')
        assert response.status_code == 200
        assert_data(response, '000104', '参数为空')
        # print(response.json())

    @allure.story('推送设置_只传noticeColumn')
    def test_MC_setting_onlyvalnoticeColumn(self):
        response = zhuorui('消息通知', '推送设置_只传noticeColumn')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('推送设置_只传sound')
    def test_MC_setting_onlyvalsound(self):
        response = zhuorui('消息通知', '推送设置_只传sound')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('推送设置_只传shock')
    def test_MC_setting_onlyvalshock(self):
        response = zhuorui('消息通知', '推送设置_只传shock')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('推送设置_只传orderDeal')
    def test_MC_setting_onlyvalorderDeal(self):
        response = zhuorui('消息通知', '推送设置_只传orderDeal')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('推送设置_只传stockPrice')
    def test_MC_setting_onlyvalstockPrice(self):
        response = zhuorui('消息通知', '推送设置_只传stockPrice')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())

    # @allure.story('推送设置')
    # def test_MC_setting(self):
    #     response = zhuorui('消息通知', '推送设置')
    #     assert response.status_code == 200
    #     assert_data(response, '000000', 'ok')
    #     # print(response.json())