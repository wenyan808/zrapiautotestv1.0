import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
# test_getCommonInfo
# @pytest.mark.skip(reason="调试中}")
@allure.feature('公共基本信息')
class TestgetCommonInfo:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('公共基本信息')
    def test_getCommonInfo(self):
        response = zhuorui('公共基本信息', '公共基本信息')
        assert response.status_code == 200
        assert_data(response, '000000', 'ok')
        # print(response.json())