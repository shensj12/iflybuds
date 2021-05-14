from Common.myunit import StartEnd
from BusinessView.loginView import LoginView
import unittest
import logging

class TestLogin(StartEnd):
    csv_file = '../Data/account.csv'
    def test_login_no_verificationcode(self):
        logging.info('==== test_login_no_verificationcode ====')
        l=LoginView(self.driver)
        # csv文件中的第一行
        data=l.get_csv_data(self.csv_file,2)
        l.login_action(data[0])
        # 断言查看是否成功获取验证码
        self.assertFalse(l.check_verificationStatus())

    def test_verificationcode_login(self):
        logging.info('==== test_login_success ====')
        l=LoginView(self.driver)
        # csv文件中的第一行
        data=l.get_csv_data(self.csv_file,1)
        l.login_action(data[0])
        # 断言查看是否成功获取验证码
        self.assertTrue(l.check_verificationStatus())
        # 断言查看是否登录成功
        self.assertTrue(l.check_loginStatus())

    def test_wechat_login(self):
        logging.info('==== test_wechat_login ====')
        l=LoginView(self.driver)
        # 断言是否在登录页，在则点击微信登录按钮
        self.assertFalse(l.Wechat_login())
        # 断言查看是否登录成功
        self.assertTrue(l.check_loginStatus())

    def test_authsdk_login(self):
        logging.info('==== test_authsdk_login ====')
        l = LoginView(self.driver)
        # 断言是否在登录页，在则点击一键手机号登录按钮
        self.assertFalse(l.authsdk_login())
        # 断言查看是否登录成功
        self.assertTrue(l.check_loginStatus())

