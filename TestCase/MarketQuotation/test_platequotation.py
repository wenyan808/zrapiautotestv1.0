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

	@allure.story('获取板数据列表_HS科创板')
	def test_hskechuang(self):
		response = zhuorui('市场行情','获取板数据列表_HS科创板')
		assert_data(response, '000000', 'ok')

	@allure.story('获取板数据列表_HS创业板')
	def test_hschuangye(self):
		response = zhuorui('市场行情','获取板数据列表_HS创业板')
		assert_data(response, '000000', 'ok')

	@allure.story('获取板数据列表_HS主板')
	def test_hszhuban(self):
		response = zhuorui('市场行情','获取板数据列表_HS主板')
		assert_data(response, '000000', 'ok')

	@allure.story('获取板数据列表_US中概股')
	def test_uszhonggai(self):
		response = zhuorui('市场行情','获取板数据列表_US中概股')
		assert_data(response, '000000', 'ok')

	@allure.story('获取板数据列表_HK创业板')
	def test_hkchuangye(self):
		response = zhuorui('市场行情','获取板数据列表_HK创业板')
		assert_data(response, '000000', 'ok')

	@allure.story('获取板数据列表_HK主板')
	def test_hkzhuban(self):
		response = zhuorui('市场行情','获取板数据列表_HK主板')
		assert_data(response, '000000', 'ok')
