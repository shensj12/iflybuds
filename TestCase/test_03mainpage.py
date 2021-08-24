from Common.myunit import StartEnd
from BusinessView.mainpageView import MainPageView
import unittest
import logging
from Common.common_fun import Common
from Common import elements


class TestMainpage(StartEnd):
    def test_01_leftconfig_success(self):
        logging.info('MAIN TESTS')
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

    def test_03_check_scanning(self):
        m = MainPageView(self.driver)
        logging.info('==== test_scanning ====')
        # 断言是否进入扫一扫
        self.assertTrue(m.check_scanning())

# =====================================================================================================================
    # audio改变语言和悬浮窗测试
    def test_04_audiorecordingpage_success(self):
        m = MainPageView(self.driver)
        logging.info('==== test_audiorecordingpage ====')
        # 播放喜马拉雅FM
        m.open_ximalaya()
        m.audio_record_action()
        # 断言是否进入录音页面
        self.assertTrue(m.check_recording_page_audio())

    def test_05_audio_change_language_success(self):
        m = MainPageView(self.driver)
        logging.info('==== change language ====')
        m.change_language()
        # 断言成功改变语言
        self.assertTrue(m.check_language_change())

    def test_06_audio_floating_window_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_floating_window====')
        m.start_up_floating_window(elements.Sel_audiorecord)
        # 断言是否成功切换悬浮窗
        self.assertTrue(m.check_floating_window())

    def test_07_audio_over_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_record_complete====')
        # 断言是否成功结束录音
        self.assertTrue(m.check_record_over())
# =====================================================================================================================
    # microphone改变语言和悬浮窗测试
    def test_08_microphonerecordingpage_success(self):
        m = MainPageView(self.driver)
        logging.info('==== test_microphonerecordingpage ====')
        m.microphone_record_action()
        # 断言是否进入录音页面
        self.assertTrue(m.check_recording_page_mic())

    def test_09_microphone_change_language_success(self):
        m = MainPageView(self.driver)
        logging.info('==== change language ====')
        m.change_language()
        # 断言成功改变语言
        self.assertTrue(m.check_language_change())

    def test_10_microphone_floating_window_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_floating_window====')
        m.start_up_floating_window(elements.Sel_Microphonerecord)
        # 断言是否成功切换悬浮窗
        self.assertTrue(m.check_floating_window())

    def test_11_microphone_over_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_record_complete====')
        # 断言是否成功结束录音
        self.assertTrue(m.check_record_over())
# =====================================================================================================================
    # dial改变语言和悬浮窗测试
    def test_12_dialrecordingpage_success(self):
        m = MainPageView(self.driver)
        logging.info('==== test_dialrecordingpage ====')
        m.dial_record_action()
        # 断言是否进入录音页面
        self.assertTrue(m.check_recording_page_dial())

    def test_13_dial_change_language_success(self):
        m = MainPageView(self.driver)
        logging.info('==== change language ====')
        m.change_language()
        # 断言成功改变语言
        self.assertTrue(m.check_language_change())

    def test_14_dial_floating_window_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_floating_window====')
        m.start_up_floating_window(elements.Sel_dialrecord) # 通话时进入app直接开始录音
        # 断言是否成功切换悬浮窗
        self.assertTrue(m.check_floating_window())

    def test_15_dial_over_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_record_complete====')
        # 断言是否成功结束录音
        self.assertTrue(m.check_record_over())
        # 关闭喜马拉雅FM和腾讯会议
        m.close_wemeet()

# ======================================================================================================================
    def test_16_nontrans_audiorecord_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_nontrans_audio====')
        m.turn_off_transtext()
        m.audio_record_action()
        # 断言成功进入录音界面
        self.assertTrue(m.check_nontranstext_audio())

    def test_17_nontrans_audio_over_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_nontrans_audio_over====')
        # 断言录音是否成功结束
        self.assertTrue(m.check_nontrans_record_over(elements.Btn_record_transtext))

    def test_18_transtext_in_record_audio(self):
        logging.info('====test_transtext_in_record_audio====')
        m = MainPageView(self.driver)
        m.transtext_action()
        # 断言是否成功转文字
        self.assertTrue(m.check_record_transtext())

    def test_19_trantext_when_recording_audio(self):
        m = MainPageView(self.driver)
        m.audio_record_action()
        m.transtext_when_recording()
        # 断言录音时切换转文字成功
        self.assertTrue(m.check_change_trans_success())

# ======================================================================================================================
    def test_20_nontrans_microphonerecord_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_nontrans_microphone====')
        m.microphone_record_action()
        # 断言成功进入录音界面
        self.assertTrue(m.check_nontranstext_audio())

    def test_21_nontrans_microphone_over_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_nontrans_microphone_over====')
        # 断言录音是否成功结束
        self.assertTrue(m.check_nontrans_record_over(elements.Btn_record_transtext))

    def test_22_transtext_in_record_microphone(self):
        logging.info('====test_transtext_in_record_microphone====')
        m = MainPageView(self.driver)
        m.transtext_action()
        # 断言是否成功转文字
        self.assertTrue(m.check_record_transtext())

    def test_23_trantext_when_recording_microphone(self):
        m = MainPageView(self.driver)
        m.microphone_record_action()
        m.transtext_when_recording()
        # 断言录音时切换转文字成功
        self.assertTrue(m.check_change_trans_success())

# ======================================================================================================================
    def test_24_nontrans_dialrecord_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_nontrans_dial====')
        m.dial_record_action()
        # 断言成功进入录音界面
        self.assertTrue(m.check_nontranstext_audio())

    def test_25_nontrans_dial_over_success(self):
        m = MainPageView(self.driver)
        logging.info('====test_nontrans_dial_over====')
        # 断言录音是否成功结束
        self.assertTrue(m.check_nontrans_record_over(elements.name_bar))

    def test_26_transtext_in_record_dial(self):
        logging.info('====test_transtext_in_record_dial====')
        m = MainPageView(self.driver)
        m.transtext_action()
        # 断言是否成功转文字
        self.assertTrue(m.check_record_transtext())

    def test_27_trantext_when_recording_dial(self):
        m = MainPageView(self.driver)
        m.driver.back()
        m.driver.start_activity('tws.iflytek.headset', 'tws.iflytek.ui.SplashActivity')
        m.transtext_when_recording()
        # 断言录音时切换转文字成功
        self.assertTrue(m.check_change_trans_success())
        m.turn_off_transtext()
        m.close_wemeet()
        m.stop_ximalaya()
