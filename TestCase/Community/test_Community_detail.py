# test_Community_detail
import json
import time


import allure
import pytest

import glo
from Common.login import login
from Common.show_sql import OperationSql
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区-获取帖子详情')
class TestCommunitydetail():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    def test_Community_detail(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = JSON

        # 拼装参数
        paylo = {
            "title": "嫦娥五号上升器月面点火,是我国首次地外天体起飞",
            "articleType": 2,
            "content": "从国家航天局获悉，12月3日23时10分，嫦娥五号上升器月面点火，3000牛发动机工作约6分钟后，"
                       "顺利将携带月壤的上升器送入到预定环月轨道，成功实现我国首次地外天体起飞。[tag:00700.HK][tag:600519.SH]"
                       "[img:community/images/2020/12/04/16070706185435230.png]",
            "images": [{
                "name": "community/images/2020/12/04/16070706185435230.png",
                "w": 1000,
                "h": 563,
                "url": "http://zhuorui-public.oss-cn-shenzhen.aliyuncs.com/community/images/2020/12/04/16070706185435230.png"
            }],
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
        time.sleep(60.1)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="发帖"
        )
        y = r.json()
        # print(y)
        postId = y.get("data").get("postId")
        # print(postId)
        body = {'postId': f"{postId}"}
        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)
        # print(body1)
        detail_url = HTTP + "/as_community/api/post/v1/detail"

        r = Requests(self.session).post(
            url=detail_url, headers=headers, json=body1, title="获取帖子详情"
        )
        j = r.json()
        # print(j)
        # 断言
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                assert "postId" in j.get("data")
                # print(j.get("data").get("articleType"))
                assert j.get("data").get("articleType") == paylo.get("articleType")
                if "title" in j.get("data") and paylo.get("articleType") == 2:
                    assert j.get("data").get("title") == paylo.get("title")
                assert j.get("data").get("content") == paylo.get("content")
                if "images" in j.get("data"):
                    assert type(j.get("data").get("images")) == type(paylo.get("images"))
                    assert j.get("data").get("images") == paylo.get("images")
                assert "publishTime" in j.get("data")
                q = OperationSql("192.168.1.237", "root", "123456", "user_account")
                userId = str(q.show_sql("select id from t_user_account where `zr_no`= '68904140';"))
                assert j.get("data").get("creator").get("userId") == userId[3:-5:]
                assert j.get("data").get("creator").get("nickname") == glo.nickname
                assert j.get("data").get("creator").get("headPhoto") == glo.headPhoto
                assert j.get("data").get("creator").get("zrNo") == glo.zrNo
                assert "praiseNum" in j.get("data")
                assert "commentNum" in j.get("data")
                assert "hot" in j.get("data")
                assert "shield" in j.get("data")
                assert "delete" in j.get("data")
                assert "follow" in j.get("data")
                postId = y.get("data").get("postId")
                # print(postId)
                body = {'postId': f"{postId}"}
                sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
                body1 = {}
                body1.update(body)
                body1.update(sign1)
                # print(body1)
                delete_url = HTTP + "/as_community/api/post/v1/delete"

                r = Requests(self.session).post(
                    url=delete_url, headers=headers, json=body1, title="删帖"
                )
                j = r.json()
                # print(j)
                # 断言
                assert r.status_code == 200
                assert j.get("code") == "000000"
                assert j.get("msg") == "ok"
