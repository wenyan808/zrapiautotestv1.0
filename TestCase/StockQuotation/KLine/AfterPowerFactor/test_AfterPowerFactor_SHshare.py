import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestAfterPowerFactor:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询最新复权因子_SH个股')
    def test_AfterPowerFactor_SHshare(self):
        response = zhuorui('k线', '查询最新复权因子_SH个股')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('查询最新复权因子_SH个股_ts为空')
    def test_AfterPowerFactor_SHshare_tsNone(self):
        response = zhuorui('k线', '查询最新复权因子_SH个股_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_SH个股_ts为中文')
    def test_AfterPowerFactor_SHshare_tschinese(self):
        response = zhuorui('k线', '查询最新复权因子_SH个股_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('查询最新复权因子_SH个股_只传ts')
    def test_AfterPowerFactor_SHshare_onlyvalts(self):
        response = zhuorui('k线', '查询最新复权因子_SH个股_只传ts')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_SH个股_code为空')
    def test_AfterPowerFactor_SHshare_codeNone(self):
        response = zhuorui('k线', '查询最新复权因子_SH个股_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_SH个股_code为中文')
    def test_AfterPowerFactor_SHshare_codechinese(self):
        response = zhuorui('k线', '查询最新复权因子_SH个股_code为中文')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_SH个股_只传code')
    def test_AfterPowerFactor_SHshare_onlyvalcode(self):
        response = zhuorui('k线', '查询最新复权因子_SH个股_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_SH个股_无token')
    def test_AfterPowerFactor_SHshare_notoken(self):
        response = zhuorui('k线', '查询最新复权因子_SH个股_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.status_code)
        # print(response.json())
