# 测试用例执行前后操作配置，封装为StartEnd类
import unittest
from Common.desired_caps import appium_desired
import logging
from time import sleep
import warnings


class StartEnd(unittest.TestCase):
    driver = None

    # 用例执行前执行操作
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        logging.info('====setUp====')
        cls.driver = appium_desired()

    # 用例执行完成后的操作
    @classmethod
    def tearDownClass(cls):
        logging.info('====tearDown====')
        sleep(5)
        cls.driver.close_app()
