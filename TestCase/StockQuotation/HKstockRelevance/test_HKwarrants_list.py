import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('港股')
class TestHKstockF10repolist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('全部论证-窝轮牛熊列表涨跌幅排序')
    def test_HKstock_warrantzdf(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表涨跌幅排序')
        assert_data(response, '000000', 'ok')
        # assert response.status_code == 200
        print(response.json())
    @allure.story('全部论证-窝轮牛熊列表涨跌价排序')
    def test_HKstock_warrantzdj(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表涨跌价排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表最新价排序')
    def test_HKstock_warrantzxj(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表最新价排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表成交量排序')
    def test_HKstock_warrantcjl(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表成交量排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表成交额排序')
    def test_HKstock_warrantcje(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表成交额排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表溢价率排序')
    def test_HKstock_warrantyjl(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表溢价率排序')
        # assert_data(response, '000000', 'ok')
        # assert response.status_code == 200
        print(response.json())
    @allure.story('全部论证-窝轮牛熊列表到期日排序')
    def test_HKstock_warrantdqr(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表到期日排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表行使价排序')
    def test_HKstock_warrantxsj(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表行使价排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表街货比排序')
    def test_HKstock_warrantjhb(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表街货比排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表街货量排序')
    def test_HKstock_warrantjhl(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表街货量排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表引伸波幅排序')
    def test_HKstock_warrantysbf(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表引伸波幅排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表收回价排序')
    def test_HKstock_warrantshj(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表收回价排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表距收回价排序')
    def test_HKstock_warrantjshj(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表距收回价排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表杠杆比率排序')
    def test_HKstock_warrantggbl(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表杠杆比率排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表换股比率排序')
    def test_HKstock_warranthgbl(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表换股比率排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表升序排序')
    def test_HKstock_warrantsx(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表升序排序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选认购证')
    def test_HKstock_warrantrgz(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选认购证')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选认沽证')
    def test_HKstock_warrantrguz(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选认沽证')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选牛证')
    def test_HKstock_warrantnz(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选牛证')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选熊证')
    def test_HKstock_warrantxz(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选熊证')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选法兴')
    def test_HKstock_warrantfx(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选法兴')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选法巴')
    def test_HKstock_warrantfb(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选法巴')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选瑞信')
    def test_HKstock_warrantrx(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选瑞信')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选花旗')
    def test_HKstock_warranthq(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选花旗')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选高盛')
    def test_HKstock_warrantgs(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选高盛')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选东亚')
    def test_HKstock_warrantdy(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选东亚')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选汇丰')
    def test_HKstock_warranthf(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选汇丰')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选到期日3月')
    def test_HKstock_warrantdqr3(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选到期日3月')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选到期日3-6月')
    def test_HKstock_warrantdqr6(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选到期日3-6月')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选到期日6-9月')
    def test_HKstock_warrantdqr9(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选到期日6-9月')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选到期日9-12月')
    def test_HKstock_warrantdqr12(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选到期日9-12月')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选到期日12月')
    def test_HKstock_warrantdqr1201(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选到期日12月')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选杠杆比率1')
    def test_HKstock_warrantggbl1(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选杠杆比率1')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选杠杆比率1-5')
    def test_HKstock_warrantggbl5(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选杠杆比率1-5')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选杠杆比率5-10')
    def test_HKstock_warrantggbl10(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选杠杆比率5-10')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('全部论证-窝轮牛熊列表筛选杠杆比率10')
    def test_HKstock_warrantggbl1001(self):
        response = zhuorui('港股', '全部论证-窝轮牛熊列表筛选杠杆比率10')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

