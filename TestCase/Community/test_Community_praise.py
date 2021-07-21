# test_Community_praise
import json
import time

import allure
import pytest

import glo
from Common.Community_common.Community_post import Communitypostdelete
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
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_postpraise(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = JSON

        # 拼装参数
        paylo = {
            "title": "神舟十二号载人飞船发射圆满成功",
            "articleType": 2,
            "content": "　来源：中国新闻网\n\n中新网酒泉6月17日电(郭超凯)据中国载人航天工程办公室消息，北京时间2021年6月17日9时22分，"
                       "搭载神舟十二号载人飞船的长征二号F遥十二运载火箭，在酒泉卫星发射中心准时点火发射，约573秒后，"
                       "神舟十二号载人飞船与火箭成功分离，进入预定轨道，顺利将聂海胜、刘伯明、汤洪波3名航天员送入太空，"
                       "飞行乘组状态良好，发射取得圆满成功。这是我国载人航天工程立项实施以来的第19次飞行任务，"
                       "也是空间站阶段的首次载人飞行任务。飞船入轨后，将按照预定程序，与天和核心舱进行自主快速交会对接。"
                       "组合体飞行期间，航天员将进驻天和核心舱，完成为期3个月的在轨驻留，开展机械臂操作、出舱活动等工作，"
                       "验证航天员长期在轨驻留、再生生保等一系列关键技术。目前，天和核心舱与天舟二号的组合体运行在约390km"
                       "的近圆对接轨道，状态良好，满足与神舟十二号交会对接的任务要求和航天员进驻条件。[tag:000601.SH][tag:00031.HK]",
            "products": [{
                    "ts": "HK",
                    "code": "00031",
                    "name": "航天控股",
                    "type": "2"
                }, {
                    "ts": "SH",
                    "code": "000601",
                    "name": "航天科技",
                    "type": "2"
                }]
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
        if y.get("code") == "000000":
            postId = y.get("data").get("postId")
            # print(postId)
            body = {'postId': f"{postId}"}
            sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
            body1 = {}
            body1.update(body)
            body1.update(sign1)
            body2 = json.dumps(dict(body1))
            postId_praise_url = HTTP + "/as_community/api/praise/v1/add"
            r = Requests(self.session).post(
                url=postId_praise_url, headers=headers, data=body2, title="帖子点赞"
            )
            # print(r.json())
            # 删帖社区帖子
            delete_url = HTTP + "/as_community/api/post/v1/delete"
            # postId = y.get("data").get("postId")
            # # print(postId)
            # body = {'postId': f"{postId}"}
            Communitypostdelete(delete_url, headers, body)
            # 断言
            assert r.status_code == 200
            assert r.json().get("code") == "000000"
            assert r.json().get("msg") == "ok"

        elif y.get("code") == "460301":
            raise AssertionError("请不要发布重复内容")
        elif y.get("code") == "460300":
            raise AssertionError("您发言太频繁了，请稍后再试")
        elif y.get("code") == "460404":
            raise AssertionError("内容含有敏感词，请修改后发送")
        else:
            raise AssertionError(f"{print(y.get('code'))}")





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
        # 删帖
        delete_url = HTTP + "/as_community/api/post/v1/delete"
        postId = y.get("data").get("postId")
        # print(postId)
        body = {'postId': f"{postId}"}
        Communitypostdelete(delete_url, headers, body)
        # 断言
        assert r.status_code == 200
        assert r.json().get("code") == "000000"
        assert r.json().get("msg") == "ok"

