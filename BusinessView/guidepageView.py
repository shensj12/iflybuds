import logging
from Common.common_fun import Common,NoSuchElementException
from Common.desired_caps import  appium_desired
from selenium.webdriver.common.by import By
from time import sleep

class guidepageView(Common):
    # 用户服务协议和隐私政策确认页
    Link_service=(By.LINK_TEXT,'《用户服务协议》')
    Link_privacy=(By.LINK_TEXT,'《隐私政策》')
    Btn_back=(By.ID,'tws.iflytek.headset:id/back')
    Btn_confim=(By.ID,'tws.iflytek.headset:id/privacy_confirm')
    Btn_disagree=(By.ID,'tws.iflytek.headset:id/privacy_exit')
    Web_view=(By.ID,'tws.iflytek.headset:id/web_view')
    # 点击不同意后的确认提示框
    User_tip=(By.ID,'tws.iflytek.headset:id/tv_usertip')
    Btn_exit=(By.ID,'tws.iflytek.headset:id/cancel')
    Btn_confim2=(By.ID,'tws.iflytek.headset:id/comfirm')
    # 获取权限知晓页
    per_layout=(By.ID,'tws.iflytek.headset:id/user_permission_list_layout')
    Btn_confim3=(By.ID,'tws.iflytek.headset:id/permission_confirm')
    Btn_skip=(By.ID,'tws.iflytek.headset:id/permission_cancel')
    # 手机页面中iflybuds图标
    iflbuds = (By.XPATH,'//android.widget.TextView[@content-desc="iFLYBUDS"]')
    # 登录页标题
    btn_title = (By.ID,'tws.iflytek.headset:id/authsdk_title_view')

    # # 检查点击超链接《用户服务协议》后页面是否跳转
    # def check_servicepage(self):
    #     logging.info('==== check_servicepage ====')
    #     try:
    #         self.driver.find_element(*self.Link_service).click()
    #         self.driver.find_element(*self.Web_view)
    #     except NoSuchElementException:
    #         logging.error('Enter the failure')
    #         self.getScreenShot('Enter the failure')
    #         return False
    #     else:
    #         logging.info('Enter the success')
    #         self.driver.find_element(*self.Btn_back).click()
    #         return True
    #
    # #检查点击超链接《隐私政策》后页面是否跳转
    # def check_sprivacypage(self):
    #     logging.info('==== check_sprivacypage ====')
    #     try:
    #         self.driver.find_element(*self.Link_privacy).click()
    #         self.driver.find_element(*self.Web_view)
    #     except NoSuchElementException:
    #         logging.error('Enter the failure')
    #         self.getScreenShot('Enter the failure')
    #         return False
    #     else:
    #         logging.info('Enter the success')
    #         self.driver.find_element(*self.Btn_back).click()
    #         return True


    # 检查确认框正常弹出
    def check_conbx(self):
        logging.info('==== check_conbx ====')
        try:
            self.driver.find_element(*self.Btn_disagree).click()
            self.driver.find_element(*self.User_tip)
        except NoSuchElementException:
            logging.error('Pop-up failure')
            self.getScreenShot('Pop-up failure')
            return False
        else:
            logging.info('Pop-up success')
            return True
    # 检查APP是否正常退出
    def check_exit(self):
        logging.info('==== check_exit ====')
        try:
            self.driver.find_element(*self.Btn_exit).click()
            sleep(1)
            self.driver.find_element(*self.iflbuds)
        except NoSuchElementException:
            logging.error('exit failure')
            self.getScreenShot('exit failure')
            return False
        else:
            logging.info('exit success')
            return True
    #  点击同意并继续按钮，页面正常跳转
    def check_agree(self):
        logging.info('==== check_agree ====')
        try:
            self.driver.find_element(*self.iflbuds).click()
            sleep(1)
            self.driver.find_element(*self.Btn_confim).click()
            sleep(1)
            self.driver.find_element(*self.per_layout)
        except NoSuchElementException:
            logging.error('agree failure')
            self.getScreenShot('agree failure')
            return False
        else:
            logging.info('agree success')
            return True
    # 检查是否正常跳转到登录页
    def check_peragree(self):
        logging.info('==== check_per_agree ====')
        try:
            self.driver.find_element(*self.Btn_confim3).click()
            self.driver.find_element(*self.btn_title)
        except NoSuchElementException:
            logging.error('per_agree failure')
            self.getScreenShot('per_agree failure')
            return False
        else:
            logging.info('per_agree success')
            return True