import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('港股')
class TestHKstockF10repolist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('全部论证-牛熊街货00700')
    def test_HKstock_warrantnxjh(self):
        response = zhuorui('港股', '全部论证-牛熊街货00700')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-牛熊街货HSI')
    def test_HKstock_warrantnxjhHSI(self):
        response = zhuorui('港股', '全部论证-牛熊街货HSI')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-牛熊街货00700收回价5')
    def test_HKstock_warrantnxjhshj5(self):
        response = zhuorui('港股', '全部论证-牛熊街货00700收回价5')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-牛熊街货00700收回价10')
    def test_HKstock_warrantnxjhshk10(self):
        response = zhuorui('港股', '全部论证-牛熊街货00700收回价10')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-牛熊街货00700收回价20')
    def test_HKstock_warrantnxjhshk20(self):
        response = zhuorui('港股', '全部论证-牛熊街货00700收回价20')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
