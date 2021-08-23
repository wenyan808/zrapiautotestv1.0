# test_SOR_deleteonestock
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason="调试中")
@allure.feature('股价提醒')
class TestSORDeleteonestock:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('删除配置')
    def test_SOR_deleteonestock(self):
        response = zhuorui('Allstock', '删除配置')
        assert_data(response, '000000', 'ok')