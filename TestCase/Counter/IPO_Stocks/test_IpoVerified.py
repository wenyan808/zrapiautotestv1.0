import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
# test_IpoVerified
@pytest.mark.skip(reason="调试中}")
@allure.feature('新股认购')
class TestIpoVerified:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('认购前验证')
    def test_IpoVerified(self):
        response = zhuorui('柜台', '认购前验证')
        assert response.status_code == 200
        # assert_data(response, '000000', 'ok')
        print(response.json())