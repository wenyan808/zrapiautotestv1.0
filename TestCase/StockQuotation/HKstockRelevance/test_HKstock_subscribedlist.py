import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason='调试中')
@allure.feature('港股')
class TestHKstocknewstocklist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('新股日历获取可认购列表')
    def test_HKstock_subscribedlist(self):
        response = zhuorui('港股', '新股日历获取可认购列表')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('新股日历获取可认购列表_无token')
    def test_HKstock_subscribedlist_notoken(self):
        response = zhuorui('港股', '新股日历获取可认购列表_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
