import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockNewsPagingQuery:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('个股新闻分页查询')
    def test_Astock_news_paging_query(self):
        response = zhuorui('A股', '个股新闻分页查询')
        assert_data(response, '000000', 'ok')
