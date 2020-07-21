import allure
# import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason="")
@allure.feature('A股')
class TestHKstockF10profile:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('港股F10简况')
    def test_HKstock_F10profile(self):
        response = zhuorui('港股', '港股F10简况')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10简况_无token')
    def test_HKstock_F10profile_notoken(self):
        response = zhuorui('港股', '港股F10简况_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10简况_ts为空')
    def test_HKstock_F10profile_tsNone(self):
        response = zhuorui('港股', '港股F10简况_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10简况_ts为中文')
    def test_HKstock_F10profile_tschinese(self):
        response = zhuorui('港股', '港股F10简况_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10简况_code为空')
    def test_HKstock_F10profile_codeNone(self):
        response = zhuorui('港股', '港股F10简况_code为空')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10简况_code为中文')
    def test_HKstock_F10profile_codechinese(self):
        response = zhuorui('港股', '港股F10简况_code为中文')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10简况_只传ts')
    def test_HKstock_F10profile_onlyvalts(self):
        response = zhuorui('港股', '港股F10简况_只传ts')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10简况_只传code')
    def test_HKstock_F10profile_onlyvalcode(self):
        response = zhuorui('港股', '港股F10简况_只传code')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('港股F10简况_参数为空')
    def test_HKstock_F10profile_bobyNone(self):
        response = zhuorui('港股', '港股F10简况_参数为空')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

