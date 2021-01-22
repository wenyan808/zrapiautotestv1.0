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

    @allure.story('根据选择查询结果数量_选择港股')
    def test_selectorhk(self):
        response = zhuorui('选股器', '根据选择查询结果数量_选择港股')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_选择港股选择第二页')
    def test_selectorhk2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_选择港股选择第二页')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_选择港股选择半导体行业')
    def test_selectorhk0701(self):
        response = zhuorui('选股器', '根据选择查询结果数量_选择港股选择半导体行业')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标小于50亿')
    def test_selectorhkMarkValue1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标小于50亿')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标大于50亿小于500亿')
    def test_selectorhkMarkValue2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标大于50亿小于500亿')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标大于500亿')
    def test_selectorhkMarkValue3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标大于500亿')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标股价小于10')
    def test_selectorlast1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标股价小于10')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标股价大于10小于50')
    def test_selectorlast2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标股价大于10小于50')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标股价大于50小于100')
    def test_selectorlast3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标股价大于50小于100')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标股价大于100')
    def test_selectorlast4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标股价大于100')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标涨跌幅小于-5%')
    def test_selectordiffRate1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标涨跌幅小于-5%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标涨跌幅大于-5%小于0%')
    def test_selectordiffRate2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标涨跌幅大于-5%小于0%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标涨跌幅大于0%小于5%')
    def test_selectordiffRate3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标涨跌幅大于0%小于5%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标涨跌幅大于5%')
    def test_selectordiffRate4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标涨跌幅大于5%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市盈率（静）0-10')
    def test_selectorpeRatioStatic1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市盈率（静）0-10')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市盈率（静）10-20')
    def test_selectorpeRatioStatic2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市盈率（静）10-20')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市盈率（静）20-30')
    def test_selectorpeRatioStatic3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市盈率（静）20-30')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市盈率（静）30-50')
    def test_selectorpeRatioStatic4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市盈率（静）30-50')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市盈率（静）大于50')
    def test_selectorpeRatioStatic5(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市盈率（静）大于50')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市盈率（TTM）0-10')
    def test_selectorpeRatioTTM1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市盈率（静）0-10')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市盈率（TTM）10-20')
    def test_selectorpeRatioTTM2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市盈率（静）10-20')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市盈率（TTM）20-30')
    def test_selectorpeRatioTTM3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市盈率（静）20-30')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市盈率（TTM）30-50')
    def test_selectorpeRatioTTM4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市盈率（静）30-50')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市盈率（TTM）大于50')
    def test_selectorpeRatioTTM5(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市盈率（静）大于50')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市净率小于1')
    def test_selectormarketRate1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市净率小于1')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市净率1-2')
    def test_selectormarketRate2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市净率1-2')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市净率2-3')
    def test_selectormarketRate3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市净率2-3')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市净率3-5')
    def test_selectormarketRate4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市净率3-5')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标市净率大于5')
    def test_selectormarketRate5(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标市净率大于5')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标成交额小于50w')
    def test_selectorturnover1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标成交额小于50w')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标成交额50w-100w')
    def test_selectorturnover2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标成交额50w-100w')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标成交额100w-500w')
    def test_selectorturnover3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标成交额100w-500w')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标成交额500w-2000w')
    def test_selectorturnover4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标成交额500w-2000w')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标成交额大于2000w')
    def test_selectorturnover5(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标成交额大于2000w')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标成交量小于50w')
    def test_selectorsharestraded1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标成交量小于50w')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标成交量50w-100w')
    def test_selectorsharestraded2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标成交量50w-100w')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标成交量100w-500w')
    def test_selectorsharestraded3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标成交量100w-500w')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标成交量500w-2000w')
    def test_selectorsharestraded4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标成交量500w-2000w')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标成交量大于2000w')
    def test_selectorsharestraded5(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标成交量大于2000w')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标量比小于1')
    def test_selectorvolumeRatio1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标量比小于1')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标量比1-3')
    def test_selectorvolumeRatio2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标量比1-3')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标量比3-5')
    def test_selectorvolumeRatio3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标量比3-5')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标量比大于5')
    def test_selectorvolumeRatio4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标量比大于5')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标委比小于0%')
    def test_selectorcomparison1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标委比小于0%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标委比0%-30%')
    def test_selectorcomparison2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标委比0%-30%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标委比30%-50%')
    def test_selectorcomparison3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标委比30%-50%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标委比大于50%')
    def test_selectorcomparison4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标委比大于50%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标换手率小于1%')
    def test_selectorturnoverRate1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标换手率小于1%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标换手率1%-3%')
    def test_selectorturnoverRate2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标换手率1%-3%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标换手率3%-5%')
    def test_selectorturnoverRate3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标换手率3%-5%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标换手率大于5%')
    def test_selectorturnoverRate4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标换手率大于5%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标振幅小于5%')
    def test_selectoramplitude1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标振幅小于5%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标振幅5%-10%')
    def test_selectoramplitude2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标振幅5%-10%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标振幅10%-15%')
    def test_selectoramplitude3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标振幅10%-15%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标振幅大于15%')
    def test_selectoramplitude4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标振幅大于15%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标连涨天数大于3')
    def test_selectorriseDay1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标连涨天数大于3')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标连涨天数大于5')
    def test_selectorriseDay2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标连涨天数大于5')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标连涨天数大于20')
    def test_selectorriseDay3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标连涨天数大于20')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标连涨天数大于10')
    def test_selectorriseDay4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标连涨天数大于10')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标连跌天数大于3')
    def test_selectorfallDay1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标连跌天数大于3')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标连跌天数大于5')
    def test_selectorfallDay2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标连跌天数大于5')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标连跌天数大于10')
    def test_selectorfallDay3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标连跌天数大于10')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标连跌天数大于20')
    def test_selectorfallDay4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标连跌天数大于20')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标上市时间过去1周')
    def test_selectorlistingDay1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标上市时间过去1周')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标上市时间过去1月')
    def test_selectorlistingDay2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标上市时间过去1月')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标上市时间过去1年')
    def test_selectorlistingDay3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标上市时间过去1年')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股行情指标上市时间一年以前')
    def test_selectorlistingDay4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股行情指标上市时间一年以前')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润0-1亿')
    def test_selectorprofit1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润0-1亿')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润1亿-10亿')
    def test_selectorprofit2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润1亿-10亿')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润10亿-20亿')
    def test_selectorprofit3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润10亿-20亿')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润大于20亿')
    def test_selectorprofit4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润大于20亿')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标营业收入0-10亿')
    def test_selectorincome1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标营业收入0-10亿')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标营业收入10亿-100亿')
    def test_selectorincome2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标营业收入10亿-100亿')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标营业收入100亿-500亿')
    def test_selectorincome3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标营业收入100亿-500亿')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标营业收入大于500亿')
    def test_selectorincome4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标营业收入大于500亿')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润增长率小于0')
    def test_selectorprofitRiseRate1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润增长率小于0')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润增长率0-30%')
    def test_selectorprofitRiseRate2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润增长率0-30%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润增长率30%-50%')
    def test_selectorprofitRiseRate3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润增长率30%-50%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标增长率50%-100%')
    def test_selectorprofitRiseRate4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润增长率50%-100%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润增长率大于100%')
    def test_selectorprofitRiseRate5(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润增长率大于100%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标营收增长率小于0')
    def test_selectorprofitRiseRate1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标营收增长率小于0')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标营收增长率0-30%')
    def test_selectorprofitRiseRate2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标营收增长率0-30%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标营收增长率30%-50%')
    def test_selectorprofitRiseRate3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标营收增长率30%-50%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标营收增长率50%-100%')
    def test_selectorprofitRiseRate4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标营收增长率50%-100%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标营收增长率大于100%')
    def test_selectorprofitRiseRate5(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标营收增长率大于100%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标毛利润率0-10%')
    def test_selectorgrossProfitRate1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标毛利润率0-10%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标毛利润率10%-40%')
    def test_selectorgrossProfitRate2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标毛利润率10%-40%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标毛利润率40%-70%')
    def test_selectorgrossProfitRate3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标毛利润率40%-70%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标毛利润率大于70%')
    def test_selectorgrossProfitRate4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标毛利润率大于70%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润率小于0')
    def test_selectorprofitRate1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润率小于0')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润率0%-10%')
    def test_selectorprofitRate2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润率0%-10%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润率10%-20%')
    def test_selectorprofitRate3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润率10%-20%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标净利润率大于20%')
    def test_selectorprofitRate4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标净利润率大于20%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标资产负债率0-30%')
    def test_selectorliabilityRate1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标资产负债率0-30%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标资产负债率30%-50%')
    def test_selectorliabilityRate2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标资产负债率30%-50%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标资产负债率50%-70%')
    def test_selectorliabilityRate3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标资产负债率30%-50%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标资产负债率大于70%')
    def test_selectorliabilityRate4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标资产负债率大于70%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标资产负债率0-10%')
    def test_selectorroe1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标资产负债率0-10%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标资产负债率10%-30%')
    def test_selectorroe2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标资产负债率10%-30%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标资产负债率30%-50%')
    def test_selectorroe3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标资产负债率30%-50%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股财务指标资产负债率大于50%')
    def test_selectorroe4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股财务指标资产负债率大于50%')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标MA多头排列')
    def test_selectorma1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标MA多头排列')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标MA空头排列')
    def test_selectorma2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标MA空头排列')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标MACD金叉')
    def test_selectormacd1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标MACD金叉')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标MACD死叉')
    def test_selectormacd2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标MACD死叉')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标MACD底背离')
    def test_selectormacd3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标MACD底背离')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标MACD顶背离')
    def test_selectormacd4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标MACD顶背离')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标BOLL升穿上轨')
    def test_selectormacd1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标BOLL升穿上轨')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标BOLL升穿中轨')
    def test_selectormacd2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标BOLL升穿中轨')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标BOLL跌穿下轨')
    def test_selectormacd3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标BOLL跌穿下轨')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标BOLLL跌穿中轨')
    def test_selectormacd4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标BOLLL跌穿中轨')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标RSI金叉')
    def test_selectorrsi1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标RSI金叉')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标RSI死叉')
    def test_selectorrsi2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标RSI死叉')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标RSI底背离')
    def test_selectorrsi3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标RSI底背离')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标RSI顶背离')
    def test_selectorrsi4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标RSI顶背离')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标KDJ金叉')
    def test_selectorKDJ1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标KDJ金叉')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标KDJ死叉')
    def test_selectorKDJ2(self):
        response = zhuorui('选股器', '根据选择查询结根据选择查询结果数量_港股技术指标KDJ死叉果列表_港股技术指标RSI死叉')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标KDJ底背离')
    def test_selectorKDJ3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标KDJ底背离')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标KDJ顶背离')
    def test_selectorKDJ4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标KDJ顶背离')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标KDJ金叉')
    def test_selectorKDJ1(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标KDJ金叉')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标KDJ死叉')
    def test_selectorKDJ2(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标KDJ死叉')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标KDJ底背离')
    def test_selectorKDJ3(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标KDJ底背离')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标KDJ顶背离')
    def test_selectorKDJ4(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标KDJ顶背离')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标K线形态早晨之星')
    def test_selectorZCZX(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标K线形态早晨之星')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标K线形态出水芙蓉')
    def test_selectorCSFR(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标K线形态出水芙蓉')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标K线形态旭日东升')
    def test_selectorXRDS(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标K线形态旭日东升')
        assert_data(response, '000000', 'ok')

    @allure.story('根据选择查询结果数量_港股技术指标K线形态蜻蜓点水')
    def test_selectorQTDS(self):
        response = zhuorui('选股器', '根据选择查询结果数量_港股技术指标K线形态蜻蜓点水')
        assert_data(response, '000000', 'ok')