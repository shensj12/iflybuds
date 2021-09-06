import logging
import operator

from appium.webdriver.common.touch_action import TouchAction

from Common.common_fun import Common, NoSuchElementException
from Common import elements
from time import sleep

class RecordingView(Common):
    # 切换至录音记录界面
    def change_to_recording_page(self):
        logging.info('==== change to recording page ====')
        sleep(3)
        self.cancel_upgrade()
        sleep(1)
        self.driver.find_element(*elements.Btn_recording_menu).click()
        sleep(1)
        self.driver.find_element(*elements.refresh_icon).click()

    # 检查是否已在录音记录界面
    def check_page_is_recording(self):
        logging.info('==== check this is recording page ====')
        return self.driver.find_element(*elements.Img_records).text

    # 检查记录是否为空
    def check_if_empty_record(self):
        logging.info('==== check recording empty or not ====')
        try:
            self.find_element(*elements.first_record)
        except NoSuchElementException:
            logging.error('Empty recording list')
            self.getScreenShot('Empty recording list')
            return False
        else:
            logging.info('Non-empty recording list')
            return True

    # 进入录音记录
    def enter_record(self):
        logging.info('==== enter the first record ====')
        self.find_element(*elements.first_record).click()

    # 检查分享链接
    def check_more_contents_url(self):
        logging.info('==== check contents in MORE ROW ====')
        logging.info('==== check sharing URL ====')
        self.find_element(*elements.Btn_more).click()
        try:
            self.find_element(*elements.Btn_share_url).click()
            self.find_element(*elements.Check_share_url)
        except NoSuchElementException:
            logging.error("No share url")
            self.getScreenShot("No share url")
            return False
        else:
            logging.info("share url success")
            return True

    # 分享链接至微信
    def share_url_wechat(self):
        logging.info('==== share url to wechat ====')
        self.find_element(*elements.Check_share_url).click()
        sleep(1)
        self.find_element(*elements.wechat_double_first).click()
        sleep(1)
        self.find_element(*elements.wechat_forward_first).click()
        sleep(1)
        self.find_element(*elements.wechat_forward_confirm).click()

    # 检查分享是否成功
    def check_wechat_share(self):
        try:
            self.find_element(*elements.back_iflybuds)
        except NoSuchElementException:
            logging.error('share  fail')
            self.getScreenShot('share  fail')
            return False
        else:
            logging.info('share  success')
            return True

    # 返回iflybuds
    def share_back(self):
        self.find_element(*elements.back_iflybuds).click()
        try:
            self.find_element(*elements.Btn_more)
        except NoSuchElementException:
            logging.error('back fail')
            self.getScreenShot('back fail')
            return False
        else:
            logging.info('back success')
            return True

    # 返回iflybuds
    def share_back_abst(self):
        self.find_element(*elements.back_iflybuds).click()
        try:
            self.find_element(*elements.Btn_share)
        except NoSuchElementException:
            logging.error('back fail')
            self.getScreenShot('back fail')
            return False
        else:
            logging.info('back success')
            return True

    # 检查分享文字
    def check_more_contents_text(self):
        logging.info('==== check sharing text ====')
        self.find_element(*elements.Btn_more).click()
        try:
            self.find_element(*elements.Btn_share_text).click()
            self.find_element(*elements.Check_share_text)
        except NoSuchElementException:
            logging.error("No share text")
            self.getScreenShot("No share text")
            return False
        else:
            logging.info("share text success")
            return True

    # 分享文字至微信
    def share_text_wechat(self):
        logging.info('==== share url to wechat ====')
        self.find_element(*elements.Check_share_text).click()
        sleep(1)
        self.find_element(*elements.wechat_double_first).click()
        sleep(1)
        self.find_element(*elements.wechat_forward_first).click()
        sleep(1)
        self.find_element(*elements.wechat_forward_confirm).click()

    # 检查导出
    def check_more_contents_out(self):
        logging.info('==== check sharing out ====')
        self.find_element(*elements.Btn_more).click()
        try:
            self.find_element(*elements.Btn_share_out).click()
            self.find_element(*elements.Check_share_out)
        except NoSuchElementException:
            logging.error("No share out")
            self.getScreenShot("No share out")
            return False
        else:
            logging.info("share out success")
            return True

    # 检查发送邮件
    def check_more_contents_email(self):
        logging.info('==== check sharing email ====')
        self.find_element(*elements.Btn_more).click()
        try:
            self.find_element(*elements.Btn_share_email).click()
            self.find_element(*elements.Check_share_email)
        except NoSuchElementException:
            logging.error("No share email")
            self.getScreenShot("No share email")
            self.find_element(*elements.Check_share_email).click()
            return False
        else:
            logging.info("share email success")
            self.find_element(*elements.Check_share_email).click()
            return True

    # 导出音频
    def output_audio(self):
        self.find_element(*elements.Check_share_audio).click()
        try:
            self.find_element(*elements.Btn_cancel).click()
        except NoSuchElementException:
            return False
        else:
            return True

    # 导出文字
    def output_text(self):
        self.find_element(*elements.Btn_more).click()
        sleep(1)
        self.find_element(*elements.Btn_share_out).click()
        sleep(1)
        self.find_element(*elements.Check_share_out).click()
        try:
            self.find_element(*elements.Btn_cancel).click()
        except NoSuchElementException:
            return False
        else:
            return True

    # 检查区分说话人
    def check_more_contents_dist(self):
        logging.info('==== check contents in MORE ROW ====')
        logging.info('====区分说话人====')
        self.find_element(*elements.Btn_more).click()
        self.find_element(*elements.more_col_01).click()
        try:
            # 开始分析
            TouchAction(self.driver).tap(x=534, y=1954).perform()
            # 不需要
            # self.driver.tap([(546, 2136)], 100)
        except NoSuchElementException:
            logging.error('dist Fail')
            self.getScreenShot('dist Fail')
            return False
        else:
            logging.info('dist Success')
            return True

    # 检查原始记录
    def check_more_contents_origin(self):
        logging.info('====查看原始记录====')
        self.find_element(*elements.Btn_more).click()
        self.find_element(*elements.more_col_01).click()
        try:
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                              '/android.widget.FrameLayout/android.widget.RelativeLayout/android'
                                              '.widget.ListView/android.widget.LinearLayout')
        except NoSuchElementException:
            logging.error('search origin Fail')
            self.getScreenShot('search origin Fail')
            self.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info('search origin Success')
            self.find_element(*elements.Btn_back).click()
            return True

    # 检查翻译
    def check_more_contents_translate(self):
        logging.info('====翻译====')
        self.find_element(*elements.Btn_more).click()
        self.find_element(*elements.more_col_03).click()
        sleep(3)
        try:
            self.driver.find_element_by_id('tws.iflytek.headset:id/left_text')
        except NoSuchElementException:
            logging.error('translate fail')
            self.getScreenShot('translate fail')
            self.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info('translate success')
            self.find_element(*elements.Btn_back).click()
            return True

    # 检查复制全部
    def check_more_contents_copyall(self):
        logging.info('====复制全部====')
        self.find_element(*elements.Btn_more).click()
        self.find_element(*elements.more_col_04).click()
        try:
            self.find_element(*elements.Btn_more)
        except NoSuchElementException:
            logging.error('copy fail')
            self.getScreenShot('copy fail')
            return False
        else:
            logging.info('copy success')
            return True

    # 检查查看摘要
    def check_more_contents_abstract(self):
        logging.info('====查看摘要====')
        self.find_element(*elements.Btn_more).click()
        self.find_element(*elements.more_col_05).click()
        try:
            self.driver.find_element_by_id('tws.iflytek.headset:id/content')
        except NoSuchElementException:
            logging.error('abstract fail')
            self.getScreenShot('abstract fail')
            return False
        else:
            logging.info('abstract success')
            # self.find_element(*elements.Btn_back).click()
            return True

    # 分享摘要链接
    def share_abst_url(self):
        logging.info('====share abst url====')
        self.find_element(*elements.Btn_share).click()
        sleep(1)
        self.find_element(*elements.abst_share_url).click()
        sleep(1)
        self.find_element(*elements.Check_share_url).click()
        sleep(1)
        self.find_element(*elements.wechat_double_first).click()
        sleep(1)
        self.find_element(*elements.wechat_forward_first).click()
        sleep(1)
        self.find_element(*elements.wechat_forward_confirm).click()

    # 分享摘要文字
    def share_abst_text(self):
        logging.info('====share abst text====')
        self.find_element(*elements.Btn_share).click()
        sleep(1)
        self.find_element(*elements.abst_share_text).click()
        sleep(1)
        self.find_element(*elements.Check_share_text).click()
        sleep(1)
        self.find_element(*elements.wechat_double_first).click()
        sleep(1)
        self.find_element(*elements.wechat_forward_first).click()
        sleep(1)
        self.find_element(*elements.wechat_forward_confirm).click()

    # 导出摘要
    def output_abst(self):
        logging.info('====output abstract====')
        self.find_element(*elements.Btn_share).click()
        sleep(1)
        self.find_element(*elements.abst_output).click()
        sleep(1)
        try:
            self.find_element(*elements.Btn_cancel).click()
        except NoSuchElementException:
            logging.error('output fail')
            self.getScreenShot('output fail')
            self.find_element(*elements.Btn_back).click()
            return False
        else:
            logging.info('output success')
            self.find_element(*elements.Btn_back).click()
            return True

    # 删除云端
    def delete_uploaded(self):
        deleted = self.find_element(*elements.first_record)
        TouchAction(self.driver).long_press(deleted).perform()
        sleep(1)
        try:
            keep = self.find_element(*elements.keep_cloud_delete)
        except NoSuchElementException:
            self.find_element(*elements.Btn_cancel).click()
        else:
            keep.click()
            sleep(1)
            self.find_element(*elements.Btn_confirm).click()

    # 上传云端
    def upload_to_cloud(self):
        logging.info('==== upload to cloud ====')
        sleep(1)
        self.find_element(*elements.Btn_more).click()
        # Wi-Fi
        try:
            self.find_element(*elements.more_col_02).click()
        except NoSuchElementException:
            logging.error('upload Fail')
            self.getScreenShot('upload Fail')
            return False
        else:
            try:
                self.find_element(*elements.not_wifi_hint)
            except NoSuchElementException:
                # 数据流量
                pass
            else:
                logging.info('upload Success')
                self.find_element(*elements.Btn_confirm).click()
            try:
                self.find_element(*elements.Btn_pop_close).click()
            except NoSuchElementException:
                pass
            return True

    def download_to_cloud_in_record(self):
        self.find_element(*elements.Btn_cloud).click()
        sleep(1)
        self.delete_uploaded()
        self.find_element(*elements.first_record).click()
        sleep(1)
        TouchAction(self.driver).tap(x=515, y=2228).perform() # 下载音频
        sleep(1)
        self.find_element(*elements.Btn_back).click()

    # 确认搜索框
    def show_search_bar(self):
        logging.info('====show search bar====')
        self.find_element(*elements.Btn_search_icon).click()
        try:
            self.find_element(*elements.Btn_search)
        except NoSuchElementException:
            logging.error('no search bar')
            self.getScreenShot('no search bar')
            return False
        else:
            logging.info('search bar exists')
            return True

    # 搜索进入测试用记录
    def enter_search_case(self):
        logging.info('====enter_search_case====')
        self.find_element(*elements.Btn_search).click()
        self.find_element(*elements.Btn_search).send_keys('测试用')
        self.find_element(*elements.Btn_search_confirm).click()
        self.find_element(*elements.Btn_search_result).click()

    # 检查是否已进入记录
    def check_in_testcase(self):
        logging.info('====check in testcase====')
        try:
            self.find_element(*elements.Btn_more)
        except NoSuchElementException:
            logging.error('enter testcase fail')
            self.getScreenShot('enter testcase fail')
            return False
        else:
            logging.info("in record")
            return True

    # 删除测试用记录
    def delete_testcase(self):
        self.find_element(*elements.Btn_more).click()
        sleep(1)
        self.find_element(*elements.delete_record).click()
        sleep(1)
        self.find_element(*elements.delete_record_confirm).click()
        sleep(1)

    # 检查是否成功删除测试用记录
    def check_testcase_deleted(self):
        logging.info('====check testcase deleted====')
        self.swipeCodown()
        self.find_element(*elements.Btn_search).send_keys('测试用')
        self.find_element(*elements.Btn_search_confirm).click()
        try:
            self.find_element(*elements.no_search_result)
        except NoSuchElementException:
            logging.error('delete fail')
            self.getScreenShot('delete fail')
            return False
        else:
            logging.info('deleted')
            return True

    # 检查取消搜索
    def check_search_cancel(self):
        logging.info('====check search cancel====')
        try:
            self.find_element(*elements.delete_search).click()
            self.find_element(*elements.Btn_search_confirm).click()
        except NoSuchElementException:
            logging.error('cancel search fail')
            self.getScreenShot('cancel fail')
            return False
        else:
            logging.info('cancel search success')
            return True

    # 检查暂停和倍速
    def check_pause_speed(self):
        logging.info('====check pause and speed====')
        TouchAction(self.driver).tap(x=536, y=2255).perform()
        sleep(1)
        # 倍速
        TouchAction(self.driver).tap(x=718, y=2148).perform()
        sleep(1)
        # 0.5倍
        TouchAction(self.driver).tap(x=243, y=2141).perform()
        sleep(1)
        # 暂停
        TouchAction(self.driver).tap(x=371, y=2153).perform()


    # 详情页改名
    def change_record_name(self):
        self.find_element(*elements.first_record).click()
        sleep(1)
        self.find_element(*elements.record_title).click()
        sleep(1)
        self.find_element(*elements.name_bar).send_keys("改名")
        sleep(1)
        self.find_element(*elements.Title_confirm).click()

    # 详情页改名取消
    def change_record_name_cancel(self):
        self.find_element(*elements.record_title).click()
        sleep(1)
        self.find_element(*elements.Btn_exit).click()
        sleep(1)
        self.find_element(*elements.Btn_back).click()

    # 检查更多关闭键
    def check_more_cancel(self):
        logging.info('====check more cancel')
        sleep(1)
        self.find_element(*elements.Btn_more).click()
        sleep(1)
        self.find_element(*elements.Btn_pop_close).click()
        try:
            self.find_element(*elements.Btn_share_url)
        except NoSuchElementException:
            return True
        else:
            return False

    # 在记录页删除记录
    def delete_record(self):
        deleted = self.find_element(*elements.first_record)
        TouchAction(self.driver).long_press(deleted).perform()
        self.find_element(*elements.Btn_confirm).click()

    def delete_record_cancel(self):
        deleted = self.find_element(*elements.first_record)
        TouchAction(self.driver).long_press(deleted).perform()
        self.find_element(*elements.Btn_cancel).click()

    def download_inlist(self):
        self.delete_uploaded()
        sleep(1)
        self.find_element(*elements.Btn_cloud).click()
        sleep(2)

    def cloud_backup(self):
        try:
            self.find_element(*elements.Btn_cloud_backup)
        except NoSuchElementException:
            logging.info('==== normal ====')
        else:
            logging.info('==== click Btn_later ====')
            self.find_element(*elements.btn_next).click()
