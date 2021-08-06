# test_US_F10directorbackgroud
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.write_xlsx import write_xlsx



# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSF10directorlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取公司高管-背景介绍')
    def test_US_F10directorlist(self):
        data = {
                "id": f'{zhuorui("Allstock", "公司高管-详情页").json().get("data").get("list")[0].get("id")}'
            }
        write_xlsx("Allstock", 32, 7, str(data))
        response = zhuorui("Allstock", "获取公司高管-背景介绍")
        assert_data(response, '000000', 'ok')

        # if "data" in response.json():
        #     if len(response.json().get("data")) != 0:
                # assert "list" in response.json().get("data")
                # for i in range(len(response.json().get("data").get("list"))):
                #     # assert response.json().get("data").get("list")[i].get("id") == "美元"
                #     assert "id" in response.json().get("data").get("list")[i]
                #     assert "name" in response.json().get("data").get("list")[i]
                #     assert "response.json()ob" in response.json().get("data").get("list")[i]
                #     assert "date" in response.json().get("data").get("list")[i]
                #     assert "active" in response.json().get("data").get("list")[i]
                # assert response.json().get("data").get("total") == 0
                # assert response.json().get("data").get("pageSize") == 15
                # assert response.json().get("data").get("currentPage") == 1
                # print(response.json().get("data"))

        #     else:
        #         logging.info("data是空的集合")
        #
        # else:
        #     logging.info("无data数据")

