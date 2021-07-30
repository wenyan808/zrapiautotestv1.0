# test_Community_addreport
"""
@File  ：test_Community_addreport.py
@Author: yishouquan
@Time  : 2020/7/28
@Desc  :  app社区_举报
"""
import json
import random

import allure
import pytest

from Common.login import login
from Common.show_sql import MongoDBField, showsql
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import write_json
from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区_举报')
class TestCommunityaddreport():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来
        # # 传入键key，值price，数据库名database，表名surface到MongoDB数据库
        # _paylo = MongoDBField("192.168.1.237", 27017, "community", "t_report", [{}, {"type": 1}])
        # # print(MongoDBField("192.168.1.237", 27017, "community", "t_report", [{}, {"type": 1}]))
        # # random_paylo = random.sample(_paylo, 50)
        # # paylo_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_paylo))
        # # write_json(BASE_DIR + r"/TestData/Communityaddreport.json", paylo)

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_addreport(self):
        url_hostlist = HTTP + "/as_community/api/community/v1/hot_list"
        headers = JSON
        headers = headers
        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        paylo = {}
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))
        # time.sleep(60.01)

        r = Requests(self.session).post(
            url=url_hostlist, headers=headers, data=payload, title="热门列表"
        )
        j = r.json()
        # print(j)
        # print(j.get("data")[0].get("postId"))

        url = HTTP + "/as_community/api/report/v1/add"

        paylo = {

            "reportedId": f"{j.get('data')[0].get('postId')}",
            "reportedType": 6,
            "type": 1
        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="举报(帖子)"
        )
        y = r.json()
        # print(y)
        # 断言
        assert r.status_code == 200
        try:
            assert y.get("code") == "000000"
            assert y.get("msg") == "ok"
        except:
            assert y.get("code") == "460600"
            assert y.get("msg") == "举报已提交"
        # else:
        #     raise AssertionError(y)
