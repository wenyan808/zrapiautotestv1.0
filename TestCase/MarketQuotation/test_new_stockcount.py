#字段说明：
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('板快行情')
class TestClass():

	@classmethod
	def setup_class(cls) -> None:
		login()

	@allure.story('新股日历获取可认购、待上市、今日上市数量')
	def test_newstock(self):
		response = zhuorui('市场行情','新股日历获取可认购、待上市、今日上市数量')
		assert_data(response, '000000', 'ok')

