# 字段说明：
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui


# 目前仅支持港股关键字查询股票
@allure.feature('关键字查询股票（仅用于策略组合）')
class TestClass():

    @classmethod
    def setup_class(cls) -> None:
        pass

    @allure.story('关键字查询股票（仅用于策略组合）')
    def test_hk(self):
        response = zhuorui('console', '关键字查询股票（仅用于策略组合）')
        assert_data(response, '000000', 'ok')
        # print(f"返回数据结果：{response.json()}")

    @allure.story('关键字查询股票,type为空')
    def test_hktypenull(self):
        response = zhuorui('console', '关键字查询股票,type为空')
        try:
            assert_data(response, '000000', 'ok')
        except:
            raise AssertionError(f"返回数据结果：{response.json()}")

    @allure.story('关键字查询股票,type为1')
    def test_hktype1(self):
        response = zhuorui('console', '关键字查询股票,type为1')
        assert_data(response, '000000', 'ok')
        # print(f"返回数据结果：{response.json()}")

    @allure.story('关键字查询股票,type为2')
    def test_hktype2(self):
        response = zhuorui('console', '关键字查询股票,type为2')
        assert_data(response, '000000', 'ok')
        # print(f"返回数据结果：{response.json()}")

    @allure.story('关键字查询股票,ts为空')
    def test_hktsnull(self):
        response = zhuorui('console', '关键字查询股票')
        assert_data(response, '000000', 'ok')
        # print(f"返回数据结果：{response.json()}")
