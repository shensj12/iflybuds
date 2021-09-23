from Common.common_fun import Common
from Common.myunit import StartEnd
from BusinessView.settingView import SettingView
import logging


class TestSettingpage(StartEnd):
    def test_01_enter_settingpage_success(self):
        logging.info('SETTING TESTS')
        s = SettingView(self.driver)
        logging.info('==== test enter setting page ====')
        s.change_to_setting_page()
        # 断言已切换至设置界面
        self.assertEqual("设置", s.check_page_is_setting())

    def test_02_leftconfig_success(self):
        s = SettingView(self.driver)
        s.change_Left_config()
        # 断言动作设置是否成功被切换
        self.assertTrue(s.check_left_chooseBtn())

    def test_03_rightconfig_success(self):
        s = SettingView(self.driver)
        logging.info('==== test_rightconfig ====')
        s.change_Right_config()
        # 断言动作设置是否成功被切换
        self.assertTrue(s.check_right_chooseBtn())

    def test_04_change_username_success(self):
        s = SettingView(self.driver)
        c = Common(self.driver)
        c.check_crash_s()
        logging.info('====change username ====')
        # 断言改变用户名
        self.assertTrue(s.change_username())

    def test_05_float_view_check(self):
        logging.info('====float view check====')
        s = SettingView(self.driver)
        # 断言录音状态正常
        self.assertTrue(s.check_float_view())

    def test_06_languagechange_success(self):
        s = SettingView(self.driver)
        logging.info('==== test language change ====')
        s.setting_call_record_action()
        # 断言语言是否成功被切换
        self.assertTrue(s.check_language_changed())

    # 白色耳机去除
    # def test_06_check_wakeup_change(self):
    #     s = SettingView(self.driver)
    #     logging.info('==== check wakeup change')
    #     if s.version == Common.Version.WHITE:
    #         s.change_wakeup()
    #         # 断言是否改变语音唤醒选项
    #         self.assertTrue(s.check_wakeup_options())

    # def test_07_webpage_check_success(self):
    #     s = SettingView(self.driver)
    #     logging.info('==== check webpage existence ====')
    #     # 断言各页面存在内容
    #     self.assertTrue(s.check_webpage_exist())

    def test_07_process_check_success(self):
        s = SettingView(self.driver)
        c = Common(self.driver)
        c.check_crash_s()
        logging.info('==== check process existence ====')
        # 断言各页面存在内容
        self.assertTrue(s.check_process_exist())

    # def test_09_dial_existence_check(self):
    #     s = SettingView(self.driver)
    #     logging.info('==== check dial existence ====')
    #     if s.Version == Common.Version.WHITE:
    #         # 断言各页面存在内容
    #         self.assertTrue(s.check_dial_exist())

    def test_08_instructions_image_success(self):
        s = SettingView(self.driver)
        c = Common(self.driver)
        c.check_crash_s()
        logging.info('==== check instructions existence ====')
        # 断言各页面存在内容
        self.assertTrue(s.check_image_exist())

    def test_09_instructions_video_success(self):
        s = SettingView(self.driver)
        c = Common(self.driver)
        c.check_crash_s()
        logging.info('==== check instructions existence ====')
        # 断言各页面存在内容
        self.assertTrue(s.check_video_exist())

    def test_10_fqa_check_success(self):
        s = SettingView(self.driver)
        c = Common(self.driver)
        c.check_crash_s()
        logging.info('==== check fqa existence ====')
        # 断言各页面存在内容
        self.assertTrue(s.check_fqa_exist())

    def test_11_help_check_success(self):
        s = SettingView(self.driver)
        c = Common(self.driver)
        c.check_crash_s()
        logging.info('==== check help existence ====')
        # 断言各页面存在内容
        self.assertTrue(s.check_help_exist())

    def test_12_us_check_success(self):
        s = SettingView(self.driver)
        c = Common(self.driver)
        c.check_crash_s()
        logging.info('==== check us existence ====')
        # 断言页面存在内容
        self.assertTrue(s.check_us_exist())

    def test_13_firmware_check_success(self):
        s = SettingView(self.driver)
        logging.info('==== check firmware existence ====')
        # 断言固件版本存在内容
        self.assertTrue(s.check_us_firmware())

    def test_14_weibo_check_success(self):
        s = SettingView(self.driver)
        logging.info('==== check weibo existence ====')
        # 断言官方微博存在内容
        self.assertTrue(s.check_us_weibo())

    def test_15_official_check_success(self):
        s = SettingView(self.driver)
        logging.info('==== check official existence ====')
        # 断言访问官网存在内容
        self.assertTrue(s.check_us_official())

    def test_16_privacy_check_success(self):
        s = SettingView(self.driver)
        logging.info('==== check privacy existence ====')
        # 断言各页面存在内容
        self.assertTrue(s.check_privacy_exist())

