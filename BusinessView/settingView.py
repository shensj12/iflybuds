import logging
from Common.common_fun import Common, NoSuchElementException
from time import sleep
import operator
from Common import elements
import random

class SettingView(Common):
    # 切换至设置页面
    def change_to_setting_page(self):
        logging.info('==== change to setting page ====')
        sleep(3)
        self.cancel_upgrade()
        sleep(1)
        self.driver.find_element(*elements.Btn_setting_menu).click()
        sleep(1)

    # 检查是否已在设置界面
    def check_page_is_setting(self):
        logging.info('==== check this is setting page ====')
        return self.driver.find_element(*elements.Title_text).text

    # 对左侧耳机进行设置
    def change_Left_config(self):
        logging.info('==== change Left_config ====')
        self.driver.find_element(*elements.setting_left_config).click()
        sleep(1)
        self.driver.find_element(*elements.prev_song).click()
        sleep(1)
        self.driver.find_element(*elements.Sel_start_record).click()

    # 检查左侧耳机动作是否被成功切换
    def check_left_chooseBtn(self):
        logging.info('==== check_left_chooseBtn ====')
        try:
            self.driver.find_element(*elements.choose_presong)
            self.driver.find_element(*elements.choose_start_record)
        except NoSuchElementException:
            logging.error('choose  Fail!')
            self.getScreenShot('choose  Fail!')
            self.driver.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info('choose  success!')
            self.driver.find_element(*elements.Btn_back).click()
            return True

    # 对右侧耳机进行设置
    def change_Right_config(self):
        logging.info('==== change Right_config ====')
        self.driver.find_element(*elements.setting_right_config).click()
        sleep(1)
        self.driver.find_element(*elements.prev_song).click()
        sleep(1)
        self.driver.find_element(*elements.Sel_hang_up).click()

    # 检查右侧耳机动作是否被成功切换
    def check_right_chooseBtn(self):
        logging.info('==== check_right_chooseBtn ====')
        try:
            self.driver.find_element(*elements.choose_presong)
            self.driver.find_element(*elements.choose_hang_up)
        except NoSuchElementException:
            logging.error('choose  Fail!')
            self.getScreenShot('choose  Fail!')
            self.driver.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info('choose  success!')
            self.driver.find_element(*elements.Btn_back).click()
            return True

    # 检查录音设置功能
    def check_float_view(self):
        logging.info('==== check record setting ====')
        self.swipeUp()
        self.find_element(*elements.Btn_setting_call_record).click()
        sleep(1)
        self.find_element(*elements.float_view_check).click()
        sleep(1)
        self.find_element(*elements.float_view_check).click()
        sleep(1)
        self.find_element(*elements.float_view_check_question).click()
        try:
            iknow = self.find_element(*elements.float_view_check_iknow)
        except NoSuchElementException:
            logging.error('float view check question fail')
            self.getScreenShot('float view check fail')
            return False
        else:
            logging.info('float view check fail')
            iknow.click()
            return True


    # 点击语种设置进行切换
    def setting_call_record_action(self):
        logging.info("==== change language ====")
        try:
            self.find_element(*elements.Label_putonghua)
        except NoSuchElementException:
            self.find_element(*elements.Btn_simultaneous).click()
        else:
            pass
        self.find_element(*elements.Setting_putonghua).click()

    # 检查语种是否成功被替换
    def check_language_changed(self):
        logging.info('==== check language changed ====')
        try:
            self.driver.find_element(*elements.Check_setting_putonghua)
        except NoSuchElementException:
            logging.error('choose  Fail!')
            self.getScreenShot('choose  Fail!')
            self.driver.find_element(*elements.Btn_back).click()
            self.swipeCodown()
            return False
        else:
            logging.info('choose  success!')
            self.driver.find_element(*elements.Btn_back).click()
            self.swipeCodown()
            return True

    # 检查使用指南图文教程
    def check_instructions_image(self, exist):
        logging.info('====check image instructions====')
        internet_ok = False
        try:
            self.find_element(*elements.Btn_refresh)
            logging.info('REFRESHING...')
        except NoSuchElementException:
            internet_ok = True
        while not internet_ok:
            self.find_element(*elements.Btn_refresh).click()
            sleep(3)
            try:
                self.find_element(*elements.Btn_refresh)
                logging.info('REFRESHING...')
            except NoSuchElementException:
                internet_ok = True
        self.driver.find_element(*elements.Sub_btn_image).click()
        for image in elements.image_list:
            self.driver.find_element(*image).click()
            sleep(1)
            try:
                self.driver.find_element(*elements.check_sub_image)
            except NoSuchElementException:
                exist &= False
                logging.error('No content(Image)')
                self.getScreenShot("No content(Image)")
                self.driver.find_element(*elements.Btn_back).click()
            else:
                logging.info('Exists(Image)')
                self.driver.find_element(*elements.Btn_back).click()

    # 检查使用指南视频教程
    def check_instructions_video(self, exist):
        logging.info('====check video instructions====')
        self.driver.find_element(*elements.Sub_btn_video).click()
        for video in elements.video_list_black:
            self.driver.find_element(*video).click()
            try:
                self.driver.find_element(*elements.check_sub_video)
            except NoSuchElementException:
                exist &= False
                logging.error('No content(video)')
                self.getScreenShot("No content(video)")
                self.driver.find_element(*elements.Btn_back).click()
            else:
                logging.info('Exists(video)')
                self.driver.find_element(*elements.Btn_back).click()

    # 检查常见问题
    def check_fqas(self, exist):
        logging.info('==== check FQAs ====')
        for question in elements.fqa_list:
            self.driver.find_element(*question).click()
            sleep(1)
            try:
                self.driver.find_element(*elements.fqa_check)
            except NoSuchElementException:
                exist &= False
                logging.error('No content fqa')
                self.getScreenShot("No content fqa")
                self.driver.find_element(*elements.Btn_back).click()
            else:
                logging.info('Exists fqa')
                self.driver.find_element(*elements.Btn_back).click()

    # 改名
    def change_username(self):
        logging.info('====change a random name====')
        name = str(random.randint(0, 100))
        try:
            self.find_element(*elements.Btn_telephone).click()
            sleep(1)
            self.find_element(*elements.Btn_nickname).click()
            sleep(1)
            self.find_element(*elements.Btn_back).click()
            sleep(1)
            self.find_element(*elements.Btn_nickname).click()
            sleep(1)
            self.find_element(*elements.nick_name).clear()
            self.find_element(*elements.nick_name).send_keys(name)
            sleep(2)
            self.find_element(*elements.Btn_save).click()
            sleep(1)
            self.driver.find_element(*elements.Btn_back).click()
        except NoSuchElementException:
            logging.error('change name Fail')
            self.getScreenShot("change name Fail")
            return False
        else:
            logging.info('change name Success')
            return True

    def change_wakeup(self):
        logging.info('====change wakeup====')
        self.find_element(*elements.Btn_voice_wakeup).click()
        sleep(1)
        self.find_element(*elements.xiaofei_wakeup).click()

    def check_wakeup_options(self):
        logging.info('====check wakeup====')
        try:
            self.find_element(*elements.check_xiaofei)
        except NoSuchElementException:
            logging.error('Change wakeup Fail')
            self.getScreenShot('Change wakeup Fail')
            self.driver.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info('Change wakeup success')
            self.driver.find_element(*elements.Btn_back).click()
            return True

    # 检查网页版页面中是否为空
    def check_webpage_exist(self):
        logging.info('====check_webpage_exist====')
        self.find_element(*elements.Btn_webpage).click()
        sleep(1)
        try:
            self.find_element(*elements.close_webpage)
        except NoSuchElementException:
            logging.error("No web content")
            self.getScreenShot("No web content")
            self.find_element(*elements.close_webpage).click()
            return False
        else:
            logging.info("Web contents exists")
            logging.info('==== check scanning ====')
            self.driver.find_element(*elements.Btn_scan_page).click()
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
            self.find_element(*elements.close_webpage).click()
            return True

    # 检查进程防关闭页面中是否为空
    def check_process_exist(self):
        logging.info('====check_process_exist====')
        self.swipeUp()
        self.swipeUp()
        self.find_element(*elements.Btn_process).click()
        sleep(1)
        try:
            self.find_element(*elements.check_content_process)
        except NoSuchElementException:
            logging.error("No process content")
            self.getScreenShot("No process content")
            self.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info("Process contents exists")
            self.find_element(*elements.Btn_back).click()
            return True

    # 检查语音拨号页面中是否为空（白）
    def check_dial_exist(self):
        logging.info('====check_dial_exist====')
        self.find_element(*elements.Btn_dial).click()
        sleep(1)
        self.find_element(*elements.Btn_contact_alias).click()
        sleep(1)
        try:
            self.find_element(*elements.check_contact_alias)
        except NoSuchElementException:
            logging.error("No dial content")
            self.getScreenShot("No dial content")
            self.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info("Dial contents exists")
            self.find_element(*elements.Btn_back).click()
            return True

    # 检查使用指南页面图文教程
    def check_image_exist(self):
        logging.info('====check_image_exist====')
        exist = True
        self.find_element(*elements.Btn_instructions).click()
        sleep(1)
        self.check_instructions_image(exist)
        return exist

    # 检查使用指南页面视频教程
    def check_video_exist(self):
        logging.info('====check_video_exist====')
        exist = True
        sleep(1)
        self.check_instructions_video(exist)
        self.find_element(*elements.Btn_back).click()
        return exist

    # 检查常见问题中是否为空
    def check_fqa_exist(self):
        logging.info('====check_fqa_exist====')
        exist = True
        self.find_element(*elements.Btn_FQAs).click()
        sleep(1)
        self.check_fqas(exist)
        self.find_element(*elements.Btn_back).click()
        return exist

    # 检查进程防关闭页面中是否为空
    def check_help_exist(self):
        logging.info('====check_help_exist====')
        self.find_element(*elements.Btn_help).click()
        sleep(1)
        try:
            self.find_element(*elements.check_content_help)
        except NoSuchElementException:
            logging.error("No help content")
            self.getScreenShot("No help content")
            self.find_element(*elements.Btn_help_back).click()
            return False
        else:
            logging.info("Help contents exists")
            self.find_element(*elements.Btn_help_back).click()
            return True

    # 检查关于我们页面中是否为空
    def check_us_exist(self):
        logging.info('====check_us_exist====')
        self.find_element(*elements.Btn_us).click()
        sleep(1)
        try:
            self.find_element(*elements.check_content_us)
        except NoSuchElementException:
            logging.error("No us content")
            self.getScreenShot("No us content")
            self.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info("Us contents exists")
            return True

    # 检查固件版本是否为空
    def check_us_firmware(self):
        self.find_element(*elements.Btn_firmware).click()
        try:
            self.find_element(*elements.check_firmware)
        except NoSuchElementException:
            logging.error('No firmware content')
            self.find_element(*elements.Btn_firmware_back).click()
            return False
        else:
            logging.info('Firmware OK')
            self.find_element(*elements.Btn_firmware_back).click()
            return True

    # 检查官方微博是否为空
    def check_us_weibo(self):
        self.find_element(*elements.Btn_weibo).click()
        try:
            sleep(1)
            self.find_element(*elements.check_weibo)
        except NoSuchElementException:
            logging.error('No weibo content')
            self.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info('weibo OK')
            self.find_element(*elements.Btn_back).click()
            return True

    # 检查访问官网是否为空
    def check_us_official(self):
        self.find_element(*elements.Btn_official).click()
        try:
            sleep(1)
            self.find_element(*elements.check_official)
        except NoSuchElementException:
            logging.error('No official content')
            self.find_element(*elements.Btn_back).click()
            sleep(1)
            self.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info('Official OK')
            sleep(1)
            self.find_element(*elements.Btn_back).click()
            sleep(1)
            self.find_element(*elements.Btn_back).click()
            return True

    # 检查隐私设置页面中是否为空
    def check_privacy_exist(self):
        logging.info('====check_privacy_exist====')
        self.find_element(*elements.Btn_privacy).click()
        sleep(1)
        try:
            self.find_element(*elements.check_privacy)
        except NoSuchElementException:
            logging.error("No privacy content")
            self.getScreenShot("No privacy content")
            self.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info("Privacy contents exists")
            self.find_element(*elements.Btn_back).click()
            return True


