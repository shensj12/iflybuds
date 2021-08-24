from selenium.webdriver.common.by import By
from Common.myunit import StartEnd
from BusinessView.loginView import LoginView
import logging

class TestLogin(StartEnd):
    csv_file = '../Data/account.csv'

    def test_01_login_no_verificationcode(self):
        logging.info('LOGIN TESTS')
        logging.info('==== test_login_no_verificationcode_01 ====')
        l = LoginView(self.driver)
        # csv文件中的第一行
        data = l.get_csv_data(self.csv_file, 2)
        l.login_action(data[0])
        l.allow_privacy_02()
        l.get_ver()
        # 断言查看是否成功获取验证码
        self.assertFalse(l.check_verificationStatus())

    def test_02_verificationcode_login(self):
        logging.info('==== test_login_success_02 ====')
        l = LoginView(self.driver)
        # csv文件中的第一行
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0])
        l.get_ver()
        # 断言查看是否成功获取验证码
        self.assertTrue(l.check_verificationStatus())
        # 断言查看是否登录成功
        self.assertTrue(l.check_firstlogin())

    def test_03_guide_page(self):
        logging.info('==== test_guide_page_03 ====')
        l = LoginView(self.driver)
        # 断言查看引导页是否正常切换完成
        self.assertTrue(l.check_guidepage_change())

    def test_04_wechat_login(self):
        logging.info('==== test_wechat_login_04 ====')
        l = LoginView(self.driver)
        # 断言是否在登录页，在则点击微信登录按钮
        self.assertFalse(l.Wechat_login())
        # 断言查看是否登录成功
        self.assertTrue(l.check_loginStatus())

    def test_05_authsdk_login(self):
        logging.info('==== test_authsdk_login_05 ====')
        l = LoginView(self.driver)
        # 断言是否在登录页，在则点击一键手机号登录按钮
        self.assertFalse(l.authsdk_login())
        # 断言查看是否登录成功
        self.assertTrue(l.check_loginStatus())
