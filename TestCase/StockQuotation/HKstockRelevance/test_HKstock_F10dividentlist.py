import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('港股')
class TestHKstockF10dividentlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('F10获取分红派息列表')
    def test_HKstock_F10dividentlist(self):
        response = zhuorui('港股', 'F10获取分红派息列表')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取分红派息列表_无token')
    def test_HKstock_F10dividentlist_notoken(self):
        response = zhuorui('港股', 'F10获取分红派息列表_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取分红派息列表_ts为空')
    def test_HKstock_F10dividentlist_tsNone(self):
        response = zhuorui('港股', 'F10获取分红派息列表_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取分红派息列表_ts为中文')
    def test_HKstock_F10dividentlist_tschinese(self):
        response = zhuorui('港股', 'F10获取分红派息列表_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取分红派息列表_code为空')
    def test_HKstock_F10dividentlist_codeNone(self):
        response = zhuorui('港股', 'F10获取分红派息列表_code为空')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取分红派息列表_code为中文')
    def test_HKstock_F10dividentlist_codechinese(self):
        response = zhuorui('港股', 'F10获取分红派息列表_code为中文')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取分红派息列表_只传ts')
    def test_HKstock_F10dividentlist_onlyvalts(self):
        response = zhuorui('港股', 'F10获取分红派息列表_只传ts')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取分红派息列表_只传code')
    def ttest_HKstock_F10dividentlist_onlyvalcode(self):
        response = zhuorui('港股', 'F10获取分红派息列表_只传code')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('F10获取分红派息列表_参数为空')
    def test_HKstock_F10dividentlist_bobyNone(self):
        response = zhuorui('港股', 'F10获取分红派息列表_参数为空')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

