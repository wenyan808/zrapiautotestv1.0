# test_USetf_platelist
import logging
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSetfplatelist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('美股etf板块首页')
    def test_USetf_platelist(self):
        response = zhuorui("Allstock", "美股etf板块首页")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                for i in range(len( response.json().get("data"))):
                    assert "ts" in response.json().get("data")[i]
                    assert "code" in response.json().get("data")[i]
                    assert "type" in response.json().get("data")[i]
                    assert "plateCode" in response.json().get("data")[i]
                    assert "name" in response.json().get("data")[i]
                    assert "plateName" in response.json().get("data")[i]
                    assert "plateDiffRate" in response.json().get("data")[i]
                    assert "name" in response.json().get("data")[i]
                    assert "diffRate" in response.json().get("data")[i]
                    assert "last" in response.json().get("data")[i]
                    assert "delay" in response.json().get("data")[i]
                    if str(response.json().get("data")[i].get("delay")) == "true":
                        logging.info("实时数据")
                    else:
                        logging.info("延时数据")
                # assert response.json().get("data").get("total") == 65
                # assert response.json().get("data").get("pageSize") == 15
                # assert response.json().get("data").get("currentPage") == 1
                # print(response.json().get("data"))

            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
