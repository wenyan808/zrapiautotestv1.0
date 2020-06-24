import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockF10Briefing:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('F10简况')
    def test_Astock_F10_briefing(self):
        response = zhuorui('A股', 'F10简况')
        # print(response)
        assert_data(response, '000000', 'ok')


