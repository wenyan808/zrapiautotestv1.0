# test_US_F10directorlist
import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSF10directorlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('公司高管-详情页')
    def test_US_F10directorlist(self):
        response = zhuorui("Allstock", "公司高管-详情页")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "list" in response.json().get("data")
                for i in range(len(response.json().get("data").get("list"))):
                    # assert response.json().get("data").get("list")[i].get("code") == paylo.get("code")
                    assert "id" in response.json().get("data").get("list")[i]
                    assert "name" in response.json().get("data").get("list")[i]
                    assert "job" in response.json().get("data").get("list")[i]
                    if "date" in response.json().get("data").get("list")[i]:
                        assert "date" in response.json().get("data").get("list")[i]
                    assert "active" in response.json().get("data").get("list")[i]
                assert "total" in response.json().get("data")
                # assert response.json().get("data").get("pageSize") == paylo.get("pageSize")
                # assert response.json().get("data").get("currentPage") == paylo.get("currentPage")
                # print(response.json().get("data"))

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")
