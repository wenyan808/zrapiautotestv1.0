# test_Community_commentlist
"""
@File  ：test_Community_commentlist.py
@Author: yishouquan
@Time  : 2020/7/28
@Desc  :  app社区-查询帖子的评论
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
@allure.feature('社区-查询帖子的评论')
class TestCommunitycommentlist():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    def test_Community_commentlist(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = {}
        headers.update(JSON)



        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        paylo = {
            "title": "全球上市公司市值TOP10，科技股占了9家",
            "articleType": 2,
            "content": "美股周一（12月7日），特斯拉大涨7.13%，股价再创新高，市值突破6000亿美元；"
                       "台积电涨2.56%，股价再创新高，市值突破5500亿美元。台积电市值首次超过伯克希尔。"
                       "截至周一收盘，全球上市公司市值TOP10，科技股占了9家。[tag:00700.HK][tag:09988.HK]",
            "products": [
                {
                    "ts": "Hk",
                    "code": "00700",
                    "name": "腾讯控股",
                    "type": "2"
                },
                {
                    "ts": "HK",
                    "code": "09988",
                    "name": "阿里巴巴-SW",
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

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="发帖"
        )
        y = r.json()
        if y.get("code") == "000000":
            postId = y.get("data").get("postId")
            # print(postId)
            body4 = {'postId': f"{postId}"}
            body2 = {
                "content": " 未来是科技的世界，直接买买买[tag:00700.HK][tag:09988.HK]",
                "products": [
                    {
                        "ts": "Hk",
                        "code": "00700",
                        "name": "腾讯控股",
                        "type": "2"
                    },
                    {
                        "ts": "HK",
                        "code": "09988",
                        "name": "阿里巴巴-SW",
                        "type": "2"
                    }
                ]
            }
            body1 = {}
            body1.update(body4)
            body1.update(body2)
            sign1 = {"sign": get_sign(body1)}  # 把参数签名后通过sign1传出来
            body1.update(sign1)
            body = json.dumps(dict(body1))
            # print(body)
            comment_url = HTTP + "/as_community/api/comment/v1/add"
            # print(comment_url)
            r = Requests(self.session).post(
                url=comment_url, headers=headers, data=body, title="发表评论"
            )
            j = r.json()
            # print(j)
            commentId = j.get("data").get("commentId")
            # body5 = {'postId': f"{postId}"}
            body1 = {}
            body1.update(body4)
            sign1 = {"sign": get_sign(body1)}
            body1.update(sign1)
            body6 = json.dumps(dict(body1))
            commentlist_url = HTTP + "/as_community/api/comment/v1/list"
            r = Requests(self.session).post(
                url=commentlist_url, headers=headers, data=body6, title="查询帖子的评论"
            )
            h = r.json()
            # print(h)
            # 删帖社区帖子
            delete_url = HTTP + "/as_community/api/post/v1/delete"
            # postId = y.get("data").get("postId")
            # print(postId)
            # body = {'postId': f"{postId}"}
            Communitypostdelete(delete_url, headers, body4)
            # # 断言
            assert r.status_code == 200
            assert h.get("code") == "000000"
            assert h.get("msg") == "ok"
            if "data" in h:
                if len(h.get("data")) != 0:
                    assert h.get("data")[0].get("commentId") == commentId
                    assert "commentId" in h.get("data")[0]
                    assert "commentTime" in h.get("data")[0]
                    userId = showsql(
                        '192.168.1.237', 'root', '123456', "user_account",
                        "select user_id from t_user_account where `zr_no`= '68904140';"
                    )
                    if "fromUser" in h.get("data")[0]:
                        assert h.get("data")[0].get("fromUser").get("userId") == list(list(userId)[0])[0]
                        assert h.get("data")[0].get("fromUser").get("nickname") == glo.nickname
                        # assert h.get("data")[0].get("fromUser").get("headPhoto") == glo.headPhoto
                        # assert h.get("data")[0].get("fromUser").get("zrNo") == glo.zrNo
                    assert h.get("data")[0].get("content") == body2.get("content")
                    assert "products" in h.get("data")[0]
                    for i in range(len(h.get("data")[0].get("products"))):
                        assert "ts" in h.get("data")[0].get("products")[i]
                        assert "code" in h.get("data")[0].get("products")[i]
                        assert "name" in h.get("data")[0].get("products")[i]
                        assert "type" in h.get("data")[0].get("products")[i]
                    # assert "praise" in h.get("data")[0]
                    assert "praiseNum" in h.get("data")[0]
                    assert "commentNum" in h.get("data")[0]

        elif y.get("code") == "460301":
            raise AssertionError("请不要发布重复内容")
        elif y.get("code") == "460300":
            raise AssertionError("您发言太频繁了，请稍后再试")
        elif y.get("code") == "460404":
            raise AssertionError("内容含有敏感词，请修改后发送")