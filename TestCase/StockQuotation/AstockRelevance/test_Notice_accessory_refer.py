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
        # assert_data(response, '000000', 'ok')
        print(response.text)

    @allure.story('公告获得公告列表分页')
    def test_NoticeAccessoryRefer_list(self):
        response = zhuorui('A股', '公告获得公告列表分页')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('公告附件查询_SH')
    def test_NoticeAccessoryrefer_SH(self):
        response = zhuorui('A股', '公告附件查询_SH')
        # assert_data(response, '000000', 'ok')
        print(response.text)

    @allure.story('公告附件查询_US')
    def test_NoticeAccessoryrefer_US(self):
        response = zhuorui('A股', '公告附件查询_US')
        # assert_data(response, '000000', 'ok')
        print(response.text)

    @allure.story('公告附件查询_SZ')
    def test_NoticeAccessoryrefer_SZ(self):
        response = zhuorui('A股', '公告附件查询_SZ')
        # assert_data(response, '000000', 'ok')
        print(response.text)

