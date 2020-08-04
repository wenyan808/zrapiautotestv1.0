import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@pytest.mark.skip(reason="状态显示未完成，目前无法运行")
@allure.feature('选股器')
class TestStockSelectionDeviceModify:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('修改策略_1-中国香港')
    def test_StockSelectionDevice_modify01(self):
        response = zhuorui('选股器', '修改策略_1-中国香港')
        if response.json().get("code") == "000000":
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == "450001":
            assert_data(response, '450001', '策略名称已存在')
        elif response.json().get("code") == "450002":
            assert_data(response, '450002', '操作失败')
        assert response.status_code == 200
        # print(response.json())