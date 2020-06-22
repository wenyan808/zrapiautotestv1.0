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

	@allure.story('查询板块详情页成分股列表_US行业')
	def test_hs(self):
		response = zhuorui('市场行情','查询板块详情页成分股列表_US行业')
		assert_data(response, '000000', 'ok')

	@allure.story('查询板块详情页成分股列表_US概念')
	def test_us(self):
		response = zhuorui('市场行情','查询板块详情页成分股列表_US概念')
		assert_data(response, '000000', 'ok')

	@allure.story('查询板块详情页成分股列表_HS概念')
	def test_uk(self):
		response = zhuorui('市场行情','查询板块详情页成分股列表_HS概念')
		assert_data(response, '000000', 'ok')

	@allure.story('查询板块详情页成分股列表_HS行业')
	def test_canshuwei0(self):
		response = zhuorui('市场行情','查询板块详情页成分股列表_HS行业')
		assert_data(response, '000000', 'ok')

	@allure.story('查询板块详情页成分股列表_HK行业')
	def test_sczdgk(self):
		response = zhuorui('市场行情','查询板块详情页成分股列表_HK行业')
		assert_data(response, '000000', 'ok')

	@allure.story('查询板块详情页成分股列表_HK概念')
	def test_sczdgk(self):
		response = zhuorui('市场行情','查询板块详情页成分股列表_HK概念')
		assert_data(response, '000000', 'ok')

