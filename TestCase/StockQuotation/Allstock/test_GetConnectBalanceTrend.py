# test_GetConnectBalanceTrend
import allure
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason="调试中")
@allure.feature('公共分类')
class TestNowSrverinfo:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询当天的北向最新资金流动趋势')
    def test_nowSrverinfo(self):
        response = zhuorui("Allstock", "查询当天的北向最新资金流动趋势")
        # assert_data(response, '000000', 'ok')

        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert response.json().get("code") == "000000"
            assert response.json().get("msg") == "ok"
            if "data" in j:
                if len(j.get("data")) != 0:
                    for i in range(len(response.json().get("data"))):
                        assert "time" in response.json().get("data")[i]
                        assert "time" in response.json().get("data")[i]
                        assert "balanceSZ" in response.json().get("data")[i]
                        assert "balanceSH" in response.json().get("data")[i]
