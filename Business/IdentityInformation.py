ownerCardType = '0101'
'''开户人证件类型
中国内地居民
    内地身份证(0101)
香港永久居民
    香港居民身份证（0201）
香港非永久居民
    香港临时身份证+大陆身份证（0301,0302）
    香港临时身份证+签证身份书（0301,0303）
    香港临时身份证+特区护照（0301,0304）
澳门永久居民
    澳门居民身份证（0401）
澳门非永久居民
    澳门临时身份证+大陆身份证(0501,0502)
    澳门临时身份证+澳门旅游证(0501,0503)
    澳门临时身份证+特区护照(0501,0504)
其他
    护照（0601）
'''
cardType = "0101"
"""证件类型： 
    中国内地居民（01） 
        内地身份证(0101)

    香港永久居民（02）
        香港永久居民身份证（0201）

    香港非永久居民(03)
        香港临时居民身份证（0301）
        大陆身份证（0302）
        签证身份书（0303）
        特区护照（0304）

    澳门永久居民（04）	 
        澳门永久居民身份证（0401）

    澳门非永久居民(05)	
        澳门临时居民身份证(0501)
        大陆身份证(0502)
        澳门旅游证(0503)
        特区护照(0504)

    其他（06）
        护照（0601）

    见证人信息（07）
        内地(0701)
        香港(0702)
        澳门(0703)
        其他地区(0704)
"""
# 内地
identityTypes = [1]  # 身份类型 1-大陆居民 2-我是港澳地区居民 3-我是其他地区居民 海外居民，传入2,3
Derivative = "false"  # 是否投资衍生品"false"/"true"
phoneArea = '86'  # 地区
nationality = 86  # 国籍   中国内地-86    中国香港-852   中国澳门-853   新加坡-65
sex = 0  # 用户性别    1-男 0-女
cardName = '杨梦梅'  # 证件姓名
cardNo = '430681199305029026'  # 证件号码
cardLastNamePinyin = 'YANG'  # 证件姓拼音
cardNamePinyin = 'MENGMEI'  # 证件名拼音
address = '广东省深圳市南山区科苑路5号科技园工业厂房24栋南段五层西'  # 通讯地址
homeAddress = ''  # 住宅地址(港澳+其他地区必填)
homeAddress_img_Name = "homeAddress_img_Name.png"  # 住宅地址证明名称
# homeAddressUrl = ''  # 住宅地址证明url(港澳+其他地区必填)
catalog = '/Business/UserFileUp/'  # 住宅地址证明照片的存放路径
homeAddress_photo = 'homeAddress_img_Name.png'  # 住宅地址证明照片名称
mailbox = '510210300@qq.com'  # 邮箱
bankCardNo = '62148578049521431'  # 银行卡号
bankCardName = 2  # 银行名称
cardSex = '女'
cardNation = '汉'
cardBirth = '1993-05-02'
# 香港
# identityTypes = [2]  # 身份类型 1-大陆居民 2-我是港澳地区居民 3-我是其他地区居民 海外居民，传入2,3
# Derivative = "false"  # 是否投资衍生品"false"/"true"
# phoneArea = '86'  # 地区
# nationality = 852  # 国籍   中国内地-86    中国香港-852   中国澳门-853   新加坡-65
# sex = 1  # 用户性别    1-男 0-女
# cardName = '龍子鑫'  # 证件姓名
# cardNo = '561802561970'  # 证件号码
# cardLastNamePinyin = 'LONG'  # 证件姓拼音
# cardNamePinyin = 'ZIXIN'  # 证件名拼音
# address = '广东省深圳市南山区科苑路5号科技园工业厂房24栋南段五层西'  # 通讯地址
# homeAddress = ''  # 住宅地址(港澳+其他地区必填)
# homeAddress_img_Name = "homeAddress_img_Name.png"  # 住宅地址证明名称
# # homeAddressUrl = ''  # 住宅地址证明url(港澳+其他地区必填)
# catalog = '/Business/UserFileUp/'  # 住宅地址证明照片的存放路径
# homeAddress_photo = ''  # 住宅地址证明照片名称
# mailbox = '510210300@qq.com'  # 邮箱
## bankCardNo = '62148578049521431'  # 银行卡号
## bankCardName = 2  # 银行名称
# cardSex = '男'
## cardNation = '汉'
# cardBirth = '1975-11-25'
'''
BOC(1, '中国银行'),            PINGAG(6, '平安银行'),         MSYH(11, '民生银行'),
CCB(2, '建设银行'),            CMB(7, '招商银行'),            ZXYH(12, '中信银行'),
ICBC(3, '工商银行'),           CGBC(8, '广发银行'),           GDYH(13, '光大银行'),
ABC(4, '农业银行'),            HXYH(9, '华夏银行'),           OTHER(0, '其他银行');
BCM(5, '交通银行'),            XYYH(10, '兴业银行')
'''
img_name01 = 'yang01.png'  # 存放身份证正面图片的名字，如****.jpg
img_name02 = 'yang02.png'  # 存放身份证方面图片的名字
img_filename = 'feige.mp4'  # 存放人脸核身视频的名字
bankCard = 'guo.png'
# bankCardUrl = 'open/images/2021/04/12/16181960179037331.jpg'  # 银行卡图片url
bankCardPhone = '13691843190'  # 银行卡手机预留号码
# videoUrl = 'open/video/2021/03/15/16157779058400411.mp4'
signatureUrl = 'open/images/2021/04/12/16181961029023150.jpeg'
# cardFrontUrl = 'open/images/2021/04/12/16181956539613025.jpg'
# cardBackUrl = 'open/images/2021/04/12/16181956602830908.jpg'
signature_imgname = 'gexinqianm.jpeg'  # 个人签名图片名称
witnessSignaturename = ''  # 见证人电子签名图片名称(港澳地区+其他地区开户时需要)
bankCardUrl = None

phone6 = '15814213200'  # 卓锐登陆的手机号
pwd = 'zr123456'

# 财务状况
fsWorkStatus = 1  # 财务状况-工作状态 1-受雇   2-自雇  3-退休 4-自由投资者 5-其他
fsWorkDesc = None  # 工作状态为其他时详细工作描述
fsCompanyName = "深圳市卓锐科技有限公司"  # 财务状况-公司名称
fsPost = 2  # 职位 1-基层员工 2-中层管理人员 3-高级经理/主管 4-总裁/总经理 5-董事/股东 6-其他_说明详细职位
fsPostOther = None  # 职位为其他时的补充
fsIndustry = 2  # 行业性质 1-金融类 2-互联网/IT 3-广告传媒 4-商业/贸易 5-加工制造 6-服务行业 7-医药生物 8-教育培训
# 9-政府机关/事业部 10-学生或待业 11-其他_说明详细行业
fsIndustryOther = None  # 行业性质为其他时的补充
fsIncome = 3  # 财务状况-年收入   1- 100w+ 2- 50-100w  3- 20-50w   4- 20w内
fsTotalAssets = 4  # 总资产 1 1000万以上 2 200-1000万 3 50-200万 4 50万以内
fsRisk = 2  # 财务状况-风险承受能力   1-高  2-中   3-低
fsWealthSource = 1  # 财务状况-财富来源   1- 薪资/花红    2- 储蓄   3- 投资回报   4- 退休金   5- 遗产   6- 其他
fsWealthSourceOther = None  # 财富来源为其他时，对其他进行补充说明
fsFundSource = 1  # 财务状况-资金来源   1- 中国内地   2- 中国港澳台地区    3- 美国    4- 其他
fsFundSourceOther = None  # 资金来源地为其他时，对其他进行补充说明

# 投资经验
investBond = 3  # 股票投资经验1  5年以上 2  3-5年 3  1-3年 4  1年内 5   无
investFund = 3  # 基金投资经验 1  5年以上 2  3-5年 3  1-3年 4  1年内 5  无
investFixed = 3  # 固收投资经验   1  5年以上 2  3-5年 3  1-3年 4  1年内 5  无
investWarrants = 3  # 认证股投资经验  1  5年以上 2  3-5年 3  1-3年 4  1年内 5  无
investOther = 3  # 其它投资经验 1  5年以上 2  3-5年 3  1-3年 4  1年内 5  无
investRate = 2  # 每月交易频率   1 大于20次2  6-20次 3  0-5次
investTarget = 2  # 投资目标 1-股息回报 2-资本增值 3-投机 4-保本 5-对冲 6-其他
investTime = 3  # 预计投资时间 1  5年以上   2  3-5年   3  1-3年    4  1年内
investAmount = 4  # 预计投资金额   1 500万以上 2 100万-500万 3  100万-50万 4 30万-100万 5 30万内
investReserveFund = 1  # 您现时的储备资金足够应付多少个月的开支及以面对突如其来的情况？ 1 12个月以上   2 6~12个月   3 3~6个月   4 不足3个月   5 无法应付
investLossScope = 1  # 您可以接受哪个范围的投资金额潜在损失范围？ 1 75% 以上 2 51% - 75%  3 21% - 50% 4 11% - 20% 5 低于 10%
# 见证人证件选择(海外开户)
witnessCardType = "0701"  # 见证人信息 内地(0701) 香港(0702) 澳门(0703) 其他地区(0704)
# 见证人信息
witnessCardNo = ''  # 见证人证件号（见证人的证件号和申请人不能一样）
witnessCardName = ''  # 见证人证件中文姓名（见证人为大陆居民时必填）
witnessPracticeType = ''  # 见证人执业身份
witnessPracticeOther = ''  # 见证人其他执业身份
witnessPracticeNo = ''  # 见证人执业证号
witnessLastNamePinyin = ''  # 见证人证件姓拼音
witnessNamePinyin = ''  # 见证人证件名拼音
witnessPracticeimgname = ''  # 见证人执业证书图片名字
witnessPracticePerson_imgname = ''  # 见证人执业证书人像面图片名字

# 调查文件名称
Files_name = "zhanghupingzheng2.JPG"

# 新增银行卡信息：
# 前期参考：https://www.kdocs.cn/l/chG1vjCIZTz6
# bankRegion = 1  # 银行地区 1-香港银行 2-美国/境外行 3-无香港及境外行   number
# bankName = '中国银行(香港)彩虹道分行'  # 银行名称   string
supportMoneyType = 1  # 支持存入币种 1-港币账户 2-美元账户 3-人民币账户 4-全币种账户   number  ----->   注意：：：境外银行的币种类型必须是美元账户
bankAccount = ''  # 账户号码 string
# rtgsCode = 'HASEHKHH'  # 代码（RTGS) string
# swift = '024'  # 银行SWIFT码  string
# bankAddress = '香港新蒲岗彩虹道58号'  # 银行地址   string
# payeeAddress = '朱韦卓'  # 收款人地址 string
# bankAccountDocument = '|'  # 上传银行账户凭证url 多张照片以|隔开   string
# bindBankId = ''  # 银行id  string

# 银行名称          银行SWIFT码   银行id
# 恒生银行               024        1
# 民生银行香港分行        353        2
# 招商银行香港银行         238        3
# 汇丰银行                   004        4
# 中国建设银行（亚洲）        009         5

# 新增银行名称列表（后期优化，应该是访问接口，目前是前端写死，我们访问接口目前使用这个进行新增银行账户）
add_bankname_list = {"YHXX_list": [
    {'bankRegion': 1, 'list': [{
        'bankName': '恒生银行',
        'supportMoneyType': supportMoneyType,
        'bankAccount': bankAccount,
        'rtgsCode': 'HASEHKHH',
        'swift': '024',
        'bankAddress': '83 Des Voeux Road Central Hong Kong',
        'payeeAddress': '83 Des Voeux Road Central Hong Kong',
        'bindBankId': '1'
    },
        {
            'bankName': '民生银行香港分行',
            'supportMoneyType': supportMoneyType,
            'bankAccount': bankAccount,
            'rtgsCode': 'HASEHKHH',
            'swift': '353',
            'bankAddress': '84 Des Voeux Road Central Hong Kong',
            'payeeAddress': '84 Des Voeux Road Central Hong Kong',
            'bindBankId': '2'
        },
        {
            'bankName': '招商银行香港银行',
            'supportMoneyType': supportMoneyType,
            'bankAccount': bankAccount,
            'rtgsCode': 'HASEHKHH',
            'swift': '009',
            'bankAddress': '90 Des Voeux Road Central Hong Kong',
            'payeeAddress': '90 Des Voeux Road Central Hong Kong',
            'bindBankId': '5'
        },
        {
            'bankName': '汇丰银行',
            'supportMoneyType': supportMoneyType,
            'bankAccount': bankAccount,
            'rtgsCode': 'HASEHKHH',
            'swift': '004',
            'bankAddress': '85 Des Voeux Road Central Hong Kong',
            'payeeAddress': '85 Des Voeux Road Central Hong Kong',
            'bindBankId': '4'
        },
        {
            'bankName': '中国建设银行(亚洲)',
            'supportMoneyType': supportMoneyType,
            'bankAccount': bankAccount,
            'rtgsCode': 'HASEHKHH',
            'swift': '024',
            'bankAddress': '83 Des Voeux Road Central Hong Kong',
            'payeeAddress': '83 Des Voeux Road Central Hong Kong',
            'bindBankId': '5'
        },
        {
            'bankName': '恒生银行',
            'supportMoneyType': supportMoneyType,
            'bankAccount': bankAccount,
            'rtgsCode': 'HASEHKHH',
            'swift': '024',
            'bankAddress': '83 Des Voeux Road Central Hong Kong',
            'payeeAddress': '83 Des Voeux Road Central Hong Kong',
            'bindBankId': '2'
        }
    ]
     },
    {'bankRegion': 2, 'list': [{
        'bankName': 'Velo华美银行',
        'supportMoneyType': supportMoneyType,
        'bankAccount': bankAccount,
        'rtgsCode': 'HASEHKHH',
        'swift': 'EWBKUS666XXX',
        'bankAddress': '83 Des Voeux Road Central Hong Kong',
        'payeeAddress': '83 Des Voeux Road Central Hong Kong',
        'bindBankId': '2'
    },
        {
            'bankName': '标准国际银行',
            'supportMoneyType': supportMoneyType,
            'bankAccount': bankAccount,
            'rtgsCode': 'HASEHKHH',
            'swift': 'GPELPRSJ',
            'bankAddress': '83 Des Voeux Road Central Hong Kong',
            'payeeAddress': '83 Des Voeux Road Central Hong Kong',
            'bindBankId': '2'
        }]
     }]
}
