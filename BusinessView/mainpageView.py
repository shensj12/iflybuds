import logging

from appium.webdriver.common.touch_action import TouchAction

from Common.common_fun import Common, NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from Common import elements


class MainPageView(Common):
    Left_config = (By.ID, 'tws.iflytek.headset:id/left_config')
    Right_config = (By.ID, 'tws.iflytek.headset:id/right_config')
    Voice_config = (By.ID, 'tws.iflytek.headset:id/voice_layout')
    Btn_back = (By.ID, 'tws.iflytek.headset:id/back')
    Btn_IFLYBUDS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout['
                              '2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/b.b.k.a.c['
                              '1]/android.widget.FrameLayout/android.widget.ImageView')

    Sel_start_stop = (By.ID, 'tws.iflytek.headset:id/lf_start_stop_lay')
    Sel_nextsong = (By.ID, 'tws.iflytek.headset:id/lf_next_lay')
    Sel_presong = (By.ID, 'tws.iflytek.headset:id/lf_pre_lay')
    # Sel_voicedial=(By.ID,'tws.iflytek.headset:id/lf_wake_lay') 白
    Sel_System_assistant = (By.ID, 'tws.iflytek.headset:id/lf_start_stop_call_record_lay')
    Sel_pat_close = (By.ID, 'tws.iflytek.headset:id/lf_close_lay')
    Sel_hang_up = (By.ID, 'tws.iflytek.headset:id/lf_hang_up_lay')
    Sel_start_record = (By.ID, 'tws.iflytek.headset:id/lf_start_record_lay')
    Sel_phone_close = (By.ID, 'tws.iflytek.headset:id/lf_dial_close_lay')

    choose_nextsong = (By.ID, 'tws.iflytek.headset:id/lf_next')
    choose_start_record = (By.ID, 'tws.iflytek.headset:id/lf_start_record')
    choose_presong = (By.ID, 'tws.iflytek.headset:id/lf_pre')
    choose_hang_up = (By.ID, 'tws.iflytek.headset:id/lf_hang_up')

    Btn_hx = (By.ID, 'tws.iflytek.headset:id/voice_layout')
    Sel_hxvoicedial = (By.ID, 'tws.iflytek.headset:id/app_layout')
    Sel_VoiceAssistant = (By.ID, 'tws.iflytek.headset:id/sys_lay')
    Sel_hx_close = (By.ID, 'tws.iflytek.headset:id/close_lay')

    Btn_start_record = (By.ID, 'tws.iflytek.headset:id/start_btn')
    Btn_stop_record = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                 '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                                 '2]/android.widget.LinearLayout[2]/android.widget.ImageView')
    Sel_audiorecord = (By.XPATH,
                       '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                       '.FrameLayout[2]/android.widget.LinearLayout')
    Sel_Microphonerecord = (By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                            '.FrameLayout[3]/android.widget.LinearLayout')
    Sel_first_trial = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                 '.LinearLayout')
    Sel_tryout = (By.ID, 'tws.iflytek.headset:id/positive')
    Sel_notrial = (By.ID, 'tws.iflytek.headset:id/cancel')
    Btn_float = (By.ID, 'tws.iflytek.headset:id/float_state')
    Allow_float = (By.ID, 'tws.iflytek.headset:id/permission_layout')
    Config_get = (By.ID, 'android:id/switch_widget')
    Config_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="向上导航"]')

    Check_recording_page = (By.ID, 'tws.iflytek.headset:id/recording_tv')
    Btn_change_language = (By.ID, 'tws.iflytek.headset:id/language_layout')
    # 外语
    Btn_language_other = (By.ID, 'tws.iflytek.headset:id/language_grid_tab_other')
    Btn_english = 'new UiSelector().textContains("英语")'
    # 中文
    Btn_language_chinese = (By.ID, 'tws.iflytek.headset:id/language_grid_tab_cn')
    Btn_putonghua = (By.XPATH,
                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout'
                     '/android.widget.LinearLayout['
                     '2]/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout['
                     '1]/android.widget.TextView')

    Btn_pop_close = (By.ID, 'tws.iflytek.headset:id/pop_close')
    # 结束录音
    Btn_end_record = (By.ID, 'tws.iflytek.headset:id/hangup_btn')

    # 对左侧耳机进行设置
    def change_Left_config(self):
        logging.info('==== change Left_config ====')
        self.driver.find_element(*self.Left_config).click()
        sleep(1)
        self.driver.find_element(*self.Sel_nextsong).click()
        sleep(1)
        self.driver.find_element(*self.Sel_start_record).click()

    # 检查左侧耳机动作是否被成功切换
    def check_left_chooseBtn(self):
        logging.info('==== check_left_chooseBtn ====')
        try:
            self.driver.find_element(*self.choose_nextsong)
            self.driver.find_element(*self.choose_start_record)
        except NoSuchElementException:
            logging.error('choose left Fail!')
            self.getScreenShot('choose left Fail!')
            self.driver.find_element(*self.Btn_back).click()
            return False
        else:
            logging.info('choose left success!')
            self.driver.find_element(*self.Btn_back).click()
            return True

    # 对右侧耳机进行设置
    def change_Right_config(self):
        logging.info('==== change Right_config ====')
        self.driver.find_element(*self.Right_config).click()
        sleep(1)
        self.driver.find_element(*self.Sel_presong).click()
        sleep(1)
        self.driver.find_element(*self.Sel_hang_up).click()

    # 检查右侧耳机动作是否被成功切换
    def check_right_chooseBtn(self):
        logging.info('==== check_right_chooseBtn ====')
        try:
            self.driver.find_element(*self.choose_presong)
            self.driver.find_element(*self.choose_hang_up)
        except NoSuchElementException:
            logging.error('choose right Fail!')
            self.getScreenShot('choose right Fail!')
            self.driver.find_element(*self.Btn_back).click()
            return False
        else:
            logging.info('choose right success!')
            self.driver.find_element(*self.Btn_back).click()
            return True

    # 点击音/视频录音
    def audio_record_action(self):
        logging.info('==== start audio_record ====')
        self.driver.find_element(*self.Btn_IFLYBUDS).click()
        self.driver.find_element(*self.Btn_start_record).click()
        self.driver.find_element(*self.Sel_audiorecord).click()
        # 是否初次试用
        try:
            self.driver.find_element(*self.Sel_first_trial)
        except NoSuchElementException:
            pass
        else:
            self.driver.find_element(*self.Sel_tryout).click()

    # 点击麦克风录音
    def microphone_record_action(self):
        logging.info('==== start microphone_record ====')
        self.driver.find_element(*self.Btn_IFLYBUDS).click()
        self.driver.find_element(*self.Btn_start_record).click()
        self.driver.find_element(*self.Sel_Microphonerecord).click()
        # 是否初次试用
        try:
            self.driver.find_element(*self.Sel_first_trial)
        except NoSuchElementException:
            pass
        else:
            self.driver.find_element(*self.Sel_notrial).click()

    # 点击通话录音
    def dial_record_action(self):
        logging.info('==== start dial_record ====')
        sleep(2)
        self.driver.back()
        self.find_element(*elements.Desktop_wemeet).click()
        # 腾讯会议可能有广告
        sleep(5)
        self.find_element(*elements.Btn_fast_meeting).click()
        sleep(1)
        self.find_element(*elements.Btn_enter_meeting).click()
        sleep(1)
        try:
            self.find_element(*elements.Having_meeting_end).click()
        except NoSuchElementException:
            pass
        sleep(2)
        self.driver.start_activity('tws.iflytek.headset', 'tws.iflytek.ui.SplashActivity')

    # 检查是否进入录音界面（音视频录音）
    def check_recording_page_audio(self):
        logging.info('==== check recording page ====')
        try:
            self.driver.find_element(*self.Check_recording_page)
        except NoSuchElementException:
            logging.error('audio record  Fail!')
            self.getScreenShot('audio record  Fail!')
            return False
        else:
            logging.info('audio record  success!')
            sleep(1)
            return True

    # 检查是否进入录音界面（麦克风录音）
    def check_recording_page_mic(self):
        logging.info('==== check recording page ====')
        try:
            self.driver.find_element(*self.Check_recording_page)
        except NoSuchElementException:
            logging.error('mic record  Fail!')
            self.getScreenShot('mic record  Fail!')
            sleep(10)
            return False
        else:
            logging.info('mic record  success!')
            sleep(1)
            return True

    # 检查是否进入录音界面(通话录音)
    def check_recording_page_dial(self):
        logging.info('==== check recording page ====')
        # 点击"我知道了"
        try:
            self.find_element(*elements.Btn_iknow).click()
        except NoSuchElementException:
            pass
        try:
            sleep(10)
            self.driver.find_element(*self.Check_recording_page)
        except NoSuchElementException:
            logging.error('dial record  Fail!')
            self.getScreenShot('dial record  Fail!')
            return False
        else:
            logging.info('dial record  success!')

            return True

    def open_ximalaya(self):
        logging.info('start 喜马拉雅FM')
        sleep(1)
        self.driver.back()
        self.find_element(*elements.Desktop_ximalaya).click()
        sleep(10)
        logging.info('click play')
        try:
            self.find_element(*elements.Btn_ximaplay2)
        except NoSuchElementException:
            self.find_element(*elements.Btn_ximaplay).click()
        else:
            self.find_element(*elements.Btn_ximaplay2).click()
        sleep(1)
        self.driver.start_activity('tws.iflytek.headset', 'tws.iflytek.ui.SplashActivity')

    def resume_ximalaya(self):
        return True

    def stop_ximalaya(self):
        logging.info('stop 喜马拉雅FM')
        self.driver.back()
        self.find_element(*elements.Desktop_ximalaya).click()
        self.find_element(*elements.play_bar).click()
        self.find_element(*elements.Btn_pause).click()

    # 检查扫一扫
    def check_scanning(self):
        logging.info('==== check scanning ====')
        self.driver.find_element(*elements.Btn_scan).click()
        try:
            self.driver.find_element(*elements.btn_file_allow).click()
        except NoSuchElementException:
            pass
        try:
            self.driver.find_element(*elements.scan_url)
        except NoSuchElementException:
            logging.error('scanning fail')
            self.getScreenShot("scanning fail")
            self.driver.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info('scanning success')
            self.driver.find_element(*elements.Btn_back).click()
            return True

    # 授权通讯录
    def grant(self):
        try:
            self.find_element(*elements.btn_access).click()
        except NoSuchElementException:
            pass
        else:
            self.find_element(*elements.btn_device_allow).click()
        # 关闭弹窗
        try:
            self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout"
                                              "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                              ".RelativeLayout/android.widget.LinearLayout["
                                              "2]/android.widget.ImageView").click()
        except NoSuchElementException:
            pass

    # 检查未开启自动云备份后录音结束（1.3.5.7。。。次）弹出开启提示框
    def check_auto_cloud_backup(self):
        logging.info("==== check_cloud_backup ====")
        try:
            self.find_element(*elements.Btn_auto_cloud_backup)
        except NoSuchElementException:
            logging.info('==== normal ====')
        else:
            self.find_element(*elements.btn_next).click()

    # 录音界面改变语言
    def change_language(self):
        logging.info('==== change language ====')
        self.find_element(*elements.Btn_change_language).click()
        sleep(2)
        self.find_element(*elements.Btn_sichuanhua).click()
        sleep(15)
        self.driver.find_element(*self.Btn_stop_record).click()
        sleep(1)
        try:
            self.find_element(*elements.name_bar).send_keys("腾讯会议")
            self.find_element(*elements.Title_confirm).click()
        except NoSuchElementException:
            pass
        try:
            self.driver.find_element(*self.Btn_back).click()
        except NoSuchElementException:
            pass
        sleep(1)
        # 第一次通话后通讯录授权
        self.grant()
        # 自动云备份提示框
        self.check_auto_cloud_backup()

    # 检查语言是否成功被改变
    def check_language_change(self):
        try:
            self.driver.find_element(*self.Btn_back).click()
        except NoSuchElementException:
            pass
        try:
            self.find_element(*elements.close_first_record_prompt).click()
        except NoSuchElementException:
            pass
        sleep(2)
        self.find_element(*elements.Btn_setting_menu).click()
        self.swipeUp()
        self.find_element(*elements.Btn_setting_call_record).click()
        sleep(2)
        try:
            self.find_element(*elements.check_sichuanhua)
        except NoSuchElementException:
            logging.error('change language fail')
            self.getScreenShot('change language fail')
            self.find_element(*self.Btn_back).click()
            sleep(1)
            self.find_element(*elements.Btn_recording_menu).click()
            return False
        else:
            logging.info('change language success')
            self.find_element(*elements.Setting_putonghua).click()
            sleep(1)
            self.find_element(*self.Btn_back).click()
            sleep(1)
            self.find_element(*elements.Btn_recording_menu).click()
        # 第一次通话后通讯录授权
        self.grant()
        # 自动云备份提示框
        self.check_auto_cloud_backup()
        return True

    #  悬浮窗
    def start_up_floating_window(self, record_type):
        logging.info('==== use floating window ====')
        try:
            self.driver.find_element(*elements.Btn_IFLYBUDS).click()
            self.driver.find_element(*self.Btn_start_record).click()
            sleep(1)
            self.driver.find_element(*record_type).click()
        except NoSuchElementException:
            pass
        sleep(1)
        self.find_element(*self.Btn_float).click()
        # 授权悬浮窗
        try:
            self.find_element(*elements.Allow_float).click()
        except NoSuchElementException:
            pass
        else:
            self.find_element(*elements.Config_get).click()
            sleep(1)
            self.driver.find_element(*elements.Config_back).click()
            sleep(1)
            self.find_element(*elements.Btn_float).click()

    # 检查悬浮窗是否展开并记录
    def check_floating_window(self):
        sleep(6)
        # 坐标定位-点击悬浮窗停止键
        # 悬浮窗在中下部，悬浮球在框右侧
        TouchAction(self.driver).tap(x=910, y=1460).perform()
        try:
            self.find_element(*elements.name_bar).send_keys("悬浮窗")
            self.find_element(*elements.Title_confirm).click()
        except NoSuchElementException:
            pass
        # 区分说话人
        TouchAction(self.driver).tap(x=536, y=1959).perform()
        sleep(2)
        try:
            self.find_element(*elements.Btn_back).click()
        except NoSuchElementException:
            pass
        # 自动云备份提示框
        self.check_auto_cloud_backup()
        try:
            self.find_element(*elements.Btn_setting_menu)
        except NoSuchElementException:
            logging.error("floating window fail")
            self.getScreenShot("floating window fail")
            self.driver.start_activity('tws.iflytek.headset', 'tws.iflytek.ui.SplashActivity')
            return False
        else:
            logging.info('floating window success')
            # 可能有通讯录授权
            self.grant()

            return True

    # 检查录音是否正常结束
    def check_record_over(self):
        logging.info('====check_record_over====')
        self.check_auto_cloud_backup()
        try:
            self.find_element(*elements.first_record)
        except NoSuchElementException:
            logging.error('record over fail')
            self.getScreenShot('record over fail')
            self.find_element(*elements.Btn_IFLYBUDS).click()
            return False
        else:
            logging.info('record over success')
            self.find_element(*elements.Btn_IFLYBUDS).click()
            return True

    # 打开录音实时转文字
    def turn_open_transtext(self):
        logging.info('====turn open transtext====')
        self.find_element(*elements.Btn_setting_menu).click()
        sleep(1)
        self.find_element(*elements.Btn_setting_call_record).click()
        sleep(1)
        try:
            self.find_element(*elements.Label_putonghua)
        except NoSuchElementException:
            self.find_element(*elements.Btn_simultaneous).click()
        else:
            pass
        sleep(1)
        self.find_element(*elements.Btn_back).click()
        sleep(1)
        self.find_element(*elements.Btn_IFLYBUDS).click()

    # 关闭录音实时转文字
    def turn_off_transtext(self):
        logging.info('====turn off transtext====')
        self.find_element(*elements.Btn_setting_menu).click()
        sleep(1)
        self.find_element(*elements.Btn_setting_call_record).click()
        sleep(1)
        try:
            self.find_element(*elements.Label_putonghua)
        except NoSuchElementException:
            pass
        else:
            self.find_element(*elements.Btn_simultaneous).click()
        sleep(1)
        self.find_element(*elements.Btn_back).click()
        sleep(1)
        self.find_element(*elements.Btn_IFLYBUDS).click()

    # 检查是否成功进入音视频录音
    def check_nontranstext_audio(self):
        logging.info('====check nontranstext audio====')
        try:
            self.find_element(*elements.Btn_transtext)
        except NoSuchElementException:
            logging.error('nontrans audio fail')
            self.getScreenShot('nontrans audio fail')
            return False
        else:
            logging.info('nontrans audio success')
            sleep(20)
            self.find_element(*elements.Btn_stop_record).click()
            return True

    # 检查录音是否正常结束
    def check_nontrans_record_over(self, check):
        logging.info('====check_nontrans_record_over====')
        try:
            self.find_element(*check)
        except NoSuchElementException:
            logging.error('nontrans audio record over fail')
            self.getScreenShot('nontrans audio record over fail')
            return False
        else:
            logging.info('record over success')
            return True

    # 在录音记录内转文字
    def transtext_action(self):
        logging.info('====transtext_action====')
        try:
            self.find_element(*elements.name_bar).send_keys("测试用")
            self.find_element(*elements.Title_confirm).click()
        except NoSuchElementException:
            pass
        sleep(2)
        self.find_element(*elements.play_audio).click()
        sleep(1)
        self.find_element(*elements.Btn_record_transtext).click()
        sleep(1)
        self.find_element(*elements.trans_putonghua).click()
        sleep(1)
        # 区分说话人
        TouchAction(self.driver).tap(x=527, y=2133).perform()
        sleep(6)

    # 检查录音记录转文字是否成功
    def check_record_transtext(self):
        logging.info('====check_record_transtext====')
        try:
            self.find_element(*elements.Btn_record_transtext)
        except NoSuchElementException:
            logging.info('trans success')
            self.find_element(*elements.Btn_back).click()
            return True
        else:
            logging.error('trans fail')
            self.getScreenShot('trans fail')
            return False

    def transtext_when_recording(self):
        logging.info('====transtext when recording====')
        self.find_element(*elements.Btn_transtext).click()
        sleep(1)
        self.find_element(*elements.trans_putonghua).click()
        sleep(1)

    def check_change_trans_success(self):
        try:
            self.find_element(*elements.Btn_change_language)
        except NoSuchElementException:
            logging.error('change trans mode fail')
            self.getScreenShot('change trans mode fail')
            try:
                self.find_element(*elements.Btn_stop_record).click()
                self.find_element(*elements.Btn_back).click()
                self.check_auto_cloud_backup()
            except NoSuchElementException:
                pass
            return False
        else:
            logging.info('change trans mode success')
            try:
                self.find_element(*elements.Btn_stop_record).click()
                try:
                    self.find_element(*elements.name_bar).send_keys('录音时转文字')
                    self.find_element(*elements.Title_confirm).click()
                except NoSuchElementException:
                    pass
                self.find_element(*elements.Btn_back).click()
                self.check_auto_cloud_backup()
            except NoSuchElementException:
                pass
            return True

    def check_finish_record(self):
        try:
            self.find_element(*elements.Btn_stop_record)
        except NoSuchElementException:
            pass
        else:
            self.find_element(*elements.Btn_stop_record).click()
            if self.find_element(*elements.name_bar):
                self.find_element(*elements.Btn_exit).click()
            else:
                pass








