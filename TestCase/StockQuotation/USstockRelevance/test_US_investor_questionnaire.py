"""
@File  ：test_US_investor_questionnaire.py
@Author: chenjialuo
@Time  : 2021/8/12
@Desc  :  美股非专业投资者声明签署
"""

# test_US_investor_questionnaire
import logging
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSQuestionnaire:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取是否已签署非专业投资者声明')
    def test_US_questionnaire_get(self):
        response = zhuorui('Allstock', '获取是否已签署非专业投资者声明')
        assert_data(response, '000000', 'ok')
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "sign" in response.json().get("data")
            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")
    @allure.story('提交非专业投资者声明签署内容')
    def test_US_questionnaire_add(self):
        response = zhuorui('Allstock', '提交非专业投资者声明签署内容')
        assert_data(response, '000000', 'ok')
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "result" in response.json().get("data")
            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")