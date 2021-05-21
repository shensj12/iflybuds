from Common.myunit import StartEnd
from BusinessView.mainpageView import MainPageView
import unittest
import logging
from Common.common_fun import Common

class TestMainpage(StartEnd):
    def test_01_leftconfig_success(self):
        c = Common(self.driver)
        m = MainPageView(self.driver)
        logging.info('==== test_leftconfig ====')
        logging.info('==== check login ====')
        c.check_login()
        logging.info('==== test_leftconfig ====')
        m.change_Left_config()
        # 断言动作设置是否成功被切换
        self.assertTrue(m.check_left_chooseBtn())

    def test_02_rightconfig_success(self):
        m = MainPageView(self.driver)
        logging.info('==== test_rightconfig ====')
        m.change_Right_config()
        # 断言动作设置是否成功被切换
        self.assertTrue(m.check_right_chooseBtn())

    def test_03_recordingpage_success(self):
        m = MainPageView(self.driver)
        logging.info('==== test_recordingpage ====')
        m.audiorecord_action()
        # 断言是否进入录音页面
        self.assertTrue(m.check_recording_page())



