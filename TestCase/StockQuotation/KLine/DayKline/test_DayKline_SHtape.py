import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_xlsx_exampleshuju import shuju

@pytest.mark.skip(reason='该用例不进行维护了，跳过')
@allure.feature('k线')
class TestDayKlineSHtape:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('日K查询_SH大盘_上证指数')
    def test_dayKline_SHtape_szzs(self):
        response = zhuorui('k线', '日K查询_SH大盘_上证指数')
        assert_data(response, '000000', 'ok')
        print(response.text)
        if "data" in response.json():
            # assert response.json().get("data")
            # print(response.json().get("data")[1])
            if len(response.json().get("data")) != 0:
                for info in response.json().get("data"):
                    for i in shuju('k线'):
                        if '日K查询_SH大盘_上证指数' in i:
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

    @allure.story('日K查询_SH大盘_沪股通')
    def test_dayKline_SHtape_hgt(self):
        response = zhuorui('k线', '日K查询_SH大盘_沪股通')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_type类型为2（股票）')
    def test_dayKline_SHtape_typeOf2(self):
        response = zhuorui('k线', '日K查询_SH大盘_type类型为2（股票）')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_type不正确')
    def test_dayKline_SHtape_typeError(self):
        response = zhuorui('k线', '日K查询_SH大盘_type不正确')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_type为空')
    def test_dayKline_SHtape_typeNone(self):
        response = zhuorui('k线', '日K查询_SH大盘_type为空')
        assert_data(response, '000103', 'type is not null')
        # print(response.text)

    @allure.story('日K查询_SH大盘_adjType为空')
    def test_dayKline_SHtape_adjTypeNone(self):
        response = zhuorui('k线', '日K查询_SH大盘_adjType为空')
        assert_data(response, '000103', 'adjType is empty !')
        # print(response.text)

    @allure.story('日K查询_SH大盘_adjType类型为2前复权')
    def test_dayKline_SHtape_adjTypeOf2(self):
        response = zhuorui('k线', '日K查询_SH大盘_adjType类型为2前复权')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_adjType类型为3后复权')
    def test_dayKline_SHtape_adjTypeOf3(self):
        response = zhuorui('k线', '日K查询_SH大盘_adjType类型为3后复权')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_pageSize条数为1')
    def test_dayKline_SHtape_pageSizeOf1(self):
        response = zhuorui('k线', '日K查询_SH大盘_pageSize条数为1')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_pageSize条数为10000')
    def test_dayKline_SHtape_pageSizeOf10000(self):
        response = zhuorui('k线', '日K查询_SH大盘_pageSize条数为10000')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_ts为空')
    def test_dayKline_SHtape_tsNone(self):
        response = zhuorui('k线', '日K查询_SH大盘_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('日K查询_SH大盘_ts为string')
    def test_dayKline_SHtape_tsString(self):
        response = zhuorui('k线', '日K查询_SH大盘_ts为string')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('日K查询_SH大盘_code为空')
    def test_dayKline_SHtape_codeNone(self):
        response = zhuorui('k线', '日K查询_SH大盘_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.text)

    @allure.story('日K查询_SH大盘_code异常')
    def test_dayKline_SHtape_codeException(self):
        response = zhuorui('k线', '日K查询_SH大盘_code异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_code不正确')
    def test_dayKline_SHtape_codeError(self):
        response = zhuorui('k线', '日K查询_SH大盘_code不正确')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_endTime')
    def test_dayKline_SHtape_endTime(self):
        response = zhuorui('k线', '日K查询_SH大盘_endTime')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_startTime')
    def test_dayKline_SHtape_startTime(self):
        response = zhuorui('k线', '日K查询_SH大盘_startTime')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_startTime为s')
    def test_dayKline_SHtape_startTime_s(self):
        response = zhuorui('k线', '日K查询_SH大盘_startTime为s')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_startTime为ms')
    def test_dayKline_SHtape_startTime_ms(self):
        response = zhuorui('k线', '日K查询_SH大盘_startTime为ms')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_endTime为s')
    def test_dayKline_SHtape_endTime_s(self):
        response = zhuorui('k线', '日K查询_SH大盘_endTime为s')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_endTime为ms')
    def test_dayKline_SHtape_endTime_ms(self):
        response = zhuorui('k线', '日K查询_SH大盘_endTime为ms')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_all')
    def test_dayKline_SHtape_all(self):
        response = zhuorui('k线', '日K查询_SH大盘_all')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_参数为空')
    def test_dayKline_SHtape_None(self):
        response = zhuorui('k线', '日K查询_SH大盘_参数为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('日K查询_SH大盘_endTime为空')
    def test_dayKline_SHtape_endTimeNone(self):
        response = zhuorui('k线', '日K查询_SH大盘_endTime为空')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_startTime为空')
    def test_dayKline_SHtape_startTimeNone(self):
        response = zhuorui('k线', '日K查询_SH大盘_startTime为空')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('日K查询_SH大盘_只传值ts')
    def test_dayKline_SHtape_Onlyvalue_ts(self):
        response = zhuorui('k线', '日K查询_SH大盘_只传值ts')
        # assert_data(response, '000103', 'adjType is empty !')
        # if response == None:
        # raise AttributeError
        # print(response.text)

    @allure.story('日K查询_SH大盘_只传值code')
    def test_dayKline_SHtape_Onlyvalue_code(self):
        response = zhuorui('k线', '日K查询_SH大盘_只传值code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('日K查询_SH大盘_只传值type')
    def test_dayKline_SHtape_Onlyvalue_type(self):
        response = zhuorui('k线', '日K查询_SH大盘_只传值type')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('日K查询_SH大盘_只传值adjType')
    def test_dayKline_SHtape_Onlyvalue_adjType(self):
        response = zhuorui('k线', '日K查询_SH大盘_只传值adjType')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('日K查询_SH大盘_只传值pageSize')
    def test_dayKline_SHtape_Onlyvalue_pageSize(self):
        response = zhuorui('k线', '日K查询_SH大盘_只传值pageSize')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('日K查询_SH大盘_只传值startTime')
    def test_dayKline_SHtape_Onlyvalue_startTime(self):
        response = zhuorui('k线', '日K查询_SH大盘_只传值startTime')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)

    @allure.story('日K查询_SH大盘_只传值endTime')
    def test_dayKline_SHtape_Onlyvalue_endTime(self):
        response = zhuorui('k线', '日K查询_SH大盘_只传值endTime')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.text)
