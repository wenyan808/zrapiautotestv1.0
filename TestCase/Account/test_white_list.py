import logging

import allure
import pytest
import requests
# from api.login_api import Login
# from api.white_list_api import WhiteList
# from app import init_log, BASE_DIR
# from utils import get_script_data, assert_data


class TestWhiteList:
    def setup(self) -> None:
        self.session = requests.session()
        init_log()

    def setup_class(self) -> None:
        self.login = Login()
        self.white_list = WhiteList()

    def teardown(self) -> None:
        self.session.close()

    filename = BASE_DIR + "/data/white_list_data.json"
    data = get_script_data(filename)

    @pytest.mark.parametrize('info', data)
    @allure.severity("blocker")
    @allure.feature("开户添加白名单")
    @allure.story("开户添加白名单")
    @allure.issue("BUT地址：https://gitee.com/qtt1025/zhuorui01.git")
    @allure.testcase("用例地址：https://gitee.com/qtt1025/zhuorui01.git")
    def test_white_list(self, info):
        response_white_list = self.white_list.get_white_list(self.session, info["cardNo"])
        logging.info("开户添加白名单信息为：{}".format(response_white_list.json()))
        assert_data(response_white_list, info["code"], info["msg"])
        print(response_white_list.json())
