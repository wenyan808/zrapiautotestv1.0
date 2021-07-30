# test_Community_detail
import json
import time

import allure
import pytest

from Common.Community_common.Community_post import Communitypostdelete
from Common.OSS import oss_img, oss_file
from Common.getTestLoginToken import gettestLoginToken, getlogintoken
from Common.login import login

from Common.show_sql import showsql
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_yaml import yamltoken

from glo import HTTP, JSON, phone, phoneArea, pwd, headPhoto, nickname, zrNo


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
        headers1 = JSON
        header = headers1
        headers = {}
        headers.update(header)
        # token = {"token": getlogintoken(phone, pwd, phoneArea)}
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
        url_path = list(oss_img("community", "zhurong.png", userId, catalog, url1, headers))
        # url0 = list(oss_file("community", "zhurong.png", userId, catalog, url1, headers))[0]
        url0 = url_path[0]
        path = url_path[-1]
        a = "[img:" + path + "]"
        paylo = {
            "title": "嫦娥五号上升器月面点火,是我国首次地外天体起飞",
            "articleType": 2,
            "content": "6月11日，中国国家航天局公布了由祝融号火星车拍摄的着陆点全景、火星地形地貌等影像图，标志着中国首次火星探测任务取得圆满成功。"
                       "传回的影像资料中，除细节丰富的表面地貌引人注目外，着陆平台和火星车上鲜红方正的“中国印迹”背后藏有“科技密码”。\n\n"
                       "这两面五星红旗由中国航天科技集团有限公司五院510所研制。贴装在火星车表面的器表五星红旗长96毫米、宽64毫米，与嫦娥三号、四号上使用的国旗是“孪生兄弟”；"
                       "安装于着陆平台上的国旗装置长360毫米、宽240毫米，系登陆后展开。\n\n受安装位置和空间限制，着陆平台国旗装置设计了类似中国传统文化中书画画轴的展开方式，"
                       "利用形状记忆复合材料实现国旗的锁定和释放。"
                       "在着陆火星前的地面总装与测试、发射、地火转移、环火飞行以及着陆阶段，"
                       "国旗始终处于卷绕收纳状态，着陆后通过加热形状记忆复合材料释放并展开。\n\n"
                       "国旗装置驱动机构采用形状记忆复合材料，使整个国旗装置的总重量小于200克；"
                       "卷绕锁定——展开的国旗展示适用于较大尺寸的国旗，且动态展开过程栩栩如生，展示效果极佳；解锁设计采用加热缓慢展开，"
                       "形状记忆复合材料展开几乎没有振动与冲击。\n\n"
                       "(图片来源：中国航天科技集团有限公司五院510所)\n[tag:600893.SH][tag:600316.SH][tag:000601.SH][tag:00031.HK]\n"
                       f"{a}"
            ,
            "images": [{
                "name": path,
                "w": 999,
                "h": 435,
                "url": url0
            }],
            "products": [
                {
                    "ts": "SH",
                    "code": "600893",
                    "name": "航发动力",
                    "type": "2"
                },
                {
                    "ts": "SH",
                    "code": "600316",
                    "name": "洪都航空",
                    "type": "2"
                },
                {
                    "ts": "HK",
                    "code": "00031",
                    "name": "航天控股",
                    "type": "2"
                }, {
                    "ts": "SH",
                    "code": "000601",
                    "name": "航天科技",
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
        # 删帖
        delete_url = HTTP + "/as_community/api/post/v1/delete"

        Communitypostdelete(delete_url, headers, body)
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
                # if "images" in j.get("data"):
                #     assert type(j.get("data").get("images")) == type(paylo.get("images"))
                #     assert j.get("data").get("images") == paylo.get("images")
                assert "publishTime" in j.get("data")

                assert j.get("data").get("creator").get("userId") == userId
                assert j.get("data").get("creator").get("nickname") == nickname
                assert j.get("data").get("creator").get("headPhoto") == headPhoto
                assert j.get("data").get("creator").get("zrNo") == zrNo
                assert "praiseNum" in j.get("data")
                assert "commentNum" in j.get("data")
                assert "hot" in j.get("data")
                assert "shield" in j.get("data")
                assert "delete" in j.get("data")
                assert "follow" in j.get("data")
