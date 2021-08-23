# test_nowSrverinfo
import allure
from Common.assertapi import assert_data
from Common.get_time_stamp import TimeTostamp
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason="调试中")
@allure.feature('公共分类')
class TestNowSrverinfo:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取服务器当前的时间戳')
    def test_nowSrverinfo(self):
        response = zhuorui('Allstock', '获取服务器当前的时间戳')
        assert_data(response, '000000', 'ok')

        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert response.json().get("code") == "000000"
            assert response.json().get("msg") == "ok"
            if "data" in response.json():
                assert type(response.json().get("data")) == type(TimeTostamp())

    @allure.story('获取服务器当前的时间戳-newYork')
    def test_nowSrverinfo_newYork(self):
        response = zhuorui('Allstock', '获取服务器当前的时间戳-newYork')
        assert_data(response, '000000', 'ok')

        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert response.json().get("code") == "000000"
            assert response.json().get("msg") == "ok"
            if "data" in response.json():
                assert type(response.json().get("data")) == type(TimeTostamp())
