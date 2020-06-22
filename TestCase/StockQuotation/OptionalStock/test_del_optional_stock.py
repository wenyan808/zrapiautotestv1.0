import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


class TestDelOptionalStock:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('删除自选股_根据code_All')
    def test_code_all(self):
        response = zhuorui('自选股', '删除自选股_根据code_All')
        assert_data(response, '000000', 'ok')

    # @allure.story('删除自选股_根据code_type不正确')
    # def test_code_type_error(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_type不正确')

    # @allure.story('删除自选股_根据code_ts不正确')
    # def test_code_ts_error(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_ts不正确')

    # @allure.story('删除自选股_根据code_参数列表为空')
    # def test_coed_parameter_null(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_参数列表为空')

    # @allure.story('删除自选股_根据code_ts异常')
    # def test_code_ts_exception(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_ts异常')

    # @allure.story('删除自选股_根据code_code不正确')
    # def test_code_code_error(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_code不正确')

    # @allure.story('删除自选股_根据code_code异常')
    # def test_code_code_exception(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_code异常')

    # @allure.story('删除自选股_根据code_code为空')
    # def test_code_code_null(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_code为空')

    # @allure.story('删除自选股_根据code_ts为空')
    # def test_code_ts_null(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_ts为空')

    # @allure.story('删除自选股_根据code_type异常')
    # def test_code_type_exception(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_type异常')

    # @allure.story('删除自选股_根据code_type为空')
    # def test_code_type_null(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_type为空')

    # @allure.story('删除自选股_根据code_ts异常2')
    # def test_code_ts_exception2(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_ts异常2')

# if __name__ == '__main__':
# #     pytest.main()
