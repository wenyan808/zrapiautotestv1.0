# test_Community_commentdetail
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
from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区-查看评论详情')
class TestCommunitycommentdetail():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    def test_Community_commentdetail(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = JSON

        # 拼装参数
        paylo = {
            "title": "38万公里之外的亲密“牵手”",
            "articleType": 2,
            "content": "12月6日凌晨，嫦娥五号上升器成功与轨道器和返回器组合体交会对接，并将样品容器安全转移至返回器中。"
                       "这是我国首次实现月球轨道交会对接，也是人类首次在月球轨道进行无人交会对接。按计划，嫦娥五号将于12月中下旬返回地球。"
                       "[tag:00700.HK][tag:600519.SH]",
            "products": [
                {
                    "ts": "Hk",
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
        headers = headers
        # print(token)
        # print(type(token))
        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = json.dumps(dict(payload1))
        time.sleep(60.01)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="发帖"
        )
        y = r.json()
        # print(y)
        postId = y.get("data").get("postId")
        # print(postId)
        body = {'postId': f"{postId}"}
        body2 = {
            "content": " 弘扬中国航天精神，为强大祖国点赞[tag:600316.SH][tag:603698.SH]",
            "products": [
                {
                    "ts": "SH",
                    "code": "603698",
                    "name": "航天工程",
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
        commentId = j.get("data").get("commentId")
        body4 = {'commentId': f"{commentId}"}
        body1 = {}
        body1.update(body4)
        sign1 = {"sign": get_sign(body1)}
        body1.update(sign1)
        body5 = json.dumps(dict(body1))
        commentdetail_url = HTTP + "/as_community/api/comment/v1/detail"
        r = Requests(self.session).post(
            url=commentdetail_url, headers=headers, data=body5, title="查看评论详情"
        )
        h = r.json()
        # print(h)
        # 删帖社区发帖
        delete_url = HTTP + "/as_community/api/post/v1/delete"
        # postId = y.get("data").get("postId")
        # print(postId)
        # body = {'postId': f"{postId}"}
        Communitypostdelete(delete_url, headers, body)
        # # 断言
        assert r.status_code == 200
        assert h.get("code") == "000000"
        assert h.get("msg") == "ok"
        if "data" in h:
            if len(j.get("data")) != 0:
                assert "postId" in h.get("data")
                assert "commentId" in h.get("data")
                assert "commentTime" in h.get("data")
                userId = showsql(
                    '192.168.1.237', 'root', '123456', "user_account",
                    "select user_id from t_user_account where `zr_no`= '68904140';"
                )
                if "fromUser" in h.get("data"):
                    assert h.get("data").get("fromUser").get("userId") == list(list(userId)[0])[0]
                    assert h.get("data").get("fromUser").get("nickname") == glo.nickname
                    # assert h.get("data").get("fromUser").get("headPhoto") == glo.headPhoto
                    assert h.get("data").get("fromUser").get("zrNo") == glo.zrNo
                assert h.get("data").get("content") == body2.get("content")
                assert "products" in h.get("data")
                assert type(h.get("data").get("products")) == type(body2.get("products"))
                assert "commentType" in h.get("data")
                assert "praiseNum" in h.get("data")
                assert "commentNum" in h.get("data")
