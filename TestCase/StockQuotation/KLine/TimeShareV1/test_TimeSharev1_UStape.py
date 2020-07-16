import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@pytest.mark.skip(reason="该测试用例版本过低，pass")
@allure.feature('k线')
class TestTimeKlinev1UStape:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('分时查询_US大盘')
    def test_timeKlinev1_UStape(self):
        response = zhuorui('k线', '分时查询_US大盘')
        assert_data(response, '000000', 'ok')
        # print(response.text)