import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('港股')
class TestHKstockF10repolist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('牛熊证/窝轮/界内证今日上市')
    def test_HKstock_warrantt(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市总发行量降序')
    def test_HKstock_warrantzfxlj(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市总发行量降序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市到期日降序')
    def test_HKstock_warrantzfxlj(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市到期日降序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市行使价降序')
    def test_HKstock_warrantxsjj(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市行使价降序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市收回价降序')
    def test_HKstock_warrantshjj(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市收回价降序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市距收回价降序')
    def test_HKstock_warrantjshjj(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市距收回价降序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市换股比率降序')
    def test_HKstock_warranthgblj(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市换股比率降序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市上市日期降序')
    def test_HKstock_warrantssrqj(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市上市日期降序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市发行价降序')
    def test_HKstock_warrantfxjj(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市发行价降序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市每手股数降序')
    def test_HKstock_warrantmsgsj(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市每手股数降序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市总发行量升序')
    def test_HKstock_warrantzfxls(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市总发行量升序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市到期日升序')
    def test_HKstock_warrantzfxls(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市到期日升序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市行使价升序')
    def test_HKstock_warrantxsjs(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市行使价升序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市收回价升序')
    def test_HKstock_warrantshjs(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市收回价升序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市距收回价升序')
    def test_HKstock_warrantjshjs(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市距收回价升序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市换股比率升序')
    def test_HKstock_warranthgbls(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市换股比率升序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市上市日期升序')
    def test_HKstock_warrantssrqs(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市上市日期升序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市发行价升序')
    def test_HKstock_warrantfxjs(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市发行价升序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市每手股数升序')
    def test_HKstock_warrantmsgss(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市每手股数升序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市类型筛选0')
    def test_HKstock_warrantlxsx0(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市类型筛选0')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市类型筛选1')
    def test_HKstock_warrantlxsx1(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市类型筛选1')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市类型筛选2')
    def test_HKstock_warrantlxsx2(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市类型筛选2')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市类型筛选3')
    def test_HKstock_warrantlxsx3(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市类型筛选3')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市类型筛选4')
    def test_HKstock_warrantlxsx4(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市类型筛选4')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市类型筛选5')
    def test_HKstock_warrantlxsx5(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市类型筛选5')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市发行人筛选0')
    def test_HKstock_warrantfxr0(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市发行人筛选0')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市发行人筛选1')
    def test_HKstock_warrantfxr1(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市发行人筛选1')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市发行人筛选2')
    def test_HKstock_warrantfxr2(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市发行人筛选2')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市发行人筛选3')
    def test_HKstock_warrantfxr3(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市发行人筛选3')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市发行人筛选4')
    def test_HKstock_warrantfxr4(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市发行人筛选4')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市发行人筛选5')
    def test_HKstock_warrantfxr5(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市发行人筛选5')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市发行人筛选6')
    def test_HKstock_warrantfxr6(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市发行人筛选6')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市发行人筛选7')
    def test_HKstock_warrantfxr7(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市发行人筛选7')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市到期日筛选0')
    def test_HKstock_warrantdqr0(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市到期日筛选0')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市到期日筛选1')
    def test_HKstock_warrantdqr1(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市到期日筛选1')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市到期日筛选2')
    def test_HKstock_warrantdqr2(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市到期日筛选2')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市到期日筛选3')
    def test_HKstock_warrantdqr3(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市到期日筛选3')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市到期日筛选4')
    def test_HKstock_warrantdqr4(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市到期日筛选4')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市到期日筛选5')
    def test_HKstock_warrantdqr5(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市到期日筛选5')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200

    @allure.story('牛熊证/窝轮/界内证今日上市行使价高100')
    def test_HKstock_warrantxsq(self):
        response = zhuorui('港股', '牛熊证/窝轮/界内证今日上市行使价高100')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
