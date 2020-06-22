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

	@allure.story('查询概念板块行情列表数据_HS')
	def test_hs(self):
		response = zhuorui('市场行情','查询概念板块行情列表数据_HS')
		assert_data(response, '000000', 'ok')

	@allure.story('查询概念板块行情列表数据_US')
	def test_us(self):
		response = zhuorui('市场行情','查询概念板块行情列表数据_US')
		assert_data(response, '000000', 'ok')

	@allure.story('查询概念板块行情列表数据_HK')
	def test_uk(self):
		response = zhuorui('市场行情','查询概念板块行情列表数据_HK')
		assert_data(response, '000000', 'ok')
