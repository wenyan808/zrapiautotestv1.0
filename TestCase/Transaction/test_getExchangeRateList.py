import logging

import allure
import pytest
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_getExchangeRateList

# @pytest.mark.skip(reason="调试中")
from TestAssertions.test_exchange_rate.test_assertions_exchangerate import resultschema


class TestgetExchangeRateList:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('行情汇率列表')
    def test_getExchangeRateList(self):
        response = zhuorui('交易', '行情汇率列表')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                for i in range(len(response.json().get("data"))):
                    assert "moneyType" in response.json().get("data")[i]
                    assert "rate" in response.json().get("data")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

        schema = response.json()
        try:
            validate(instance=resultschema, schema=schema, format_checker=draft7_format_checker)
        except SchemaError as e:
            return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
        except ValidationError as e:
            return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
        else:
            return 0, "success!"
