import logging
from Common.common_fun import Common,NoSuchElementException
from Common.desired_caps import  appium_desired
from selenium.webdriver.common.by import By
from time import sleep

class LoginView(Common):
    phonenum_type=(By.ID,'tws.iflytek.headset:id/input')
    btn_getver=(By.ID,'tws.iflytek.headset:id/button_tv')
    wechat_btn=(By.ID,'tws.iflytek.headset:id/login_type_wx')
    btn_set=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/b.b.k.a.c[4]/android.widget.FrameLayout')
    btn_setting_account=(By.ID,'tws.iflytek.headset:id/setting_account')
    btn_loginout=(By.ID,'tws.iflytek.headset:id/login_out')
    btn_authsdk_login=(By.ID,'tws.iflytek.headset:id/authsdk_login_view')

    # 输入手机号码后获取验证码
    def login_action(self,phone_num):
        logging.info('===== login_action =====')
        logging.info('===== check_change_phonenum =====')
        self.check_change_phonenum()
        logging.info('Empty notification bar')
        self.swipeDown()
        self.check_deleteBtn()

        logging.info('phonenumber is:%s'%phone_num)
        self.driver.find_element(*self.phonenum_type).send_keys(phone_num)

        logging.info('click vergetBtn')
        self.driver.find_element(*self.btn_getver).click()

    # 检查是否发送了验证码
    def check_verificationStatus(self):
        logging.info('check verificationStatus')
        sleep(3)
        try:
            self.driver.find_element(*self.phonenum_type)
        except NoSuchElementException:
            logging.info('get verificationcode  success!')
            self.get_verificationcode()
            return True
        else:
            logging.error('get verificationcode Fail!')
            self.getScreenShot('get verificationcode Fail')
            return False

    # 获取验证码并输入
    def get_verificationcode(self):
        logging.info('get verification code')
        self.swipeDown()
        idd = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("科大讯飞")')
        messagecontent = idd.text  # 获取短信内容
        logging.info('messagecontent：' + messagecontent)
        # 截验证码
        verificationcode = messagecontent[13:19]
        logging.info('verificationcode is'+ verificationcode)
        # 将通知栏划上去
        self.swipeUp()
        # 通知过多可能需要划两次才可划上去
        self.swipeUp()
        # 输入验证码
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]").send_keys(
            verificationcode[0])
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]").send_keys(
            verificationcode[1])
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[3]").send_keys(
            verificationcode[2])
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[4]").send_keys(
            verificationcode[3])
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[5]").send_keys(
            verificationcode[4])
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[6]").send_keys(
            verificationcode[5])
        logging.info('====login finished!====')
    # 检查是否登录
    def check_loginStatus(self):
        logging.info('===== check_loginStatus =====')
        try:
            self.driver.find_element(*self.btn_set)
        except NoSuchElementException:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            self.logout_action()
            return True
    # 退出登录
    def logout_action(self):
        logging.info('==== logout_action ==== ')
        self.driver.find_element(*self.btn_set).click()
        self.driver.find_element(*self.btn_setting_account).click()
        self.driver.find_element(*self.btn_loginout).click()
        logging.info('==== logout success! ====')
    # 微信登录
    def Wechat_login(self):
        logging.info('==== Wechat_login ====')
        try:
            self.driver.find_element(*self.btn_set)
        except NoSuchElementException:
            logging.error('start Wechatlogin!')
            self.driver.find_element(*self.wechat_btn).click()
            return False
        else:
            logging.info('already logged')
            return True
    #电话号码一键登录
    def authsdk_login(self):
        logging.info('==== authsdk_login ====')
        try:
            self.driver.find_element(*self.btn_set)
        except NoSuchElementException:
            logging.error('start authsdk_login!')
            self.driver.find_element(*self.btn_authsdk_login).click()
            return False
        else:
            logging.info('already logged')
            return True



