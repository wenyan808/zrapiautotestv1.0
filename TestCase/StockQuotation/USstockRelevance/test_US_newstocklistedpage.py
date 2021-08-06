# test_US_newstocklistedpage

import logging
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSNewsstocklistedpage:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('新股日历分页获取已上市列表')
    def test_US_newsstocklistedpage(self):
        response = zhuorui("Allstock", "新股日历分页获取已上市列表")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "list" in (response.json().get("data"))
                for i in range(len(response.json().get("data").get("list"))):
                    assert "ts" in response.json().get("data").get("list")[i]
                    assert "code" in response.json().get("data").get("list")[i]
                    assert "type" in response.json().get("data").get("list")[i]
                    assert "name" in response.json().get("data").get("list")[i]
                    assert "listingTime" in response.json().get("data").get("list")[i]
                    assert "issuePrice" in response.json().get("data").get("list")[i]
                    if response.json().get("data").get("list")[i] == "last":
                        assert "last" in response.json().get("data").get("list")[i]
                    assert "delay" in response.json().get("data").get("list")[i]
                assert "total" in response.json().get("data")
                # assert response.json().get("data").get("pageSize") == paylo.get("pageSize")
                assert response.json().get("data").get("currentPage") == 1
            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
