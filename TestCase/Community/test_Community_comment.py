# test_Community_comment
"""
@File  ：test_Community_comment.py
@Author: yishouquan
@Time  : 2020/7/28
@Desc  :  app社区-发表评论
"""

import json
import time

import allure
import pytest

import glo
from Common.Community_common.Community_post import Communitypostdelete
from Common.login import login
from Common.show_sql import showsql
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON


@pytest.mark.skip(reason="调试中 ")
@allure.feature('社区-发表评论')
class TestCommunitycomment():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    def test_Community_comment(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = {}
        headers.update(JSON)


        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        paylo = {
            "title": "香港金管局与中国人民银行就人民币数字化跨境支付试点进行磋商",
            "articleType": 2,
            "content": "12月7日消息，据国外媒体报道，香港金管局总裁余伟文(Eddie Yue)上周五在一份声明中表示，"
                       "香港金管局正与中国人民银行数字货币研究所研究使用数字人民币进行跨境支付的技术测试，并作相应的技术准备。"
                       "[tag:00700.HK][tag:600519.SH]",
            "products": [
                {
                    "ts": "HK",
                    "code": "00700",
                    "name": "腾讯控股",
                    "type": "2"
                },
                {
                    "ts": "SH",
                    "code": "600519",
                    "name": "贵州茅台",
                    "type": "2"
                }
            ]
        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))
        time.sleep(60.01)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="发帖"
        )
        y = r.json()
        postId = y.get("data").get("postId")
        # print(postId)
        body = {'postId': f"{postId}"}
        body2 = {
            "content": "今天洪都航空午后拉升涨停，新余国科、安达维尔、航发动力等个股纷纷跟涨。[tag:600316.SH][tag:002311.SZ]",
            "products": [
                {
                    "ts": "SZ",
                    "code": "002311",
                    "name": "海大集团",
                    "type": "2"
                },
                {
                    "ts": "SH",
                    "code": "600316",
                    "name": "洪都航空",
                    "type": "2"
                }
            ]
        }
        body1 = {}
        body1.update(body)
        body1.update(body2)
        sign1 = {"sign": get_sign(body1)}  # 把参数签名后通过sign1传出来
        body1.update(sign1)
        body3 = json.dumps(dict(body1))
        # print(body)
        comment_url = HTTP + "/as_community/api/comment/v1/add"
        # print(comment_url)
        r = Requests(self.session).post(
            url=comment_url, headers=headers, data=body3, title="发表评论"
        )
        j = r.json()
        # print(j)
        # 删帖社区发帖
        delete_url = HTTP + "/as_community/api/post/v1/delete"
        # postId = y.get("data").get("postId")
        # print(postId)
        # body = {'postId': f"{postId}"}
        Communitypostdelete(delete_url, headers, body)
        # 断言
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                assert "postId" in j.get("data")
                assert "commentId" in j.get("data")
                assert "commentTime" in j.get("data")
                userId = showsql(
                    '192.168.1.237', 'root', '123456', "user_account",
                    "select user_id from t_user_account where `zr_no`= '68904140';"
                )
                if "fromUser" in j.get("data"):
                    if j.get("data").get("fromUser") == j.get("data").get("toUser"):
                        assert j.get("data").get("fromUser").get("userId") == j.get("data").get("toUser").get(
                            "userId") == list(list(userId)[0])[0]
                        assert j.get("data").get("fromUser").get("nickname") == j.get("data").get("toUser").get(
                            "nickname") == glo.nickname
                        assert j.get("data").get("fromUser").get("headPhoto") == j.get("data").get("toUser").get(
                            "headPhoto") == glo.headPhoto
                    else:
                        assert j.get("data").get("fromUser").get("userId") == list(list(userId)[0])[0]
                        assert j.get("data").get("fromUser").get("nickname") == glo.nickname
                        # assert j.get("data").get("fromUser").get("headPhoto") == glo.headPhoto
                        # assert j.get("data").get("toUser").get("userId")
                        # assert j.get("data").get("toUser").get("nickname")
                        # assert j.get("data").get("toUser").get("headPhoto")
                    assert j.get("data").get("content") == body2.get("content")
                    assert "products" in j.get("data")
                    assert "commentType" in j.get("data")
                    assert "praiseNum" in j.get("data")
                    assert "commentNum" in j.get("data")
