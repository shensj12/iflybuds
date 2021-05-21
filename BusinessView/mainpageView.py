import logging
from Common.common_fun import Common,NoSuchElementException
from Common.desired_caps import  appium_desired
from selenium.webdriver.common.by import By
from time import sleep

class MainPageView(Common):
    Left_config = (By.ID,'tws.iflytek.headset:id/left_config')
    Right_config = (By.ID,'tws.iflytek.headset:id/right_config')
    Voice_config = (By.ID,'tws.iflytek.headset:id/voice_layout')
    Btn_back = (By.ID,'tws.iflytek.headset:id/back')

    Sel_start_stop = (By.ID,'tws.iflytek.headset:id/lf_start_stop_lay')
    Sel_nextsong = (By.ID,'tws.iflytek.headset:id/lf_next_lay')
    Sel_presong = (By.ID,'tws.iflytek.headset:id/lf_pre_lay')
    # Sel_voicedial=(By.ID,'tws.iflytek.headset:id/lf_wake_lay') 白
    Sel_System_assistant=(By.ID,'tws.iflytek.headset:id/lf_start_stop_call_record_lay')
    Sel_pat_close = (By.ID,'tws.iflytek.headset:id/lf_close_lay')
    Sel_hang_up = (By.ID,'tws.iflytek.headset:id/lf_hang_up_lay')
    Sel_start_record = (By.ID,'tws.iflytek.headset:id/lf_start_record_lay')
    Sel_phone_close = (By.ID,'tws.iflytek.headset:id/lf_dial_close_lay')

    choose_nextsong = (By.ID,'tws.iflytek.headset:id/lf_next')
    choose_srart_record = (By.ID,'tws.iflytek.headset:id/lf_start_record')
    choose_presong = (By.ID,'tws.iflytek.headset:id/lf_pre')
    choose_hang_up = (By.ID,'tws.iflytek.headset:id/lf_hang_up')

    Btn_hx = (By.ID,'tws.iflytek.headset:id/voice_layout')
    Sel_hxvoicedial = (By.ID,'tws.iflytek.headset:id/app_layout')
    Sel_VoiceAssistant = (By.ID,'tws.iflytek.headset:id/sys_lay')
    Sel_hx_close = (By.ID,'tws.iflytek.headset:id/close_lay')

    Btn_start_record = (By.ID,'tws.iflytek.headset:id/start_btn')
    Sel_audiorecord = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout')
    Sel_tryout = (By.ID,'tws.iflytek.headset:id/positive')
    Sel_notrial = (By.ID,'tws.iflytek.headset:id/cancel')
    Btn_float = (By.ID,'tws.iflytek.headset:id/float_state')
    Allow_float = (By.ID,'tws.iflytek.headset:id/permission_layout')
    Config_get = (By.ID,'android:id/switch_widget')
    Config_back = (By.XPATH,'//android.widget.ImageButton[@content-desc="向上导航"]')
    Btn_change_language = (By.ID,'tws.iflytek.headset:id/language_layout')
    # 外语
    Btn_language_other = (By.ID,'tws.iflytek.headset:id/language_grid_tab_other')
    Btn_english = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[1]')

    Sel_Microphonerecord = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout')
    #中文
    Btn_language_chinese = (By.ID,'tws.iflytek.headset:id/language_grid_tab_cn')
    Btn_putonghua = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.TextView')
    # 结束录音
    Btn_end_record = (By.ID,'tws.iflytek.headset:id/hangup_btn')


    # 对左侧耳机进行设置
    def change_Left_config(self):
        logging.info('==== change Left_config ====')
        self.driver.find_element(*self.Left_config).click()
        sleep(1)
        self.driver.find_element(*self.Sel_nextsong).click()
        self.driver.find_element(*self.Sel_start_record).click()
    # 检查左侧耳机动作是否被成功切换
    def check_left_chooseBtn(self):
        logging.info('==== check_left_chooseBtn ====')
        try:
            self.driver.find_element(*self.choose_nextsong)
            self.driver.find_element(*self.choose_srart_record)
        except NoSuchElementException:
            logging.error('choose  Fail!')
            self.getScreenShot('choose  Fail!')
            self.driver.find_element(*self.Btn_back).click()
            return False
        else:
            logging.info('choose  success!')
            self.driver.find_element(*self.Btn_back).click()
            return True

    #对右侧耳机进行设置
    def change_Right_config(self):
        logging.info('==== change Right_config ====')
        self.driver.find_element(*self.Right_config).click()
        sleep(1)
        self.driver.find_element(*self.Sel_presong).click()
        self.driver.find_element(*self.Sel_hang_up).click()
    # 检查右侧耳机动作是否被成功切换
    def check_right_chooseBtn(self):
        logging.info('==== check_right_chooseBtn ====')
        try:
            self.driver.find_element(*self.choose_presong)
            self.driver.find_element(*self.choose_hang_up)
        except NoSuchElementException:
            logging.error('choose  Fail!')
            self.getScreenShot('choose  Fail!')
            self.driver.find_element(*self.Btn_back).click()
            return False
        else:
            logging.info('choose  success!')
            self.driver.find_element(*self.Btn_back).click()
            return True
    #点击音/视频录音
    def audiorecord_action(self):
        logging.info('==== start audiorecord ====')
        self.driver.find_element(*self.Btn_start_record).click()
        self.driver.find_element(*self.Sel_audiorecord).click()
        self.driver.find_element(*self.Sel_notrial).click()
    # 检查是否进入录音界面
    def check_recording_page(self):
        logging.info('check recording page')
        try:
            self.driver.find_element(*self.Btn_change_language)
        except NoSuchElementException:
            logging.error('audiorecord  Fail!')
            self.getScreenShot('audiorecord  Fail!')
            return False
        else:
            logging.info('audiorecord  success!')
            return True




















