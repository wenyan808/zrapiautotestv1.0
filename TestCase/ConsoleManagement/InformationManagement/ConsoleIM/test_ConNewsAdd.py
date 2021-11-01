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


@pytest.mark.skip(reason="调试中 ")
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

        headers = {}
        headers.update(header)
        # print(token)
        # print(type(token))
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        catalog = "/Business/Img/"
        tupian_path = f'<img src="{list(oss_file("information", "zhong30省份2021年前三季度GDP.jpg", catalog, url1, headers))[-1]}"/>'

        title = "大变局下，中国经济版图的5个变化！"  # 资讯标题
        content = "中新网客户端北京10月28日电(记者 李金磊)2021年以来，在疫情、汛情等冲击之下，中国经济继续前行。" \
                  "能源价格猛涨，多地限电限产；楼市降温，多地交易腰斩……大变局之下，前三季度中国经济版图又有哪些变化？" \
                  + tupian_path

        source = "卓锐资讯转中国新闻网"  # 资讯来源
        tag = 2  # 标签(1,股票2,指数3,基金)
        code = "600111.SZ"  # 如0700.HK
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
