# 测试用例执行前后操作配置，封装为StartEnd类
import unittest
from Common.desired_caps import appium_desired
import logging
from time import sleep

class StartEnd(unittest.TestCase):
    # 用例执行前执行操作
    def setUp(self):
        logging.info('====setUp====')
        self.driver=appium_desired()
    # 用例执行完成后的操作
    def tearDown(self):
        logging.info('====tearDown====')
        sleep(5)
        self.driver.close_app()