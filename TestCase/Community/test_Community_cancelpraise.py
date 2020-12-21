# test_Community_cancelpraise
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
@allure.feature('社区-取消点赞')
class TestCommunitycancelpraise():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_cancelpostpraise(self):
        login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = JSON

        # 拼装参数
        paylo = {
            "title": "赵立坚：这颗苦果，中方绝不会吞下！？",
            "articleType": 2,
            "content": "【环球时报-环球网报道 记者张卉】12月8日，美国宣布将对中国全国人大常委会副委员长实施所谓制裁。"
                       "在9日举行的外交部例行记者会上，有记者就中方反制措施提问。\n\n"
                       "对此，发言人赵立坚表示，我的同事昨天已经阐明了中方的立场。"
                       "针对美方的恶劣行径，中方将采取坚决有力反制，坚定捍卫自身主权安全发展利益。\n\n"
                       "我也可以告诉你的是，中方绝不会吞下损害中国主权安全发展利益的苦果，赵立坚称。"
                       "[tag:BK0500.SH][img:community/images/2020/12/02/16069047993369120.png]",
            "images": [
                {
                    "name": "community/images/2020/12/02/16069047993369120.png",
                    "w": 530,
                    "h": 295,
                    "url": "http://zhuorui-public.oss-cn-shenzhen.aliyuncs.com/"
                           "community/images/2020/12/02/16069047993369120.png"
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
        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)
        body1 = json.dumps(dict(body1))
        postId_praise_url = HTTP + "/as_community/api/praise/v1/add"
        Requests(self.session).post(
            url=postId_praise_url, headers=headers, data=body1, title="帖子点赞"
        )
        body = {'postId': f"{postId}"}
        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)
        body2 = json.dumps(dict(body1))
        cancelpraise_url = HTTP + "/as_community/api/praise/v1/cancel"
        r = Requests(self.session).post(
            url=cancelpraise_url, headers=headers, data=body2, title="取消帖子点赞"
        )
        # print(r.json())
        # 断言
        assert r.status_code == 200
        assert r.json().get("code") == "000000"
        assert r.json().get("msg") == "ok"
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

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_cancelcommentpraise(self):
        login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = JSON

        # 拼装参数
        paylo = {
            "title": "“一箭双星”发射成功！",
            "articleType": 2,
            "content": "12月10日4时14分，我国在西昌卫星发射中心用长征十一号运载火箭，以“一箭双星”方式将引力波暴高能电磁对应体全天监测器卫星送入预定轨道，发射获得圆满成功。"
                       "[tag:BK0500.SH]\n\n[img:community/images/2020/12/10/16075922499352942.JPG]\n"
                       "引力波暴高能电磁对应体全天监测器卫星由中国科学院战略性先导科技专项空间科学（二期）部署，2颗小卫星采用共轭轨道星座布局，"
                       "将对引力波伽马暴、快速射电暴高能辐射、特殊伽马暴和磁星爆发等高能天体爆发现象进行全天监测，研究中子星、黑洞等致密天体及其并合过程。\n\n"
                       "此外，卫星还将探测太阳耀斑、地球伽马闪和地球电子束等空间高能辐射现象，为进一步研究其物理机制提供科学观测数据。\n\n"
                       "这次任务是长征系列运载火箭的第355次飞行。[tag:BK0500.SH]"
                       "\n[img:community/images/2020/12/10/16075922499550225.JPG]\n"
                       "点赞，中国航天\n\n"
                       "（来源：央视军事）\n\n",
            "images": [
                {
                    "name": "community/images/2020/12/10/16075922499352942.JPG",
                    "w": 640,
                    "h": 360,
                    "url": "http://zhuorui-public.oss-cn-shenzhen.aliyuncs.com/"
                           "community/images/2020/12/10/16075922499352942.JPG"
                },
                {
                    "name": "community/images/2020/12/10/16075922499550225.JPG",
                    "w": 640,
                    "h": 418,
                    "url": "http://zhuorui-public.oss-cn-shenzhen.aliyuncs.com/"
                           "community/images/2020/12/10/16075922499550225.JPG"
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
        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)
        body1 = json.dumps(dict(body1))
        postId_praise_url = HTTP + "/as_community/api/praise/v1/add"
        Requests(self.session).post(
            url=postId_praise_url, headers=headers, data=body1, title="帖子点赞"
        )
        body = {'postId': f"{postId}"}
        body2 = {
            "content": "为中国航天点赞!",
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
        body = {'commentId': f"{commentId}"}
        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)
        body = json.dumps(dict(body1))
        # print(body)
        commentId_praise_url = HTTP + "/as_community/api/praise/v1/add"
        r = Requests(self.session).post(
            url=commentId_praise_url, headers=headers, data=body, title="评论点赞"
        )
        body = {'postId': f"{postId}"}
        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)
        body2 = json.dumps(dict(body1))
        cancelcommentpraise_url = HTTP + "/as_community/api/praise/v1/cancel"
        r = Requests(self.session).post(
            url=cancelcommentpraise_url, headers=headers, data=body2, title="取消评论点赞"
        )
        # print(r.json())
        # 断言
        assert r.status_code == 200
        assert r.json().get("code") == "000000"
        assert r.json().get("msg") == "ok"
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
