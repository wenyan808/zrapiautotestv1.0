# test_US_F10shareholder
import logging
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSF10shareholder:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取股东数据-机构持有top10-基金持有top10')
    def test_US_F10shareholder(self):
        response = zhuorui("Allstock", "获取股东数据-机构持有top10-基金持有top10")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "institutionHolders" in response.json().get("data")
                assert "fundHolders" in response.json().get("data")
                for i in range(len(response.json().get("data").get("institutionHolders"))):
                    assert "name" in response.json().get("data").get("institutionHolders")[i]
                    assert "ratio" in response.json().get("data").get("institutionHolders")[i]
                    assert "changeShare" in response.json().get("data").get("institutionHolders")[i]
                    assert "date" in response.json().get("data").get("institutionHolders")[i]
                    # print(stampToTime(response.json().get("data").get("institutionHolders")[i].get("date")))
                for i in range(len(response.json().get("data").get("fundHolders"))):
                    assert "name" in response.json().get("data").get("fundHolders")[i]
                    assert "ratio" in response.json().get("data").get("fundHolders")[i]
                    assert "changeShare" in response.json().get("data").get("fundHolders")[i]
                    assert "date" in response.json().get("data").get("fundHolders")[i]
            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
