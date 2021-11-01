# test_Community_commentmore_list
import json
import logging
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
@allure.feature('社区-查询一级评论下的更多评论')
class TestCommunitycommentmore_list():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    def test_Community_commentmore_list(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = {}
        headers.update(JSON)

        # 拼装参数
        paylo = {
            "title": "腾讯是全球第一线上游戏企业，重申目标价655港元",
            "articleType": 2,
            "content": "12月8日消息，摩根大通发表的研究报告指，[tag:00700.HK]是全球收入规模第一的线上游戏企业，估计公司游戏业务有强劲增长潜力，"
                       "相信海外市场属「蓝海市场」，公司可进一步抢占市场份额。现有游戏在变现方面仍有提升空间，例如《PUBG Mobile》、《英雄联盟手游版》等。"
                       "而在内地市场，公司有庞大的用户基础，相信随着游戏品种扩张亦有变现的上行空间，预计用户会由低ARPU的小游戏转向高ARPU的游戏，相信将带动"
                       "平台整体ARPU提升。\n\n在海外业务方面，该行估计腾讯在未来数年将继续扩张，而公司透过自家培育及股权投资等成功建立世界级的游戏开发能力，"
                       "估计来自五至六款国际游戏的单季收入占整体收入25%，或手游收入的30-35%，并预计海外占比到2023年将升至40-50%。在本地市场方面，"
                       "该行指出公司在内地市占约五成，渗透不同类型的游戏，不过在变现比例较高的游戏中腾讯市占率则少于两成，反映公司有潜力发掘机遇提升平台ARPU。\n\n"
                       "该行维持对腾讯「增持」评级，目标价655港元。截至发稿，腾讯涨0.6%，报587港元，总市值5.6万亿港元。[tag:00700.HK]",
            "products": [
                {
                    "ts": "HK",
                    "code": "00700",
                    "name": "腾讯控股",
                    "type": "2"
                }
            ]
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
            url=url, headers=headers, data=payload, title="发帖"
        )
        y = r.json()
        # print(y)
        postId = y.get("data").get("postId")
        # print(postId)
        body4 = {'postId': f"{postId}"}
        body2 = {
            "content": " [tag:00700.HK]买入[tag:09988.HK]买入",
            "products": [
                {
                    "ts": "HK",
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
        body3 = {
            'postId': f"{postId}",
            "commentId": f"{commentId}",
            "content": " [tag:00700.HK]已买入1手[tag:09988.HK]已买入1手",
            "products": [
                {
                    "ts": "HK",
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
        body1.update(body3)
        sign1 = {"sign": get_sign(body1)}
        body1.update(sign1)
        body5 = json.dumps(dict(body1))
        commentadd_url = HTTP + "/as_community/api/comment/v1/add"
        r = Requests(self.session).post(
            url=commentadd_url, headers=headers, data=body5, title="发表评论的评论"
        )
        h = r.json()
        # print(h)
        body6 = {'commentId': f"{commentId}"}
        body1 = {}
        body1.update(body6)
        sign1 = {"sign": get_sign(body1)}
        body1.update(sign1)
        body7 = json.dumps(dict(body1))
        commentmore_list_url = HTTP + "/as_community/api/comment/v1/more_list"
        r = Requests(self.session).post(
            url=commentmore_list_url, headers=headers, data=body7, title="查询一级评论下的更多评论"
        )
        k = r.json()
        # print(k)
        # 删帖社区帖子
        delete_url = HTTP + "/as_community/api/post/v1/delete"
        # postId = y.get("data").get("postId")
        # print(postId)
        # body8 = {'postId': f"{postId}"}
        Communitypostdelete(delete_url, headers, body4)
        # # 断言
        assert r.status_code == 200
        assert h.get("code") == "000000"
        assert h.get("msg") == "ok"
        if "data" in k:
            if len(k.get("data")) != 0:
                assert "commentId" in k.get("data")[0]
                assert "commentId" in k.get("data")[0]
                assert "commentTime" in k.get("data")[0]
                userId = showsql(
                    '192.168.1.237', 'root', '123456', "user_account",
                    "select user_id from t_user_account where `zr_no`= '68904140';"
                )
                if k.get("data")[0].get("fromUser") == k.get("data")[0].get("toUser"):
                    assert k.get("data")[0].get("fromUser").get("userId") == k.get("data")[0].get("toUser").get(
                        "userId") == list(list(userId)[0])[0]
                    assert k.get("data")[0].get("fromUser").get("nickname") == k.get("data")[0].get("toUser").get(
                        "nickname") == glo.nickname
                    # assert k.get("data")[0].get("fromUser").get("headPhoto") == k.get("data")[0].get("toUser").get(
                    #     "headPhoto") == glo.headPhoto
                    # assert k.get("data")[0].get("fromUser").get("zrNo") == glo.zrNo
                else:
                    logging.info("不是自已评论自己（fromUser和toUser不一致）")
                assert k.get("data")[0].get("content") == body3.get("content")
                assert "products" in k.get("data")[0]
                for i in range(len(k.get("data")[0].get("products"))):
                    assert "ts" in k.get("data")[0].get("products")[i]
                    assert "code" in k.get("data")[0].get("products")[i]
                    assert "name" in k.get("data")[0].get("products")[i]
                    assert "type" in k.get("data")[0].get("products")[i]
                assert "praise" in k.get("data")[0]
                assert "commentType" in k.get("data")[0]
                assert "praiseNum" in k.get("data")[0]
