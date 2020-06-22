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

	@allure.story('查询股票市场涨跌概况_HS')
	def test_hs(self):
		response = zhuorui('市场行情', '查询股票市场涨跌概况_HS')
		assert_data(response, '000000', 'ok')

	def test_us(self):
		response = zhuorui('市场行情','查询股票市场涨跌概况_US')
		assert_data(response, '000000', 'ok')

	@allure.story('查询股票市场涨跌概况_HK')
	def test_uk(self):
		response = zhuorui('市场行情','查询股票市场涨跌概况_HK')
		assert_data(response, '000000', 'ok')

	@allure.story('查询股票市场涨跌概况_参数为0')
	def test_canshuwei0(self):
		response = zhuorui('市场行情','查询股票市场涨跌概况_参数为0')
		assert_data(response, '000200', '数据不存在，操作失败')


	@allure.story('查询股票市场涨跌概况_参数为4')
	def test_sczdgk(self):
		response = zhuorui('市场行情','查询股票市场涨跌概况_参数为0')
		assert_data(response, '000200', '数据不存在，操作失败')


