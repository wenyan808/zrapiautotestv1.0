# test_Community_praise
import json
import time

import allure
import pytest

import glo
from Common.login import login
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区-点赞')
class TestCommunitycommentpraise():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_postpraise(self):
        login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = JSON

        # 拼装参数
        paylo = {
            "title": "国家海洋预报台：台湾地区海域地震不会引发海啸",
            "articleType": 2,
            "content": "本文转自【中国海洋预报网】；\n\n"
                       "据国家海洋预报台10日晚消息，2020年12月10日21时19分（北京时间），"
                       "中国台湾地区海域（24.79 N,122.00 E）发生6.3级地震，震源深度为46.9千米。"
                       "自然资源部海啸预警中心根据初步地震参数判断，本次地震不会引发海啸。"
                       "[img:community/images/2020/12/11/16076533986972449.JPG]",
            "images": [
                {
                    "name": "community/images/2020/12/11/16076533986972449.JPG",
                    "w": 640,
                    "h": 417,
                    "url": "http://zhuorui-public.oss-cn-shenzhen.aliyuncs.com/"
                           "community/images/2020/12/11/16076533986972449.JPG"
                }
            ],
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
        body = json.dumps(dict(body1))
        postId_praise_url = HTTP + "/as_community/api/praise/v1/add"
        r = Requests(self.session).post(
            url=postId_praise_url, headers=headers, data=body, title="帖子点赞"
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
    def test_Community_commentpraise(self):
        login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = JSON

        # 拼装参数
        paylo = {
            "title": "欧洲央行流动性释放超预期，油价重回50美元/桶。",
            "articleType": 2,
            "content": "欧洲央行将紧急抗疫购债计划（PEPP）总体规模增加了5000亿欧元至1.85万亿欧元，"
                       "并将该计划延长了9个月至2022年3月，目的是将政府和企业的借贷成本保持在纪录低位。"
                       "欧洲央行流动性释放超预期，推动昨日油价大幅上涨，Brent、WTI盘中一度冲高至51.06、47.74美元/桶，"
                       "日内最大涨幅分别达4.25%、4.44%。Brent油价自3月6日以来重回50美元/桶。\n\n"
                       "12月11日消息，继美股石油股大涨后，港股石油股集体疯狂，"
                       "[tag:00883.HK]涨近7%，[tag:00857.HK]涨超4%，[tag:00386.HK]涨3.9%，"
                       "[tag:02883.HK]、[tag:00135.HK]纷纷跟涨。",
            "products": [
                {
                    "ts": "HK",
                    "code": "00883",
                    "name": "中国海洋石油",
                    "type": "2"
                },
                {
                    "ts": "HK",
                    "code": "00857",
                    "name": "中国石油股份",
                    "type": "2"
                },
                {
                    "ts": "HK",
                    "code": "00386",
                    "name": "中国石油化工股份",
                    "type": "2"
                },
                {
                    "ts": "HK",
                    "code": "02883",
                    "name": "中海油田服务",
                    "type": "2"
                },
                {
                    "ts": "HK",
                    "code": "00135",
                    "name": "昆仑能源",
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
        postId =y.get("data").get("postId")
        # print(postId)
        body = {'postId': f"{postId}"}
        body2 = {
            "content": "国际油价近日升势强劲，现突破50美元/桶。",
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
