import os
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
import pytest

@allure.feature('开户')
class TestOpen:

    @classmethod
    def setup_class(cls):
        login()

    @allure.story("获取开户信息")
    def test_open_info(self):
        response = zhuorui("开户", "获取开户信息")
        assert_data(response, "000000", "ok")
        # print(response.json())

    @allure.story("身份证正面OCR")
    def test_card_front(self):
        response = zhuorui("开户", "身份证正面OCR")
        # print(response.json())
        if response.json().get('code') == "000000":
            assert_data(response, "000000", "ok")
        else:
            assert_data(response, "000301", "今日上传次数已到达上限")

    @allure.story("身份证背面OCR")
    def test_card_back(self):
        response = zhuorui("开户", "身份证背面OCR")
        # print(response.json())
        if response.json().get("code") == '000000':
            assert_data(response, "000000", "ok")
        else:
            assert_data(response, "000301", "今日上传次数已到达上限")

    @allure.story("银行卡OCR")
    def test_bank_ocr(self):
        response = zhuorui("开户", "银行卡OCR")
        # print(response.json())
        if response.json().get("code") == "000000":
            assert_data(response, "000000", "ok")
        else:
            assert_data(response, "000301", "今日银行卡上传次数已达到上限")


    @allure.story("资料和OCR识别是否一致")
    def test_identity_valid(self):
        response = zhuorui("开户", "资料和OCR识别是否一致")
        assert_data(response, "020011", "资料和OCR识别不一致")

    @allure.story("上传身份信息")
    def test_identity(self):
        response = zhuorui("开户", "上传身份信息")
        if response.json().get("code") == "000000":
            assert_data(response, "000000", "ok")
        else:
            assert_data(response, "000301", "今日上传次数已到达上限")
        # print(response.json())


    @allure.story("获取数字验证码")
    def test_get_live_code(self):
        response = zhuorui("开户", "获取数字验证码")
        assert_data(response, "000000", "ok")
        # print(response.json())

    @allure.story("活体人脸核身")
    def test_live_recognition(self):
        response = zhuorui("开户", "活体人脸核身")
        if response.json().get("code") == "000000":
            assert_data(response, "000000", "ok")
        else:
            assert_data(response, "000301", "今日上传次数已到达上限")
        # print(response.json())

    @allure.story("上传工作资料")
    def test_work_info(self):
        response = zhuorui("开户", "上传工作资料")
        assert_data(response, "000000", "ok")
    #
    @allure.story("风险测评")
    def test_risk_assessment(self):
        response = zhuorui("开户", "风险测评")
        assert_data(response, "000000", "ok")
        # print(response.json())

    @allure.story("其它资料披露")
    def test_other_info_disclosure(self):
        response = zhuorui("开户", "其它资料披露")
        assert_data(response, "000000", "ok")
    #
    @allure.story("选择开通账户")
    def test_other_select_open_account(self):
        response = zhuorui("开户", "选择开通账户")
        assert_data(response, "000000", "ok")
        # print(response.json())

    @allure.story("风险披露语音")
    def test_other_risk_disclosure_voice(self):
        response = zhuorui("开户", "风险披露语音")
        assert_data(response, "000000", "ok")
        # print(response.json())


    @allure.story("风险披露")
    def test_other_risk_disclosure(self):
        response = zhuorui("开户", "风险披露")
        assert_data(response, "000000", "ok")
        # print(response.json())

    @allure.story("上传电子签名")
    def test_other_signature(self):
        response = zhuorui("开户", "上传电子签名")
        # print(response.json())
        assert_data(response, "000000", "ok")


# if __name__ == '__main__':
    # os.system('pytest --aluredir = ./report/xml')
    # os.system('allure generate ./report/xml -o ./report/html --clean')





