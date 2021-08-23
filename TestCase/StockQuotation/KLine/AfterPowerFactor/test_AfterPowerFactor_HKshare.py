import json

import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
# from Common.show_sql import OperationSql, MongoDB
from Common.requests_library import Requests
from Common.sign import get_sign
from Common.tools.read_write_json import get_json
from Common.tools.read_write_yaml import yamltoken
from glo import JSON, HTTP, BASE_DIR


@allure.feature('k线')
class TestAfterPowerFactor:
    @classmethod
    def setup_class(cls) -> None:
        login()
        # q = OperationSql("192.168.1.237", "root", "123456", "t_stock_search")
        # ts_code = q.show_sql("select ts,code from t_stock_search;")
        # for n in ts_code:
        #     # print(n)
        #     # id = MongoDB("ts_code", ts_code)
        #     # print(ts_code)
        #     # print(ts_code[0])
        #     # print(ts_code[0][0],ts_code[0][1])
        #     cls._djson = {"ts": str(ts_code[n][0]), "code": str(ts_code[n][1])}

    # @pytest.mark.parametrize("_data", get_json(BASE_DIR + r"/TestData/t_stock_search.json"))
    @allure.story('查询最新复权因子_HK个股')
    def test_AfterPowerFactor_HKshare(self):

        response = zhuorui('k线', '查询最新复权因子_HK个股')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('查询最新复权因子_HK个股_ts为空')
    def test_AfterPowerFactor_HKshare_tsNone(self):
        response = zhuorui('k线', '查询最新复权因子_HK个股_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK个股_ts为中文')
    def test_AfterPowerFactor_HKshare_tschinese(self):
        response = zhuorui('k线', '查询最新复权因子_HK个股_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('查询最新复权因子_HK个股_只传ts')
    def test_AfterPowerFactor_HKshare_onlyvalts(self):
        response = zhuorui('k线', '查询最新复权因子_HK个股_只传ts')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK个股_code为空')
    def test_AfterPowerFactor_HKshare_codeNone(self):
        response = zhuorui('k线', '查询最新复权因子_HK个股_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK个股_code为中文')
    def test_AfterPowerFactor_HKshare_codechinese(self):
        response = zhuorui('k线', '查询最新复权因子_HK个股_code为中文')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK个股_只传code')
    def test_AfterPowerFactor_HKshare_onlyvalcode(self):
        response = zhuorui('k线', '查询最新复权因子_HK个股_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK个股_无token')
    def test_AfterPowerFactor_HKshare_notoken(self):
        response = zhuorui('k线', '查询最新复权因子_HK个股_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.status_code)
        # print(response.json())
