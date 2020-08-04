import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestNoticeAccessoryRefer:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('公告附件查询_HK')
    def test_NoticeAccessoryrefer_HK(self):
        response = zhuorui('A股', '公告附件查询_HK')
        assert_data(response, '000000', 'ok')
        # print(response.text)
        assert response.status_code == 200
        if "data" in response.json():
            # print(response.json().get("data")[0])
            # print(response.json().get("data")[1].get("code"))
            if len(response.json().get("data")) != 0:
                for info in response.json().get("data"):
                    # print(info)
                    if "title" in info:
                        assert "月報表" in response.json().get("data").get("title")
                    # assert "pubTime" in info
                    # assert "url" in info
                    # assert "relateStock" in info

    @allure.story('公告获得公告列表分页')
    def test_NoticeAccessoryRefer_list(self):
        response = zhuorui('A股', '公告获得公告列表分页')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('公告附件查询_SH')
    def test_NoticeAccessoryrefer_SH(self):
        response = zhuorui('A股', '公告附件查询_SH')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('公告附件查询_US')
    def test_NoticeAccessoryrefer_US(self):
        response = zhuorui('A股', '公告附件查询_US')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('公告附件查询_SZ')
    def test_NoticeAccessoryrefer_SZ(self):
        response = zhuorui('A股', '公告附件查询_SZ')
        assert_data(response, '000000', 'ok')
        # print(response.text)
