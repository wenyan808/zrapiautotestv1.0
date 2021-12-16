"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/11/26 18:16
# @Author:YiShouquan
# @File:test_US_KeyindicatorsDetail.py
"""
#   美股F10主要指标详情          /as_market/api/us/f10/v1/keyindicators/detail
import json
import logging

import allure
import pytest

from Business.Urlpath.UrlPath_userlogin import UrlPath_add_follow
from Common.getTestLoginToken import gettestLoginToken
from Common.login import login
from Common.show_sql import showsql
from Common.sign import get_sign

from Common.requests_library import Requests

from Common.tools.read_write_yaml import yamltoken

from glo import JSON, HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('美股-美股F10主要指标详情')
class TestUSKeyindicatorsDetail():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_US_KeyindicatorsDetail(self):
        # 关注用户url
        url_KeyindicatorsDetail = HTTP + "/as_market/api/us/f10/v1/keyindicators/detail"
        # 拼装headers参数
        headers = {}
        headers.update(JSON)
        token = {"token": gettestLoginToken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        # # 从数据库获取用户id
        # userId = showsql(
        #     '192.168.1.237', 'root', '123456', "user_account",
        #     "select user_id from t_user_account where `zr_no`= '10000039';"
        # )

        paylo = {
            "ts": "US", "code": "TSLA", "type": 0, "currentPage": 1, "pageSize": 12, "timestamp": 1637921540384
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r_KeyindicatorsDetail = Requests(self.session).post(
            url=url_KeyindicatorsDetail, headers=headers, data=payload, title="美股F10主要指标详情"
        )
        j = r_KeyindicatorsDetail.json()
        # print(j)
        assert r_KeyindicatorsDetail.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            # if j.get("data") == True:
            #     logging.info("是关注用户")
            #
            # else:
            #     logging.info("不是关注用户")
        except:
            raise AssertionError(
                f"\n请求地址：{url_KeyindicatorsDetail}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}"
            )
