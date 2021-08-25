import logging
from Common.common_fun import Common, NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from Common import elements

class LoginView(Common):
    check_privacy = (By.ID, 'tws.iflytek.headset:id/authsdk_checkbox_view')
    check_privacy_02 = (By.ID, 'tws.iflytek.headset:id/checkbox_layout')
    phonenum_type = (By.ID, 'tws.iflytek.headset:id/input')
    btn_getver = (By.ID, 'tws.iflytek.headset:id/button_tv')
    wechat_btn_outside = (By.ID, 'tws.iflytek.headset:id/login_type_wx')
    wechat_btn_inside = (By.ID, 'tws.iflytek.headset:id/login_wechat')
    btn_set = (By.XPATH,
               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
               '.widget.RelativeLayout/android.widget.LinearLayout['
               '2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/b.b.k.a.c['
               '4]/android.widget.FrameLayout')
    btn_setting_account = (By.ID, 'tws.iflytek.headset:id/setting_account')
    btn_loginout = (By.ID, 'tws.iflytek.headset:id/login_out')
    btn_authsdk_login = (By.ID, 'tws.iflytek.headset:id/authsdk_login_view')
    # 首次登录授权按钮
    btn_location_allow = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    btn_file_allow = (By.ID, 'com.android.permissioncontroller:id/permission_allow_button')
    # 引导页按钮
    btn_next = (By.ID, 'tws.iflytek.headset:id/next')
    # 授权请求-允许访问手机信息
    btn_access = (By.ID, 'tws.iflytek.headset:id/permission_phone_layout')
    btn_device_allow = (By.ID, 'com.android.permissioncontroller:id/permission_allow_button')
    # 微信双开选择
    wechat_btn_android = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.ImageView')

    # 输入手机号码后获取验证码
    def login_action(self, phone_num):
        logging.info('===== login_action =====')
        logging.info('===== check_change_phonenum =====')
        self.allow_privacy()
        self.check_change_phonenum()

        logging.info('Empty notification bar')
        self.swipeDown()
        self.check_deleteBtn()

        logging.info('phonenumber is:%s' % phone_num)
        self.driver.find_element(*self.phonenum_type).send_keys(phone_num)

    def get_ver(self):
        logging.info('click vergetBtn')
        self.driver.find_element(*self.btn_getver).click()

    # 检查是否发送了验证码
    def check_verificationStatus(self):
        logging.info('check verificationStatus')
        sleep(10)
        try:
            self.driver.find_element(*self.phonenum_type)
        except NoSuchElementException:
            logging.info('get verificationcode  success!')
            self.get_verificationcode()
            return True
        else:
            logging.error('get verificationcode Fail!')
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
        logging.info('verificationcode is' + verificationcode)
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

    # 首次登录后点击允许授权
    def grant(self):
        logging.info('==== Allow the authorized ====')
        logging.info('==== Allow Authorization Locations ====')
        self.driver.find_element(*self.btn_location_allow).click()
        sleep(1)
        self.driver.find_element(*self.btn_file_allow).click()
        sleep(5)

    # APP下载后首次登录检查是否成功登录
    def check_firstlogin(self):
        logging.info('===== check_firstlogin =====')
        try:
            self.driver.find_element(*self.btn_location_allow)
        except NoSuchElementException:
            logging.error('firstlogin Fail!')
            self.getScreenShot('firstlogin fail')
            return False
        else:
            logging.info('firstlogin success!')
            self.grant()
            return True

    # 检查引导页是否正常切换完成
    def check_guidepage_change(self):
        logging.info('===== check_guidepage_change =====')
        try:
            logging.info('==== click btn_next ====')
            self.driver.find_element(*self.btn_next).click()
            sleep(1)
            logging.info('==== Slide the page  ====')
            for i in range(2):
                self.swipeLeft()
                sleep(0.5)
            logging.info('==== click next ====')
            self.driver.find_element(*self.btn_next).click()
            sleep(1)
            logging.info('==== click btn_access ====')
            self.driver.find_element(*self.btn_access).click()
            sleep(1)
            logging.info('==== click btn_device_allow ====')
            self.driver.find_element(*self.btn_device_allow).click()
            sleep(1)
            # 关闭福利广告
            try:
                self.find_element(*elements.close_ad).click()
            except NoSuchElementException:
                pass
            sleep(1)
            self.driver.find_element(*self.btn_set)
        except NoSuchElementException:
            logging.error('guidepage change Fail!')
            self.getScreenShot('guidepage change Fail!')
            return False
        else:
            logging.info('guidepage change success!')
            sleep(1)
            self.cancel_upgrade()
            sleep(1)
            self.logout_action()
            return True

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
        self.allow_privacy()
        try:
            self.driver.find_element(*self.btn_set)
        except NoSuchElementException:
            logging.error('start Wechatlogin!')
            self.driver.find_element(*self.wechat_btn_outside).click()
            self.driver.find_element(*elements.wechat_double_first).click()
            try:
                self.grant()
            except NoSuchElementException:
                pass
            return False
        else:
            logging.info('already logged')
            return True

    # 电话号码一键登录
    def authsdk_login(self):
        logging.info('==== authsdk_login ====')
        try:
            self.driver.find_element(*self.btn_set)
        except NoSuchElementException:
            self.allow_privacy()
            logging.error('start authsdk_login!')
            self.driver.find_element(*self.btn_authsdk_login).click()
            sleep(1)
            return False
        else:
            logging.info('already logged')
            return True

    def allow_privacy(self):
        try:
            self.find_element(*self.check_privacy)
        except NoSuchElementException:
            logging.info('--NO CLICK--')
            pass
        else:
            if self.find_element(*self.check_privacy).get_attribute('checked') == 'false':
                logging.info('--CLICKING--')
                self.find_element(*self.check_privacy).click()
                sleep(1)

    def allow_privacy_02(self):
        try:
            self.find_element(*self.check_privacy_02)
        except NoSuchElementException:
            logging.info('--NO CLICK--')
            pass
        else:
            if self.find_element(*self.check_privacy_02).get_attribute('checked') == 'false':
                logging.info('--CLICKING--')
                self.find_element(*self.check_privacy_02).click()
                sleep(1)