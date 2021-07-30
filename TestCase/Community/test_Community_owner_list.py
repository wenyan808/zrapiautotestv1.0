# test_Community_owner_list
import json

import allure
import pytest

from Common.Community_common.Community_post import Communitypostdelete, Communityaddpost
from Common.get_time_stamp import get_time_stamp13
from Common.login import login
from Common.show_sql import showsql
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('个人主页-用户主贴查询')
class TestCommunitycommentowner_list():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_owner_list(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/owner_list"
        headers = {}
        headers.update(JSON)
        userId = showsql(
            '192.168.1.237', 'root', '123456', "user_account",
            "select user_id from t_user_account where `zr_no`= '68904140';"
        )
        # 拼装参数
        paylo = {

            "userId": str(list(list(userId)[0])[0]),
            "publishTime": get_time_stamp13(),
            "pageSize": 20

        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        # print(token)
        # print(type(token))
        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(60.01)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="用户主贴查询"
        )
        y = r.json()
        # print(y)
        if "data" in y:
            if len(y.get("data")) != 0:
                for i in range(len(y.get("data"))):
                    postId = y.get("data")[i].get("postId")
                    # print(postId)
                    body = {'postId': f"{postId}"}
                    # 删帖url
                    delete_url = HTTP + "/as_community/api/post/v1/delete"
                    # 删除社区发帖
                    Communitypostdelete(delete_url, headers, body)
            elif len(y.get("data")) == 0:

                # 新增url
                add_url = HTTP + "/as_community/api/post/v1/add"
                body = {
                    "articleType": "",
                    "content": "蔡徐坤“鸡你太美”指的是《只因你太美》这首歌。"
                               "\n蔡徐坤的“鸡你太美”这首的原歌曲名叫《只因你太美》，因为谐音的问题，许多网友形象的将歌名叫做了“鸡你太美”。\n"
                               "据悉，这首歌之所以会火，全凭一段蔡徐坤打球的视频，视频中蔡徐坤用篮球结合舞蹈，同时自己演唱了《只因你太美》的"
                               "一段歌曲部分，被录制成了一段视频，而这段篮球舞视频也被网友们广为乐道，火爆全网，“鸡你太美”也成了火热的梗。"
                }
                # 新增社区发帖
                a = Communityaddpost(add_url, headers, body)
                for i in range(len(a.get("data"))):
                    postId = a.get("data")[i].get("postId")
                    # print(postId)
                    body = {'postId': f"{postId}"}
                    # 删帖url
                    delete_url = HTTP + "/as_community/api/post/v1/delete"
                    # 删除社区发帖
                    Communitypostdelete(delete_url, headers, body)
            else:
                raise AssertionError(y.get("data"))
        else:
            return y
        # 断言
        assert r.status_code == 200
        assert y.get("code") == "000000"
        assert y.get("msg") == "ok"
