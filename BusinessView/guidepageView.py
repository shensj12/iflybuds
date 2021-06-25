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
    Btn_confim3=(By.ID,'tws.iflytek.headset:id/permission_confirm')
    Btn_skip=(By.ID,'tws.iflytek.headset:id/permission_cancel')

    # 检查点击超链接《用户服务协议》后页面是否跳转
    def check_servicepage(self):
        logging.info('==== check_servicepage ====')
        try:
            self.driver.find_element(*self.Link_service).click()
            self.driver.find_element(*self.Web_view)
        except NoSuchElementException:
            logging.error('Enter the failure')
            self.getScreenShot('Enter the failure')
            return False
        else:
            logging.info('Enter the success')
            self.driver.find_element(*self.Btn_back).click()
            return True

    #检查点击超链接《隐私政策》后页面是否跳转
    def check_sprivacypage(self):
        logging.info('==== check_sprivacypage ====')
        try:
            self.driver.find_element(*self.Link_privacy).click()
            self.driver.find_element(*self.Web_view)
        except NoSuchElementException:
            logging.error('Enter the failure')
            self.getScreenShot('Enter the failure')
            return False
        else:
            logging.info('Enter the success')
            self.driver.find_element(*self.Btn_back).click()
            return True

    # 点击不同意确认框正常弹出
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