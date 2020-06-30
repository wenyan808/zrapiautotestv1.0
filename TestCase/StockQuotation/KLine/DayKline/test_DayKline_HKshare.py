import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_xlsx_exampleshuju import shuju


@allure.feature('k线')
class TestDayKlineHKshare:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('日K查询_HK个股')
    def test_dayKline_HKshare(self):
        response = zhuorui('k线', '日K查询_HK个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)
        if "data" in response.json():
            # assert response.json().get("data")
            # print(response.json().get("data")[1])
            if len(response.json().get("data")) != 0:
                for info in response.json().get("data"):
                    for i in shuju('k线'):
                        if '日K查询_HK个股' in i:
                            calculate1 = i[9]
                            calculate = eval(calculate1)
                            # print(calculate)
                            # print(calculate.get("type"))
                            assert info.get("ts") == calculate.get("ts")
                            # print(calculate.get("ts"))
                            assert info.get("code") == calculate.get("code")
                            assert info.get("type") == int(calculate.get("type"))
                            assert info.get("adjType") == calculate.get("adjType")
                            # print(info)
                            # print(info.get("adj"))
                            adj = info.get("adj")
                            if adj != None:
                                assert info.get("adj") == calculate.get("adj")
                            # else:
                            #     raise NameError
            elif len(response.json().get("data")) == 0:
                print("data无数据")
            else:

                raise TypeError