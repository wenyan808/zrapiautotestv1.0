import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockDividentsList:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('分红派息-详情页')
    def test_Astock_dividents_list(self):
        response = zhuorui('A股', '分红派息-详情页')
        assert_data(response, '000000', 'ok')
