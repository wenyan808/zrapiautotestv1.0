# test_ConNewsAdd      新建修改资讯信息      /api/con_news/v1/add
import json
import logging
import random

import allure
import pytest

from Common.ConTopic_common.Deletes import delete_AddConNews, list_connews
from Common.OSS import oss_file
from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯console_新建修改资讯信息')
class TestIMConNewsAdd():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    # @pytest.mark.parametrize('info',
    #                          get_json(BASE_DIR + r"/TestData/testIMData/test_IM_conNewsList.json"))
    def test_IM_conNewsAdd(self):
        url = console_HTTP + "/api/con_news/v1/add"
        url1 = console_HTTP + "/api/con_sts/v1/token"
        header = console_JSON
        header = header
        headers = {}
        headers.update(header)
        # print(token)
        # print(type(token))
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        catalog = "/Business/Img/"
        tupian_path = f'<img src="{list(oss_file("information", "buffett01.png", catalog, url1, headers))[-1]}"/>'

        title = "2021年巴菲特股东大会直播！"  # 资讯标题
        content = "众所周知，「股神」巴菲特每年都会为伯克希尔的股东们撰写「致股东的一封信」，这些信件被投资者们称为「投资教科书」。" \
                  "而每年伯克希尔的股东大会，在投资者心目中则是堪比「投资圈春晚」。\n\n由于疫情的影响，今年伯克希尔的股东大会将再次进行线上直播。" \
                  "\n\n对此，巴菲特表示，他与查理·芒格都十分开心：得益于线上直播，世界各地的人都可以看到这场股东大会。" \
                  + tupian_path

        source = "卓锐资讯moomoo自动化测试"  # 资讯来源
        tag = 2  # 标签(1,股票2,指数3,基金)
        code = "002594.SZ"  # 如0700.HK
        topicIds = 21  # 所属专题id(1,2,3)逗号分割
        isHot = 1  # 是否热门(1-是 0-否)
        types = [0]  # 资讯类型（0,要闻,1港股,2,美股,3快讯,4专题,5异动,6新股,7AI看盘,8新闻,9公告,10评级,11宏观,12推送,13其他）
        themeImg = list(oss_file("information", "buffett02.png", catalog, url1, headers))[-1]  # 主题封面图url
        subTypes = [4]  # 快讯类型下使用(子类型):1, "异动",2, "港股",3, "美股",4, "A股"
        important = 0  # 是否重要资讯(0,重要 1,非重要)
        # id = ""  # 增不带id 修改带id
        paylo = {
            "title": title,
            "content": content,
            "source": source,
            "codesTag": [
                {
                    "tag": tag,
                    "code": code
                }
            ],
            "topicIds": topicIds,
            "isHot": isHot,
            "types": types,
            "themeImg": themeImg,
            "subTypes": subTypes,
            # "id": id,
            "important": important
        }
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="新建修改资讯信息"
        )

        j = r.json()
        # print(j)
        # 通过资讯标题获取资讯列表并删除新增资讯
        delete_AddConNews(list_connews(title))
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        assert j.get("data") == True
