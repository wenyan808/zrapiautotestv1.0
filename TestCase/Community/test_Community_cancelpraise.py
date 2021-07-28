# test_Community_cancelpraise
"""
@File  ：test_Community_cancelpraise.py
@Author: yishouquan
@Time  : 2020/7/28
@Desc  :  app社区-取消点赞
"""
import json
import time

import allure
import pytest

import glo
from Common.Community_common.Community_post import Communitypostdelete
from Common.OSS import oss_img
from Common.login import login
from Common.show_sql import showsql
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区-取消点赞')
class TestCommunitycancelpraise():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_cancelpostpraise(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = JSON
        headers = headers

        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        paylo = {
            "title": "停火不足月以色列再袭加沙，脆弱的新政府遇大挑战！",
            "articleType": 2,
            "content": "　中新网6月17日电 综合报道，巴以达成停火协议还不满一月，以色列16日又对加沙地带的巴勒斯坦伊斯兰抵抗运动"
                       "(哈马斯)军事目标发动了空袭，这是双方自5月21日停火以来首次发生较大冲突，也是以色列新政府上台以来对哈马斯"
                       "发动的首次打击。外媒分析称，最新的空袭行动证明了停火协议的脆弱性，也是对脆弱的以色列新政府的一大挑战。\n\n"
                       "[tag:BK0500.SH]",
            "products": [
                {
                    "ts": "SH",
                    "code": "BK0500",
                    "name": "军工",
                    "type": "1"
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
        # print(y)
        postId = y.get("data").get("postId")
        # print(postId)
        body = {'postId': f"{postId}"}
        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)
        body1 = json.dumps(dict(body1))
        postId_praise_url = HTTP + "/as_community/api/praise/v1/add"
        Requests(self.session).post(
            url=postId_praise_url, headers=headers, data=body1, title="帖子点赞"
        )
        body3 = {'postId': f"{postId}"}
        sign1 = {"sign": get_sign(body3)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body3)
        body1.update(sign1)
        body2 = json.dumps(dict(body1))
        cancelpraise_url = HTTP + "/as_community/api/praise/v1/cancel"
        r = Requests(self.session).post(
            url=cancelpraise_url, headers=headers, data=body2, title="取消帖子点赞"
        )
        # print(r.json())
        # 删帖
        delete_url = HTTP + "/as_community/api/post/v1/delete"

        Communitypostdelete(delete_url, headers, body)
        # 断言
        assert r.status_code == 200
        assert r.json().get("code") == "000000"
        assert r.json().get("msg") == "ok"

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_cancelcommentpraise(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = JSON
        headers = headers
        # print(token)
        # print(type(token))
        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        userId1 = showsql(
            '192.168.1.237', 'root', '123456', "user_account",
            f"select user_id from t_user_account where `zr_no`= '68904140';"
        )
        userId = list(list(userId1)[0])[0]
        catalog = r"/Business/Img/community/"
        url1 = HTTP + "/as_common/api/sts/v1/token"
        url_path = list(oss_img("community", "01.jpg", userId, catalog, url1, headers))
        url0 = url_path[0]
        path0 = url_path[-1]
        a0 = "[img:" + path0 + "]"

        paylo = {
            "title": "关系人类永续发展的伟大事业 习近平念兹在兹",
            "articleType": 2,
            "content": "联播+ 被喻为“死亡之海”的库布其沙漠成为全球荒漠化防治典范，一度严重沙化的科尔沁草原重披绿装，"
                       "曾经的“不毛之地”毛乌素沙地筑起祖国北疆的“绿色长城”，昔日“狂风一起，黄沙漫天”的内蒙古多伦县成为"
                       "京津冀地区人们青睐的避暑胜地……我国历来高度重视荒漠化防治工作，与黄沙进行着顽强不屈的抗争，成效显著。\n\n"
                       "“人类只有一个地球家园。荒漠化防治是关系人类永续发展的伟大事业。”党的十八大以来，各地区、各部门深入"
                       "贯彻习近平生态文明思想，牢固树立绿水青山就是金山银山理念，统筹山水林田湖草沙系统治理，深入推进大规模"
                       "国土绿化行动，国土绿化事业取得新进展新成效。\n\n今年6月17日是第27个世界防治荒漠化与干旱日。"
                       "央视网《联播+》特梳理习近平总书记对荒漠化防治工作的部署，与您一同见证生命绝地上种出的“绿色奇迹”，"
                       "坚定走好荒漠化防治之路的决心。\n[tag:BK0500.SH]"
                       f"\n{a0}\n"
                       "（来源：央视网）\n\n",
            "images": [
                {
                    "name": path0,
                    "w": 700,
                    "h": 989,
                    "url": url0
                }
            ],
            "products": [
                {
                    "ts": "SH",
                    "code": "BK0500",
                    "name": "军工",
                    "type": "1"
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
        # print(y)
        postId = y.get("data").get("postId")
        # print(postId)
        body = {'postId': f"{postId}"}
        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)
        body2 = json.dumps(dict(body1))
        postId_praise_url = HTTP + "/as_community/api/praise/v1/add"
        Requests(self.session).post(
            url=postId_praise_url, headers=headers, data=body2, title="帖子点赞"
        )
        # body3 = {'postId': f"{postId}"}
        body2 = {
            "content": "金山银山就是绿水青山!",
            "products": [
                {
                    "ts": "SH",
                    "code": "600893",
                    "name": "航发动力",
                    "type": "2"
                }
            ]
        }
        body1 = {}
        body1.update(body)
        body1.update(body2)
        sign1 = {"sign": get_sign(body1)}  # 把参数签名后通过sign1传出来
        body1.update(sign1)
        body9 = json.dumps(dict(body1))
        # print(body)
        comment_url = HTTP + "/as_community/api/comment/v1/add"
        # print(comment_url)
        r = Requests(self.session).post(
            url=comment_url, headers=headers, data=body9, title="发表评论"
        )
        j = r.json()
        # print(j)
        commentId = j.get("data").get("commentId")
        body4 = {'commentId': f"{commentId}"}
        sign1 = {"sign": get_sign(body4)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body4)
        body1.update(sign1)
        body6 = json.dumps(dict(body1))
        # print(body)
        commentId_praise_url = HTTP + "/as_community/api/praise/v1/add"
        r = Requests(self.session).post(
            url=commentId_praise_url, headers=headers, data=body6, title="评论点赞"
        )
        # body5 = {'postId': f"{postId}"}
        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)
        body8 = json.dumps(dict(body1))
        cancelcommentpraise_url = HTTP + "/as_community/api/praise/v1/cancel"
        r = Requests(self.session).post(
            url=cancelcommentpraise_url, headers=headers, data=body8, title="取消评论点赞"
        )
        # print(r.json())
        # 删帖url
        delete_url = HTTP + "/as_community/api/post/v1/delete"

        # 删除社区发帖
        Communitypostdelete(delete_url, headers, body)
        # 断言
        assert r.status_code == 200
        assert r.json().get("code") == "000000"
        assert r.json().get("msg") == "ok"
