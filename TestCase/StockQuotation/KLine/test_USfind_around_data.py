import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('搜索')
class TestKeywordSearch:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('美股分时盘前查询')
    def test_USBEFROE(self):
        response = zhuorui('k线', '美股分时盘前查询')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('美股分时盘后查询')
    def test_USAFTER(self):
        response = zhuorui('k线', '美股分时盘后查询')
        assert_data(response, '000000', 'ok')
        # print(response.json())

