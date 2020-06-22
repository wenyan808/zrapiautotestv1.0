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

	@allure.story('新股日历获取待上市列表')
	def test_tobelist(self):
		response = zhuorui('市场行情','新股日历获取待上市列表')
		assert_data(response, '000000', 'ok')
