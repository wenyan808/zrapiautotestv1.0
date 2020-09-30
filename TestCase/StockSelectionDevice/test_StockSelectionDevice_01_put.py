import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('选股器')
class TestStockSelectionDevicePut:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('保存策略_1-中国香港')
    def test_StockSelectionDevice_put01(self):
        response = zhuorui('选股器', '保存策略_1-中国香港')
        assert response.status_code == 200
        # print(response.json())
        if response.json().get("code") == "000000":
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == "450001":
            assert_data(response, '450001', '策略名称已存在')


    @allure.story('保存策略_2-美国')
    def test_StockSelectionDevice_put02(self):
        response = zhuorui('选股器', '保存策略_2-美国')
        if response.json().get("code") == "000000":
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == "450001":
            assert_data(response, '450001', '策略名称已存在')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('保存策略_3-中国')
    def test_StockSelectionDevice_put03(self):
        response = zhuorui('选股器', '保存策略_3-中国')
        if response.json().get("code") == "000000":
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == "450001":
            assert_data(response, '450001', '策略名称已存在')
        assert response.status_code == 200
        # print(response.json())

    # @allure.story('保存策略')
    # def test_StockSelectionDevice_put01(self):
    #     response = zhuorui('选股器', '保存策略')
    #     assert_data(response, '000000', 'ok')
    #     assert response.status_code == 200
    #     # print(response.json())
