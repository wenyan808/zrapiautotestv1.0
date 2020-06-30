import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_xlsx_exampleshuju import shuju


@allure.feature('k线')
class TestDayKlineSHshare:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('日K查询_SH个股')
    def test_dayKline_SHshare(self):
        response = zhuorui('k线', '日K查询_SH个股')
        assert_data(response, '000000', 'ok')
        if "data" in response.json():
            # assert response.json().get("data")
            # print(response.json().get("data")[1])
            if len(response.json().get("data")) != 0:
                for info in response.json().get("data"):
                    for i in shuju('k线'):
                        if '日K查询_SH个股' in i:
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

    @allure.story('日K查询_SH个股_type类型为1指数')
    def test_dayKline_SHshare_typeOf1(self):
        response = zhuorui('k线', '日K查询_SH个股_type类型为1指数')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_type不正确')
    def test_dayKline_SHshare_typeError(self):
        response = zhuorui('k线', '日K查询_SH个股_type不正确')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_type为空')
    def test_dayKline_SHshare_typeNone(self):
        response = zhuorui('k线', '日K查询_SH个股_type为空')
        assert_data(response, '000103', 'type is not null')
        # print(response.text)

    @allure.story('日K查询_SH个股_adjType为空')
    def test_dayKline_SHshare_adjTypeNone(self):
        response = zhuorui('k线', '日K查询_SH个股_adjType为空')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.text)

    @allure.story('日K查询_SH个股_adjType类型为2前复权')
    def test_dayKline_SHshare_adjTypeOf2(self):
        response = zhuorui('k线', '日K查询_SH个股_adjType类型为2前复权')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_adjType类型为3后复权')
    def test_dayKline_SHshare_adjTypeOf3(self):
        response = zhuorui('k线', '日K查询_SH个股_adjType类型为3后复权')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_pageSize条数为1')
    def test_dayKline_SHshare_pageSizeOf1(self):
        response = zhuorui('k线', '日K查询_SH个股_pageSize条数为1')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_pageSize条数为10000')
    def test_dayKline_SHshare_pageSizeNone(self):
        response = zhuorui('k线', '日K查询_SH个股_pageSize条数为None')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_ts为空')
    def test_dayKline_SHshare_tsNone(self):
        response = zhuorui('k线', '日K查询_SH个股_ts为空')
        assert_data(response, '000103', 'ts is not null')
        # print(response.text)

    @allure.story('日K查询_SH个股_ts为string')
    def test_dayKline_SHshare_tsString(self):
        response = zhuorui('k线', '日K查询_SH个股_ts为string')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_code为空')
    def test_dayKline_SHshare_codeNone(self):
        response = zhuorui('k线', '日K查询_SH个股_code为空')
        assert_data(response, '000103', 'code is not null')
        # print(response.text)

    @allure.story('日K查询_SH个股_code异常')
    def test_dayKline_SHshare_codeException(self):
        response = zhuorui('k线', '日K查询_SH个股_code异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_code不正确')
    def test_dayKline_SHshare_codeError(self):
        response = zhuorui('k线', '日K查询_SH个股_code不正确')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_endTime')
    def test_dayKline_SHshare_endTime(self):
        response = zhuorui('k线', '日K查询_SH个股_endTime')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_startTime')
    def test_dayKline_SHshare_startTime(self):
        response = zhuorui('k线', '日K查询_SH个股_startTime')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_startTime为s')
    def test_dayKline_SHshare_startTime_s(self):
        response = zhuorui('k线', '日K查询_SH个股_startTime为s')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_startTime为ms')
    def test_dayKline_SHshare_startTime_ms(self):
        response = zhuorui('k线', '日K查询_SH个股_startTime为ms')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_endTime为s')
    def test_dayKline_SHshare_endTime_s(self):
        response = zhuorui('k线', '日K查询_SH个股_endTime为s')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_endTime为ms')
    def test_dayKline_SHshare_endTime_ms(self):
        response = zhuorui('k线', '日K查询_SH个股_endTime为ms')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_all')
    def test_dayKline_SHshare_all(self):
        response = zhuorui('k线', '日K查询_SH个股_all')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_参数为空')
    def test_dayKline_SHshare_None(self):
        response = zhuorui('k线', '日K查询_SH个股_参数为空')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.text)

    @allure.story('日K查询_SH个股_endTime为空')
    def test_dayKline_SHshare_endTimeNone(self):
        response = zhuorui('k线', '日K查询_SH个股_endTime为空')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_startTime为空')
    def test_dayKline_SHshare_startTimeNone(self):
        response = zhuorui('k线', '日K查询_SH个股_startTime为空')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH个股_只传值ts')
    def test_dayKline_SHshare_Onlyvalue_ts(self):
        response = zhuorui('k线', '日K查询_SH个股_只传值ts')
        # assert_data(response, '000000', 'ok')
        if response == None:
            # raise AttributeError
            print(response)

    @allure.story('日K查询_SH个股_只传值code')
    def test_dayKline_SHshare_Onlyvalue_code(self):
        response = zhuorui('k线', '日K查询_SH个股_只传值code')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.text)

    @allure.story('日K查询_SH个股_只传值type')
    def test_dayKline_SHshare_Onlyvalue_type(self):
        response = zhuorui('k线', '日K查询_SH个股_只传值type')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.text)

    @allure.story('日K查询_SH个股_只传值adjType')
    def test_dayKline_SHshare_Onlyvalue_adjType(self):
        response = zhuorui('k线', '日K查询_SH个股_只传值adjType')
        assert_data(response, '000103', 'type is not null')
        # print(response.text)

    @allure.story('日K查询_SH个股_只传值pageSize')
    def test_dayKline_SHshare_Onlyvalue_pageSize(self):
        response = zhuorui('k线', '日K查询_SH个股_只传值pageSize')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.text)

    @allure.story('日K查询_SH个股_只传值startTime')
    def test_dayKline_SHshare_Onlyvalue_startTime(self):
        response = zhuorui('k线', '日K查询_SH个股_只传值startTime')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.text)

    @allure.story('日K查询_SH个股_只传值endTime')
    def test_dayKline_SHshare_Onlyvalue_endTime(self):
        response = zhuorui('k线', '日K查询_SH个股_只传值endTime')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.text)

