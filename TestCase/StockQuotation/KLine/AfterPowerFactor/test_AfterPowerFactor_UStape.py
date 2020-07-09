import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestAfterPowerFactor:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询最新复权因子_US大盘_DIA')
    def test_AfterPowerFactor_UStape_HSCCI(self):
        response = zhuorui('k线', '查询最新复权因子_US大盘_DIA')
        assert_data(response, '000000', 'ok')
        assert response.json().get("data") == 1
        # print(response.json())

    @allure.story('查询最新复权因子_US大盘_QQQ')
    def test_AfterPowerFactor_UStape_QQQ(self):
        response = zhuorui('k线', '查询最新复权因子_US大盘_QQQ')
        assert_data(response, '000000', 'ok')
        assert response.json().get("data") == 1
        # print(response.json())

    @allure.story('查询最新复权因子_US大盘_SPY')
    def test_AfterPowerFactor_UStape_SPY(self):
        response = zhuorui('k线', '查询最新复权因子_US大盘_SPY')
        assert_data(response, '000000', 'ok')
        assert response.json().get("data") == 1
        # print(response.json())

    @allure.story('查询最新复权因子_US大盘_ts为空')
    def test_AfterPowerFactor_UStape_tsNone(self):
        response = zhuorui('k线', '查询最新复权因子_US大盘_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_US大盘_ts为中文')
    def test_AfterPowerFactor_UStape_tschinese(self):
        response = zhuorui('k线', '查询最新复权因子_US大盘_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_US大盘_只传ts')
    def test_AfterPowerFactor_UStape_onlyvalts(self):
        response = zhuorui('k线', '查询最新复权因子_US大盘_只传ts')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_US大盘_code为空')
    def test_AfterPowerFactor_UStape_codeNone(self):
        response = zhuorui('k线', '查询最新复权因子_US大盘_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_US大盘_code为中文')
    def test_AfterPowerFactor_UStape_codechinese(self):
        response = zhuorui('k线', '查询最新复权因子_US大盘_code为中文')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_US大盘_只传code')
    def test_AfterPowerFactor_UStape_onlyvalcode(self):
        response = zhuorui('k线', '查询最新复权因子_US大盘_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_US大盘_无token')
    def test_AfterPowerFactor_UStape_notoken(self):
        response = zhuorui('k线', '查询最新复权因子_US大盘_无token')
        assert_data(response, '000000', 'ok')
        assert response.json().get("data") == 1
        # print(response.json())