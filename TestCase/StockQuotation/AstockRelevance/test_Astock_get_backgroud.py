import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockGetBackgroud:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取高管的简介')
    def test_Astock_get_backgroud(self):
        response = zhuorui('A股', '获取高管的简介')
        assert_data(response, '000000', 'ok')