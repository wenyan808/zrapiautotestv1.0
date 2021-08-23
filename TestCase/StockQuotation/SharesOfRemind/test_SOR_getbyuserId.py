# test_SOR_getbyuserId
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

# @pytest.mark.skip(reason="调试中")
@allure.feature('股价提醒')
class TestSOGetbyuserId:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询用户设置的所有股价提醒的配置信息')
    def test_SOR_getbyuserId(self):

        response = zhuorui('Allstock', '查询用户设置的所有股价提醒的配置信息')
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                for h in range(len(response.json().get("data"))):
                    assert "ts" in response.json().get("data")[h]
                    assert "code" in response.json().get("data")[h]
                    assert "type" in response.json().get("data")[h]
                    assert "name" in response.json().get("data")[h]
                    assert "notifyRate" in response.json().get("data")[h]
                    assert "updateTime" in response.json().get("data")[h]
                    assert "list" in response.json().get("data")[h]
                    for i in range(len(response.json().get("data")[h].get("list"))):
                        assert "compareType" in response.json().get("data")[h].get("list")[i]
                        assert "threshold" in response.json().get("data")[h].get("list")[i]
                        assert "status" in response.json().get("data")[h].get("list")[i]
                    if response.json().get("data")[0].get("ts") == "SH" and response.json().get("data")[0].get("code") == "600887":
                        assert response.json().get("data")[0].get("ts") == "SH"
                        assert response.json().get("data")[0].get("code") == "600887"
                        assert response.json().get("data")[0].get("type") == 2
                        assert response.json().get("data")[0].get("name") == "伊利股份"
                        assert response.json().get("data")[0].get("notifyRate") == 3