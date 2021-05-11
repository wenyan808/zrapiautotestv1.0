import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('港股')
class TestHKstockF10repolist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('轮证中心_轮证占大市成交')
    def test_HKstock_warrantds(self):
        response = zhuorui('港股', '轮证中心_轮证占大市成交')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('轮证中心_轮证资金流向')
    def test_HKstock_warrantzj(self):
        response = zhuorui('港股', '轮证中心_轮证资金流向')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('轮证中心_成交活跃股牛熊证')
    def test_HKstock_warrantnx(self):
        response = zhuorui('港股', '轮证中心_成交活跃股牛熊证')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('轮证中心_成交活跃股涡轮')
    def test_HKstock_warrantwl(self):
        response = zhuorui('港股', '轮证中心_成交活跃股涡轮')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('轮证中心_成交活跃股界内证')
    def test_HKstock_warrantjn(self):
        response = zhuorui('港股', '轮证中心_成交活跃股界内证')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200


