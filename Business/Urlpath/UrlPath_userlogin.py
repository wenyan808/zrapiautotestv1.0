"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/11/11 16:09
# @Author:YiShouquan
# @File:UrlPath_userlogin.py
"""
"""账号相关"""
# 用户密码登陆
UrlPath_user_login_pwd = "/as_user/api/user_account/v1/user_login_pwd"
# 发送短信
UrlPath_send_code = "/as_notification/api/sms/v1/send_code"
# 设备验证下一步
UrlPath_device_next = "/as_user/api/user_account/v1/device_next"
# 用户验证码登陆
UrlPath_user_login_code = "/as_user/api/user_account/v1/user_login_code"
# 第一次登陆注册系统账户时设置登录密码
UrlPath_set_login_password = "/as_user/api/user_account/v1/set_login_password"
# 忘记登录密码 - 第一步
UrlPath_forgot_password_code = "/as_user/api/user_account/v1/forgot_password_code"
# 忘记登录密码-第二步
UrlPath_reset_login_password = "/as_user/api/user_account/v1/reset_login_password"
# token刷新
UrlPath_refresh_token = "/as_user/api/user_account/v1/refresh_token"
# 退出登陆
UrlPath_sign_out = "/as_user/api/user_account/v1/sign_out"
# 修改手机号-当前使用手机号验证
UrlPath_modify_phone_v1 = "/as_user/api/user_account/v1/modify_phone_v1"
# 修改手机号-新手机号验证
UrlPath_modify_phone_v2 = "/as_user/api/user_account/v1/modify_phone_v2"
# 修改登录密码-第一步
UrlPath_modify_login_password_v1 = "/as_user/api/user_account/v1/modify_login_password_v1"
# 修改登陆密码-第二步
UrlPath_modify_login_password_v2 = "/as_user/api/user_account/v1/modify_login_password_v2"

"""美股非专业投资者声明"""
# 获取是否已签署非专业投资者声明
UrlPath_get_investor_questionnaire = "/as_user/api/investor_questionnaire/v1/get"
# 提交非专业投资者声明签署内容
UrlPath_add_investor_questionnaire = "/as_user/api/investor_questionnaire/v1/add"
"""第三方登录相关"""
# 第三方登陆接口
UrlPath_user_login_third = "/as_user/api/user_third/v1/user_login_third"
# 绑定手机号码-绑定第三方账号登录
UrlPath_bind_third_login = "/as_user/api/user_third/v1/bind_third_login"
# 查询用户绑定第三方账号信息
UrlPath_get_bind_third_user = "/as_user/api/user_third/v1/get_bind_third_user"
# 绑定第三方账号操作
UrlPath_bind_third_info = "/as_user/api/user_third/v1/bind_third_info"
# 与第三方账号解绑
UrlPath_unbind_third_info = "/as_user/api/user_third/v1/unbind_third_info"
"""用户市场行情权限"""
# 获取用户市场行情权限
UrlPath_get_user_market_auth_info = "/as_user/api/user_market_auth/v1/info"
"""专属顾问"""
# 用户获取专属顾问
UrlPath_get_by_user_id = "/as_user/api/consultant/v1/get_by_user_id"
"""主页信息"""
# 获取用户信息(包含统计信息)
UrlPath_get_user_info = "/as_user/api/user_info/v1/info"
# 查询当前登录用户是否关注了ta
UrlPath_is_follow = "/as_user/api/follow/v1/is_follow"
# 获取用户信息
UrlPath_by_user_id = "/as_user/api/user_account/v1/by_user_id"
# 修改用户信息
UrlPath_update_user_info = "/as_user/api/user_info/v1/update"
# 关注用户
UrlPath_add_follow = "/as_user/api/follow/v1/add"
# 取消用户关注
UrlPath_cancel_follow = "/as_user/api/follow/v1/cancel"
# 我的关注列表
UrlPath_follow_list = "/as_user/api/follow/v1/list"
# 我的粉丝列表
UrlPath_fans_list = "/as_user/api/fans/v1/list"
"""黑名单"""
# 拉黑用户
UrlPath_add_user_black = "/as_user/api/user_black/v1/add"
# 解除拉黑
UrlPath_del_user_black = "/as_user/api/user_black/v1/del"
# 黑名单列表
UrlPath_user_black_list = "/as_user/api/user_black/v1/list"
"""实名认证"""
# app 新增实名认证（校验验证码）
UrlPath_user_certification_check_code = "/as_user/api/user_certification/v1/check_code"
"""实名认证（console）"""
# 新增实名认证（内部调用）
UrlPath_add_user_certification = "/api/user_certification/v1/add"
# 判断是否实名认证（内部调用）
UrlPath_user_certification_estimate = "/api/user_certification/v1/certification"
# console认证列表
UrlPath_con_user_certification_list = "/api/con_user_certification/v1/list"
"""登录设备管理 （console"""
# 设备-console
UrlPath_con_device_list = "/api/con_device/v1/list"
"""登录设备管理"""
# 设备查询
UrlPath_device_list = "/as_user/api/device/v1/list"
# 设备移除
UrlPath_ = "/as_user/api/device/v1/remove"
