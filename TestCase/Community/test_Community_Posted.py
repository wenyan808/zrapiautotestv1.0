# test_Community_Posted
import json
import time

import allure
import pytest

import glo
from Common.login import login
from Common.requests_library import Requests
from Common.show_sql import MongoDB, showsql
from Common.sign import get_sign
from Common.tools.read_write_json import get_json
from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区')
class TestCommunityPosted:
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    @allure.story('社区-发帖(短文/长文)')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_CommunityPosted.json"))
    def test_Community_Posted(self, info):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = JSON

        # 拼装参数
        paylo = info
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

        if glo.FALG == False:
            time.sleep(60.1)
        glo.FALG = False
        if info.get("articleType") == 2:
            title = "发帖(长文)"
        else:
            title = "发帖(短文)"
        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title=title
        )
        # r = requests.post(url=url, headers=headers, data=payload)
        # 断言
        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                if len(j.get("data")) != 0:
                    assert "postId" in j.get("data")
                    # print(j.get("data").get("articleType"))
                    assert j.get("data").get("articleType") == info.get("articleType")
                    if "title" in j.get("data") and info.get("articleType") == 2:
                        assert j.get("data").get("title") == info.get("title")
                    assert j.get("data").get("content") == info.get("content")
                    if "images" in j.get("data"):
                        assert type(j.get("data").get("images")) == type(info.get("images"))
                        assert j.get("data").get("images") == info.get("images")
                    assert "publishTime" in j.get("data")
                    userId = showsql(
                        '192.168.1.237', 'root', '123456', "user_account",
                        "select user_id from t_user_account where `zr_no`= '68904140';"
                    )
                    assert j.get("data").get("creator").get("userId") == userId[3:-5:]
                    assert j.get("data").get("creator").get("nickname") == glo.nickname
                    assert j.get("data").get("creator").get("headPhoto") == glo.headPhoto
                    assert j.get("data").get("creator").get("zrNo") == glo.zrNo
                    assert "praiseNum" in j.get("data")
                    assert "commentNum" in j.get("data")
                    assert "firstCommentNum" in j.get("data")
                    assert "praise" in j.get("data")
                    postId = j.get("data").get("postId")
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
        elif j.get("code") == "460301":
            raise AssertionError("请不要发布重复内容")
        elif j.get("code") == "460300":
            raise AssertionError("您发言太频繁了，请稍后再试")
        elif j.get("code") == "460404":
            raise AssertionError("内容含有敏感词，请修改后发送")
        else:
            raise AssertionError(f"{print(j.get('code'))}")
