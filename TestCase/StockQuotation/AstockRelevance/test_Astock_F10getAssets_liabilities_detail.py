import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockF10getAssetsLiabilitiesDetail:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('A股F10获取资产负债详情页数据')
    def test_Astock_F10getAssets_liabilities_detail(self):
        response = zhuorui('A股', 'A股F10获取资产负债详情页数据')
        assert_data(response, '000000', 'ok')