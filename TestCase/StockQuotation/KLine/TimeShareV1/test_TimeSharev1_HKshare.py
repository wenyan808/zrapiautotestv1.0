import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@pytest.mark.skip(reason="该测试用例版本过低，pass")
@allure.feature('k线')
class TestTimeKlinev1HKshare:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('分时查询_HK个股')
    def test_timeKlinev1_HKshare(self):
        response = zhuorui('k线', '分时查询_HK个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)