import csv
import logging
import os
import time
from enum import Enum

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from BaseView.baseView import BaseView
from Common import elements


class Common(BaseView):
    class Version(Enum):
        BLACK = "black"
        WHITE = "white"

    # 微信登录按钮
    wechat_btn = (By.ID, 'tws.iflytek.headset:id/login_type_wx')
    # 通知栏中的清空按钮
    btn_delete = (By.ID, "com.android.systemui:id/delete")
    # 切换手机号按钮
    change_phonenum = (By.ID, 'tws.iflytek.headset:id/login_type_switch_num')
    # 用户隐私
    check_privacy = (By.ID, 'tws.iflytek.headset:id/authsdk_checkbox_view')
    check_privacy_02 = (By.ID, 'tws.iflytek.headset:id/checkbox_layout')

    # 判断版本
    version = ""

    def check_version(self):
        self.find_element(*elements.Btn_setting_menu).click()
        time.sleep(1)
        try:
            self.find_element(*elements.Btn_voice_wakeup)
        except NoSuchElementException:
            logging.info(Common.Version.BLACK)
            self.version = Common.Version.BLACK
        else:
            logging.info(Common.Version.WHITE)
            self.version = Common.Version.WHITE

    # 检查是否登录，如果没登录则进行微信登录
    def check_login(self):
        logging.info("check_login")
        try:
            self.find_element(*elements.btn_set)
        except NoSuchElementException:
            logging.info('start login')
            self.allow_privacy_02()
            time.sleep(1)
            logging.info('click wechat')
            self.find_element(*elements.wechat_btn2).click()
            self.find_element(*elements.wechat_double_first).click()
            logging.info("login success")
        else:
            logging.info("needn't login")
        time.sleep(3)
        self.cancel_upgrade()

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
                time.sleep(1)

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
                time.sleep(1)

    # 检查通知栏是否存在清空按钮
    def check_deleteBtn(self):
        logging.info("check_deleteBtn")
        try:
            deletelBtn = self.find_element(*self.btn_delete)
        except NoSuchElementException:
            logging.info("no deleteBtn")
            self.swipeUp()
            self.swipeUp()
        else:
            deletelBtn.click()

    # 检查是否存在切换手机号按钮
    def check_change_phonenum(self):
        logging.info("check_check_change_phonenum")
        try:
            change_phonenum = self.find_element(*self.change_phonenum)
        except NoSuchElementException:
            logging.info("no change_phonenum")
        else:
            change_phonenum.click()

    # 获取屏幕大小
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 右向左滑动
    def swipeLeft(self):
        logging.info('==== swipeLeft ====')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        x2 = int(l[0] * 0.2)
        y1 = int(l[1] * 0.5)
        self.swipe(x1, y1, x2, y1, 1000)

    # 向上滑动
    def swipeUp(self):
        logging.info('swipeUp')
        l = self.get_size()
        y1 = 1
        x1 = int(l[0] * 0.93)
        y2 = int(l[1] * 0.3)
        self.swipe(x1, y2, x1, y1, 1000)

    # 通知栏向下滑动
    def swipeDown(self):
        logging.info('swipeDown')
        l = self.get_size()
        y1 = 1
        x1 = int(l[0] * 0.93)
        y2 = int(l[1] * 0.8)
        self.swipe(x1, y1, x1, y2, 1000)
        logging.info('swipeDown success')

    # 中间向下滑动
    def swipeCodown(self):
        logging.info('swipeCodown')
        l = self.get_size()
        x1 = int(l[0] * 0.93)
        y1 = int(l[1] * 0.3)
        y2 = int(l[1] * 0.9)
        self.swipe(x1, y1, x1, y2, 1000)

    # 获取当前时间
    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    # 获取截图
    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)
        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    # 读取csv文件的方法
    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data=====')
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            # enumerate函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下表，一般用于for循环
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def cancel_upgrade(self):
        logging.info('====check if upgrade====')
        try:
            self.find_element(*elements.close_upgrade)
        except NoSuchElementException:
            logging.info('No upgrade')
            pass
        else:
            self.find_element(*elements.close_upgrade).click()

    # 关闭腾讯会议
    def close_wemeet(self):
        logging.info('====close wemeet====')
        self.driver.back()
        self.driver.back()
        self.find_element(*elements.Desktop_wemeet).click()
        time.sleep(1)
        try:
            restore = self.find_element(*elements.Btn_restore_cancel)
        except NoSuchElementException:
            pass
        else:
            restore.click()
            time.sleep(1)
        try:
            self.find_element(*elements.Btn_close_meeting).click()
            time.sleep(1)
            self.find_element(*elements.Btn_close_meeting_plus).click()
            time.sleep(1)
        except NoSuchElementException:
            pass
        self.driver.start_activity('tws.iflytek.headset', 'tws.iflytek.ui.SplashActivity')
        time.sleep(1)
        self.cancel_upgrade()

    def check_crash_lm(self):
        logging.info('==== start check crash ====')
        try:
            self.find_element(*elements.iflbuds)
        except NoSuchElementException:
            logging.info('==== in app ====')
            pass
        else:
            logging.info('==== app crash =====')
            logging.info('==== start app ====')
            self.driver.start_activity('tws.iflytek.headset', 'tws.iflytek.ui.SplashActivity')

    def check_crash_lm_r(self):
        logging.info('==== start check crash ====')
        try:
            self.find_element(*elements.iflbuds)
        except NoSuchElementException:
            logging.info('==== in app ====')
            pass
        else:
            logging.info('==== app crash =====')
            logging.info('==== start app ====')
            self.driver.start_activity('tws.iflytek.headset', 'tws.iflytek.ui.SplashActivity')
            time.sleep(1)
            self.find_element(*elements.Btn_stop_record).click()

    def check_crash_r(self):
        logging.info('==== start check crash ====')
        try:
            self.find_element(*elements.iflbuds)
        except NoSuchElementException:
            logging.info('==== in app ====')
            pass
        else:
            logging.info('==== app crash =====')
            logging.info('==== start app ====')
            self.driver.start_activity('tws.iflytek.headset', 'tws.iflytek.ui.SplashActivity')
            time.sleep(10)
            self.find_element(*elements.Btn_recording_menu).click()

    def check_crash_f(self):
        logging.info('==== start check crash ====')
        try:
            self.find_element(*elements.iflbuds)
        except NoSuchElementException:
            logging.info('==== in app ====')
            pass
        else:
            logging.info('==== app crash =====')
            logging.info('==== start app ====')
            self.driver.start_activity('tws.iflytek.headset', 'tws.iflytek.ui.SplashActivity')
            time.sleep(10)
            self.find_element(*elements.Btn_finder_menu).click()

    def check_crash_s(self):
        logging.info('==== start check crash ====')
        try:
            self.find_element(*elements.iflbuds)
        except NoSuchElementException:
            logging.info('==== in app ====')
            pass
        else:
            logging.info('==== app crash =====')
            logging.info('==== start app ====')
            self.driver.start_activity('tws.iflytek.headset', 'tws.iflytek.ui.SplashActivity')
            time.sleep(10)
            self.find_element(*elements.Btn_setting_menu).click()



