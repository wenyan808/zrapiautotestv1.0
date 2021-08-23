import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@pytest.mark.skip(reason="调试中 ")
class TestBroker:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询新闻内容')
    def test_getpricehktype1(self):
        response = zhuorui('个股详情公共接口', '查询新闻内容')
        assert_data(response, '000000', 'ok')