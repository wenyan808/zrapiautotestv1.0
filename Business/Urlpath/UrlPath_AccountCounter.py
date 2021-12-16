"""柜台url——path管理
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/12/1 10:12
# @Author:YiShouquan
# @File:UrlPath_AccountCounter.py
"""
# 获取币种汇率列表
UrlPath_money_type_list = "/as_trade/api/rate/v1/money_type_list"
"""恒生3.0-公司行动"""
# 申请选股选息
UrlPath_stock_and_interest_selection = "/as_trade/api/corporate_action/v1/stock_and_interest_selection"
# 选股选息申请列表/选股选息历史记录
UrlPath_stock_and_interest_selection_list = "/as_trade/api/corporate_action/v1/stock_and_interest_selection_list"
# 股票记录(选股选息和申请供股)
UrlPath_stock_record = "/as_trade/api/corporate_action/v1/stock_record"
# 供股列表
UrlPath_apply_rs_corp_right_list = "/as_trade/api/corporate_action/v1/apply_rs_corp_right_list"
# 申请供股
UrlPath_apply_rs_corp_right = "/as_trade/api/corporate_action/v1/apply_rs_corp_right"
"""恒生3.0-预约办理港银卡"""
# 银行信息列表查询
UrlPath_reservation_bank_list = "/as_trade/api/reservation_bank/v1/list"
# 预约办理信息提交
UrlPath_reservation_bank_submit = "/as_trade/api/reservation_bank/v1/submit"
"""恒生3.0-预约办理港银卡（console"""
# 列表查询（包含详情）
UrlPath_con_reservation_bank_list = "/api/con_reservation_bank/v1/list"
# 重复预约记录
UrlPath_con_reservation_bank_reservation_record = "/api/con_reservation_bank/v1/reservation_record"
# 确认办理
UrlPath_con_reservation_bank_confirmation = "/api/con_reservation_bank/v1/confirmation"
# 预约银行编辑修改
UrlPath_con_reservation_bank_update_bank = "/api/con_reservation_bank/v1/update_bank"
# 银行信息列表查询
UrlPath_con_reservation_bank_bank_list = "/api/con_reservation_bank/v1/bank_list"
"""恒生3.0-转仓"""
# 搜索券商
UrlPath_brokerage_search = "/as_trade/api/brokerage/v1/search"
# 提交转仓申请
UrlPath_brokerage_transfer_submit = "/as_trade/api/brokerage/v1/transfer_submit"
# 转股记录列表
UrlPath_transfer_stock_list = "/as_trade/api/brokerage/v1/transfer_stock_list"
# 查看转仓记录详情
UrlPath_transfer_detail = "/as_trade/api/brokerage/v1/transfer_detail"
# 撤销转仓申请
UrlPath_transfer_cancel = "/as_trade/api/brokerage/v1/transfer_cancel"
"""恒生3.0-股票转入（console）"""
# 列表查询
UrlPath_con_brokerage_list = "/api/con_brokerage/v1/list"
# 详情查询
UrlPath_con_brokerage_details = "/api/con_brokerage/v1/details"
# 审核
UrlPath_con_brokerage_audit = "/api/con_brokerage/v1/"
"""恒生3.0-账户分析"""
# 定时任务账户资金分析
UrlPath_定时任务账户资金分析 = "/"
# 盈亏分析
UrlPath_analysis_profit = "/as_trade/api/analysis/v1/profit"
# 收益曲线
UrlPath_analysis_income_curve = "/as_trade/api/analysis/v1/income_curve"
# 资产走势
UrlPath_analysis_assets = "/as_trade/api/analysis/v1/assets"
# 个股盈亏
UrlPath_analysis_stocks_income = "/as_trade/api/analysis/v1/stocks_income"
# 持仓偏好
UrlPath_analysis_hold_preference = "/as_trade/api/analysis/v1/hold_preference"
# 新股盈亏分析
UrlPath_ipo_analysis_profit = "/as_trade/api/ipo_analysis/v1/profit"
# 新股盈亏明细
UrlPath_ipo_analysis_list = "/as_trade/api/ipo_analysis/v1/list"
# 账户分析、新股盈亏-数据更新完时间点获取
UrlPath_analysis_tm_get_update_time = "/as_trade/api/analysis_tm/v1/get_update_time"
"""恒生3.0-货币兑换"""
# 兑换
UrlPath_money_exchange_add = "/as_trade/api/money_exchange/v1/add"
# 币种兑换手续费
UrlPath_money_exchange_fee = "/as_trade/api/money_exchange/v1/fee"
# 兑换记录
UrlPath_money_exchange_list = "/as_trade/api/money_exchange/v1/list"
"""恒生3.0-R智投策略投资"""
# R智投列表
UrlPath_strategy_list = "/as_trade/api/strategy/v1/list"
# 用户订阅组合列表
UrlPath_strategy_client_subscribe_list = "/as_trade/api/strategy/v1/client_subscribe_list"
# 订阅策略
UrlPath_strategy_subscribe = "/as_trade/api/strategy/v1/subscribe"
# 取消订阅策略
UrlPath_strategy_un_subscribe = "/as_trade/api/strategy/v1/un_subscribe"
# 组合详情
UrlPath_strategy_strategy_detail = "/as_trade/api/strategy/v1/strategy_detail"
# 获取调仓记录分页
UrlPath_strategy_position_change_page = "/as_trade/api/strategy/v1/position_change_page"
# 一键跟投-组合仓位
UrlPath_strategy_combination_position = "/as_trade/api/strategy/v1/combination_position"
# 恒生3.0-查用户的策略持仓
UrlPath_get_combination_hold_list = "/as_trade/api/order/v1/get_combination_hold_list"
# 恒生3.0-一键下单(买或卖)
UrlPath_r_batch_entrust_enter = "/as_trade/api/order/v1/r_batch_entrust_enter"
# 恒生3.0-查询客户持仓组合列表
UrlPath_get_r_hold_list = "/as_trade/api/order/v1/get_r_hold_list"
# 策略基础数据恢复方案
UrlPath_策略基础数据恢复方案 = "/todo_2"
# 定时任务-策略每日基础数据保存
UrlPath_定时任务_策略每日基础数据保存 = "/todo44sd"
"""恒生3.0-订单"""
# 下单
UrlPath_entrust_enter = "/as_trade/api/order/v1/entrust_enter"
# 持仓列表
UrlPath_get_hold_list = "/as_trade/api/order/v1/get_hold_list"
# 委托成交详情
UrlPath_entrust_detail = "/as_trade/api/order/v1/entrust_detail"
# 持仓明细
UrlPath_get_hold_detail = "/as_trade/api/order/v1/get_hold_detail"
# 改单
UrlPath_entrust_modify = "/as_trade/api/order/v1/entrust_modify"
# 撤单
UrlPath_entrust_withdraw = "/as_trade/api/order/v1/entrust_withdraw"
# 查询当日委托
UrlPath_get_today_entrust = "/as_trade/api/order/v1/get_today_entrust"
# 获取可卖数量
UrlPath_get_stock_amount = "/as_trade/api/order/v1/get_stock_amount"
# 查询所有委托
UrlPath_get_all_entrust = "/as_trade/api/order/v1/get_all_entrust"
# 获取客户交易费用
UrlPath_get_client_trade_fare = "/as_trade/api/fare/v1/get_client_trade_fare"
"""恒生3.0-客户账户"""
# 修改交易密码
UrlPath_change_trade_pwd = "/as_trade/api/account/v1/change_trade_pwd"
# 登录认证
UrlPath_accountauth = "/as_trade/api/account/v1/auth"
# 获取账户资产信息
UrlPath_fundsinfo = "/as_trade/api/funds/v1/info"
# 获取客户证券等信息
UrlPath_accountinfo = "/as_trade/api/account/v1/info"
# 设置客户断线续约时长
UrlPath_account_set_renewal_time = "/as_trade/api/account/v1/set_renewal_time"
# 账户验证/效验
UrlPath_account_validation = "/as_trade/api/account/v1/validation"
# 查询最大购买力
UrlPath_funds_get_enable_balance = "/as_trade/api/funds/v1/get_enable_balance"
# 重置交易密码-步骤一
UrlPath_account_to_reset_pwd = "/as_trade/api/account/v1/to_reset_pwd"
# 重置交易密码-步骤二
UrlPath_account_reset_pwd = "/as_trade/api/account/v1/reset_pwd"
# app进入后台-断线续约倒计时
UrlPath_account_disconn_countdown = "/as_trade/api/account/v1/disconn_countdown"
"""恒生3.0-出入金"""
# 交易入金汇款银行查询
UrlPath_remit_bank_list = "/as_trade/api/remit_bank/v1/list"
# 存入资金
UrlPath_fund_deposit = "/as_trade/api/fund/v1/deposit"
# 提取资金
UrlPath_fund_withdraw = "/as_trade/api/fund/v1/withdraw"
# 手续费计算
UrlPath_fund_procedure_fee = "/as_trade/api/fund/v1/procedure_fee"
# 资金记录
UrlPath_fund_record = "/as_trade/api/fund/v1/record"
# 新增绑定银行卡
UrlPath_savebank = "/as_trade/api/bank/v1/save"
# 用户绑定银行卡列表查询
UrlPath_banklist = "/as_trade/api/bank/v1/list"
# 用户中文姓名查询
UrlPath_get_name = "/as_user/api/client/v1/get_name"
# 获取用户资金账户列表
UrlPath_get_fund_account = "/as_trade/api/fund/v1/get_fund_account"
# 资产记录-存入资金（待激活用户）
UrlPath_fund_nonactivated_record = "/as_trade/api/fund/v1/nonactivated_record"
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
#
# UrlPath_ = ""
