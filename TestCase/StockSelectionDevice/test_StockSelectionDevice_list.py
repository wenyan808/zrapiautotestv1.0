import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

# @pytest.mark.skip(reason="状态显示未完成，目前无法运行")
@allure.feature('选股器')
class TestStockSelectionDeviceList:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('用户所有策略列表查询')
    def test_StockSelectionDevice_list(self):
        response = zhuorui('Allstock', '用户所有策略条数查询')
        assert_data(response, '000000', 'ok')
        # if "data" in response.json():
            # if len(response.json().get("data")) != 0:
            #     # for info in j.get("data"):
            #     #     pass