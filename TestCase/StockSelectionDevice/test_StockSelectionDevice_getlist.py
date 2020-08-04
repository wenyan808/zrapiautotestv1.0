import allure
# import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason="状态显示未完成，目前无法运行")
@allure.feature('选股器')
class TestStockSelectionDeviceGetlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取行业列表_HK')
    def test_StockSelectionDevice_getlist_HK(self):
        response = zhuorui('选股器', '获取行业列表_HK')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            # assert response.json().get("data")
            # print(response.json().get("data")[0])
            # print(response.json().get("data")[1].get("code"))
            if len(response.json().get("data")) != 0:
                for info in response.json().get("data"):
                    # print(info)
                    if "0501" in info:
                        assert response.json().get("data")[0].get("code") == "0501"
                        assert response.json().get("data")[0].get("name") == "医疗保健设备与服务"
                    if "0402" in info:
                        assert response.json().get("data")[1].get("code") == "0402"
                        assert response.json().get("data")[1].get("name") == "综合金融服务"

    @allure.story('获取行业列表_HK')
    def test_StockSelectionDevice_getlist_US(self):
        response = zhuorui('选股器', '获取行业列表_US')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            # assert response.json().get("data")
            # print(response.json().get("data")[1])
            # print(response.json().get("data")[1].get("code"))
            if len(response.json().get("data")) != 0:
                for info in response.json().get("data"):
                    # print(info)
                    if "4850" in info:
                        assert response.json().get("data")[0].get("code") == "4850"
                        assert response.json().get("data")[0].get("name") == "金融集团"
                    if "2430" in info:
                        assert response.json().get("data")[1].get("code") == "2430"
                        assert response.json().get("data")[1].get("name") == "烟草"

    @allure.story('获取行业列表_HK')
    def test_StockSelectionDevice_getlist_A(self):
        response = zhuorui('选股器', '获取行业列表_A')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            # assert response.json().get("data")
            # print(response.json().get("data")[0])
            # print(response.json().get("data")[1].get("code"))
            if len(response.json().get("data")) != 0:
                for info in response.json().get("data"):
                    # print(info)
                    if "370100" in info:
                        assert response.json().get("data")[0].get("code") == "370100"
                        assert response.json().get("data")[0].get("name") == "化学制药"
                    if "240401" in info:
                        assert response.json().get("data")[1].get("code") == "240401"
                        assert response.json().get("data")[1].get("name") == "黄金"

    @allure.story('获取行业列表_无token')
    def test_StockSelectionDevice_getlist_Notoken(self):
        response = zhuorui('选股器', '获取行业列表_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            # assert response.json().get("data")
            # print(response.json().get("data")[0])
            # print(response.json().get("data")[1].get("code"))
            if len(response.json().get("data")) != 0:
                for info in response.json().get("data"):
                    # print(info)
                    if "0501" in info:
                        assert response.json().get("data")[0].get("code") == "0501"
                        assert response.json().get("data")[0].get("name") == "医疗保健设备与服务"
                    if "0402" in info:
                        assert response.json().get("data")[1].get("code") == "0402"
                        assert response.json().get("data")[1].get("name") == "综合金融服务"
