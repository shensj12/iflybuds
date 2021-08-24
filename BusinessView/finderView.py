import logging

from appium.webdriver.common.touch_action import TouchAction

from Common.common_fun import Common, NoSuchElementException
from Common import elements
from time import sleep


class FinderView(Common):
    # 切换至发现页面
    def change_to_finder_page(self):
        logging.info('==== change to finder page ====')
        sleep(3)
        self.cancel_upgrade()
        sleep(1)
        self.driver.find_element(*elements.Btn_finder_menu).click()

    # 检查是否已在发现界面
    def check_page_is_finder(self):
        logging.info('==== check this is finder page ====')
        return self.driver.find_element(*elements.Title_text).text

    # 启用语音拨号
    def enable_voice_dial(self):
        logging.info('==== enable voice dial ====')
        self.find_element(*elements.Btn_voice_dial).click()
        try:
            self.find_element(*elements.Start_voice_dial).click()
            sleep(1)
            try:
                self.find_element(*elements.Btn_contact_access).click()
                self.find_element(*elements.btn_file_allow).click()
                self.find_element(*elements.btn_file_allow).click()
            except NoSuchElementException:
                pass
            self.find_element(*elements.Btn_start_use).click()
        except NoSuchElementException:
            logging.info('Already enabled')
            self.getScreenShot('Already enabled')
        else:
            logging.info('Enable Success')

    # 检查是否启用语音拨号
    def check_voicedial_enabled(self):
        try:
            self.find_element(*elements.Img_wakeup_style)
        except NoSuchElementException:
            logging.error('wake up Fail')
            self.getScreenShot('wake up Fail')
            self.find_element(*elements.Btn_dial_back).click()
            return False
        else:
            logging.info('wake up Success')
            self.find_element(*elements.Btn_dial_back).click()
            return True

    # 进入放松空间
    def enter_relax(self):
        logging.info('==== relaxation space ====')
        self.driver.find_element(*elements.Btn_relax).click()

    # 检查是否已在放松空间
    def check_in_relaxation(self):
        logging.info('==== check in relaxation ====')
        try:
            self.driver.find_element(*elements.Btn_like).click()
        except NoSuchElementException:
            logging.error('change Fail')
            self.getScreenShot('change Fail')
            return False
        else:
            logging.info('change Success')
            return True

    # 打开定时关闭
    def set_time_off(self):
        logging.info('==== set time off ====')
        self.find_element(*elements.Btn_clock).click()

    # 检查定时关闭时间条
    def check_time_off(self):
        logging.info('====check time off====')
        try:
            self.find_element(*elements.time_bar)
        except NoSuchElementException:
            logging.error('no time bar')
            self.getScreenShot('no time bar')
            self.find_element(*elements.close_time).click()
            return False
        else:
            logging.info('turn off time bar')
            # 滑动调时间
            TouchAction(self.driver).press(x=177, y=2179).move_to(x=954, y=2184).release().perform()
            self.find_element(*elements.close_time).click()
            return True

    # 滑动进入睡眠音乐
    def swipe_to_sleep_music(self):
        logging.info('====swipe_to_sleep_music====')
        self.swipeLeft()
        sleep(1)

    def change_song(self):
        logging.info("==== change song ====")
        self.swipeUp()
        sleep(1)

    # 检查是否已在睡眠音乐
    def check_in_sleep_music(self):
        logging.info('====check_in_sleep_music====')
        return self.find_element(*elements.relax_title).text


    # 滑动进入冥想时刻
    def swipe_to_meditation(self):
        logging.info('====swipe_to_meditation====')
        self.swipeLeft()
        sleep(1)

    # 检查是否已在冥想时刻
    def check_in_meditation(self):
        logging.info('====check_in_meditation====')
        return self.find_element(*elements.relax_title).text

    # 滑动进入收藏音乐
    def swipe_to_collection(self):
        logging.info('====swipe_to_collection====')
        self.swipeLeft()
        sleep(1)

    # 检查是否已在收藏音乐
    def check_in_collection(self):
        logging.info('====check_in_collection====')
        return self.find_element(*elements.relax_title).text

    # 音乐最小化至发现页
    def minimise_music(self):
        logging.info('====minimise music====')
        self.find_element(*elements.Btn_back).click()

    def check_music_minimisation(self):
        try:
            self.find_element(*elements.finder_pause_music)
        except NoSuchElementException:
            logging.error('minimise fail')
            self.getScreenShot('minimise fail')
            return False
        else:
            logging.info('minimise success')
            self.find_element(*elements.finder_pause_music).click()
            sleep(1)
            self.find_element(*elements.close_music_bar).click()
            return True
