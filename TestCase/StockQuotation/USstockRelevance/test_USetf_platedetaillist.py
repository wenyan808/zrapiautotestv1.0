# test_USetf_platedetaillist

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

    @allure.story('美股etf板块etf详情页')
    def test_USetf_platelist(self):
        response = zhuorui("Allstock", "美股etf板块etf详情页")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                for i in range(len(response.json().get("data"))):
                    assert "sectionTitle" in response.json().get("data")[i]
                    assert "data" in response.json().get("data")[i]
                    for h in range(len(response.json().get("data")[i].get("data"))):
                        assert "plateName" in response.json().get("data")[i].get("data")[h]
                        assert "plateDiffRate" in response.json().get("data")[i].get("data")[h]
                        assert "plateCode" in response.json().get("data")[i].get("data")[h]
                        # assert "diffRate" in response.json().get("data")[i].get("data")[h]
                        assert "delay" in response.json().get("data")[i].get("data")[h]
                        if str(response.json().get("data")[i].get("data")[h].get("delay")) == "true":
                            logging.info("实时数据")
                        else:
                            logging.info("延时数据")

            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
