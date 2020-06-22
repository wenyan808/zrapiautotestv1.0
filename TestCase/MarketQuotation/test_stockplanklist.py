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

	@allure.story('全部股板行情数据_HS1:涨跌幅')
	def test_hs1(self):
		response = zhuorui('市场行情','全部股板行情数据_HS1:涨跌幅')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HS2:涨跌价')
	def test_hs2(self):
		response = zhuorui('市场行情','全部股板行情数据_HS2:涨跌价')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HS3:现价')
	def test_hs3(self):
		response = zhuorui('市场行情','全部股板行情数据_HS3:现价')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HS4:成交量')
	def test_hs4(self):
		response = zhuorui('市场行情','全部股板行情数据_HS4:成交量')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HS5:成交额')
	def test_hs5(self):
		response = zhuorui('市场行情','全部股板行情数据_HS5:成交额')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HS6:市盈率')
	def test_hs6(self):
		response = zhuorui('市场行情','全部股板行情数据_HS6:市盈率')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HS7:换手率')
	def test_hs7(self):
		response = zhuorui('市场行情','全部股板行情数据_HS7:换手率')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HS8:振幅')
	def test_hs8(self):
		response = zhuorui('市场行情','全部股板行情数据_HS8:振幅')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HS9:市值')
	def test_hs9(self):
		response = zhuorui('市场行情','全部股板行情数据_HS9:市值')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HS_10:量比')
	def test_hs10(self):
		response = zhuorui('市场行情','全部股板行情数据_HS_10:量比')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HS11:委比')
	def test_hs11(self):
		response = zhuorui('市场行情','全部股板行情数据_HS11:委比')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_US1:涨跌幅')
	def test_us1(self):
		response = zhuorui('市场行情','全部股板行情数据_US1:涨跌幅')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_US2:涨跌价')
	def test_us2(self):
		response = zhuorui('市场行情','全部股板行情数据_US2:涨跌价')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_US3:现价')
	def test_us3(self):
		response = zhuorui('市场行情','全部股板行情数据_US3:现价')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_US4:成交量')
	def test_us4(self):
		response = zhuorui('市场行情', '全部股板行情数据_US4:成交量')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_US5:成交额')
	def test_us5(self):
		response = zhuorui('市场行情', '全部股板行情数据_US5:成交额')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_US6:市盈率')
	def test_us6(self):
		response = zhuorui('市场行情', '全部股板行情数据_US6:市盈率')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_US7:换手率')
	def test_us7(self):
		response = zhuorui('市场行情', '全部股板行情数据_US7:换手率')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_US8:振幅')
	def test_us8(self):
		response = zhuorui('市场行情', '全部股板行情数据_US8:振幅')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_US9:市值')
	def test_us9(self):
		response = zhuorui('市场行情', '全部股板行情数据_US9:市值')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_US_10:量比')
	def test_us10(self):
		response = zhuorui('市场行情', '全部股板行情数据_US_10:量比')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_US11:委比')
	def test_us11(self):
		response = zhuorui('市场行情', '全部股板行情数据_US11:委比')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HK1:涨跌幅')
	def test_hk1(self):
		response = zhuorui('市场行情', '全部股板行情数据_HK1:涨跌幅')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HK2:涨跌价')
	def test_hk2(self):
		response = zhuorui('市场行情', '全部股板行情数据_HK2:涨跌价')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HK3:现价')
	def test_hk3(self):
		response = zhuorui('市场行情', '全部股板行情数据_HK3:现价')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HK4:成交量')
	def test_hk4(self):
		response = zhuorui('市场行情', '全部股板行情数据_HK4:成交量')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HK5:成交额')
	def test_hk5(self):
		response = zhuorui('市场行情', '全部股板行情数据_HK5:成交额')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HK6:市盈率')
	def test_hk6(self):
		response = zhuorui('市场行情', '全部股板行情数据_HK6:市盈率')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HK7:换手率')
	def test_hk7(self):
		response = zhuorui('市场行情', '全部股板行情数据_HK7:换手率')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HK8:振幅')
	def test_hk8(self):
		response = zhuorui('市场行情', '全部股板行情数据_HK8:振幅')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HK9:市值')
	def test_hk9(self):
		response = zhuorui('市场行情', '全部股板行情数据_HK9:市值')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HK_10:量比')
	def test_hk10(self):
		response = zhuorui('市场行情', '全部股板行情数据_HK_10:量比')
		assert_data(response, '000000', 'ok')

	@allure.story('全部股板行情数据_HK11:委比')
	def test_hk11(self):
		response = zhuorui('市场行情', '全部股板行情数据_HK11:委比')
		assert_data(response, '000000', 'ok')
