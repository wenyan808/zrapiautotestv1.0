import allure
# import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason="")
@allure.feature('A股')
class TestHKstockF10profile:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('F10获取持股变动列表分页')
    def test_HKstock_F10profile(self):
        response = zhuorui('港股', 'F10获取持股变动列表分页')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
