from BaseView.baseView import BaseView
from  Common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv

class Common(BaseView):
    # 微信登录按钮
    wechat_btn = (By.ID,'tws.iflytek.headset:id/login_type_wx')
    # 通知栏中的清空按钮
    btn_delete=(By.ID,"com.android.systemui:id/delete")
    # 切换手机号按钮
    change_phonenum=(By.ID,'tws.iflytek.headset:id/login_type_switch_num')

    # 检查是否登录，如果没登录则进行微信登录
    def check_login(self):
        logging.info("check_login")
        time.sleep(3)
        try:
            wechatBtn = self.find_element(*self.wechat_btn)
        except NoSuchElementException:
            logging.info("needn't login")
        else:
            wechatBtn.click()
            logging.info("login success")


    # 检查通知栏是否存在清空按钮
    def check_deleteBtn(self):
        logging.info("check_deleteBtn")
        try:
            deletelBtn = self.find_element(*self.btn_delete)
        except NoSuchElementException:
            logging.info("no deleteBtn")
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
        return x,y

    # 右向左滑动
    def swipeLeft(self):
        logging.info('swipLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        x2 = int(l[0] * 0.2)
        y1 = int(l[1] * 0.5)
        self.swipe(x1, y1, x2, y1, 1000)

    # 向上滑动
    def swipeUp(self):
        logging.info('swipUp')
        l = self.get_size()
        y1=1
        x1 = int(l[0] * 0.93)
        y2 = int(l[1] * 0.3)
        self.swipe(x1,y2,x1,y1,1000)
    # 通知栏向下滑动
    def swipeDown(self):
        logging.info('swipDown')
        l = self.get_size()
        y1 = 1
        x1 = int(l[0] * 0.93)
        y2 = int(l[1] * 0.8)
        self.swipe(x1, y1, x1, y2,1000)
        logging.info('swipDown success')
    #中间向下滑动
    def swipeCodown(self):
        logging.info('swipCodown')
        l = self.get_size()
        x1 = int(l[0] * 0.93)
        y1 = int(l[1] * 0.3)
        y2 = int(l[1] * 0.9)
        self.swipe(x1, y1, x1, y2,1000)

    # 获取当前时间
    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    # 获取截图
    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png'%(module,time)
        logging.info('get %s screenshot'%module)
        self.driver.get_screenshot_as_file(image_file)

    # 读取csv文件的方法
    def get_csv_data(self,csv_file,line):
        logging.info('=====get_csv_data=====')
        with open(csv_file,'r',encoding='utf-8') as file:
            reader=csv.reader(file)
            # enumerate函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下表，一般用于for循环
            for index,row in enumerate(reader,1):
                if index==line:
                    return row





