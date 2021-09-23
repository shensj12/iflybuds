import logging
import operator
from appium.webdriver.common.touch_action import TouchAction
from Common.common_fun import Common, NoSuchElementException
from Common import elements
from time import sleep
from BusinessView.mainpageView import MainPageView


class RecordingView(Common):
    # 检查未开启自动云备份后录音结束（1.3.5.7。。。次）弹出开启提示框
    def check_auto_cloud_backup(self):
        logging.info("==== check_cloud_backup ====")
        try:
            self.find_element(*elements.Btn_auto_cloud_backup)
        except NoSuchElementException:
            logging.info('==== normal ====')
        else:
            self.find_element(*elements.btn_next).click()

    # 切换至录音记录界面
    def change_to_recording_page(self):
        logging.info('==== change to recording page ====')
        sleep(3)
        self.cancel_upgrade()
        sleep(1)
        self.driver.find_element(*elements.Btn_recording_menu).click()
        sleep(1)
        self.check_auto_cloud_backup()
        sleep(1)
        self.driver.find_element(*elements.refresh_icon).click()

    # 检查是否已在录音记录界面
    def check_page_is_recording(self):
        logging.info('==== check this is recording page ====')
        try:
            self.find_element(*elements.Btn_search_icon)
        except NoSuchElementException:
            logging.info('==== enter the page fail ====')
            return False
        else:
            logging.info('==== enter the page success ====')
            return False

    # 进入录音记录
    def enter_record(self):
        logging.info('==== enter the first record ====')
        self.find_element(*elements.first_record).click()

    # 检查分享链接
    def check_more_contents_url(self):
        logging.info('==== check contents in MORE ROW ====')
        logging.info('==== check sharing URL ====')
        self.find_element(*elements.Btn_more).click()
        sleep(1)
        self.find_element(*elements.Btn_share_url).click()
        try:
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
            self.find_element(*elements.Btn_more)
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

    # # 检查区分说话人
    # def check_more_contents_dist(self):
    #     logging.info('==== check contents in MORE ROW ====')
    #     logging.info('====区分说话人====')
    #     self.find_element(*elements.Btn_more).click()
    #     self.find_element(*elements.more_col_01).click()
    #     try:
    #         # 开始分析
    #         TouchAction(self.driver).tap(x=534, y=1954).perform()
    #         # 不需要
    #         # self.driver.tap([(546, 2136)], 100)
    #     except NoSuchElementException:
    #         logging.error('dist Fail')
    #         self.getScreenShot('dist Fail')
    #         return False
    #     else:
    #         logging.info('dist Success')
    #         return True

    # 检查原始记录
    def check_more_contents_origin(self):
        logging.info('====查看原始记录====')
        self.find_element(*elements.Btn_more).click()
        self.find_element(*elements.more_col_02).click()
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
        self.find_element(*elements.more_col_04).click()
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
        self.find_element(*elements.more_col_05).click()
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
        self.find_element(*elements.more_col_06).click()
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
        self.find_element(*elements.Btn_more).click()
        sleep(1)
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
        self.find_element(*elements.Btn_more).click()
        sleep(1)
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
            self.find_element(*elements.more_col_03).click()
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
        TouchAction(self.driver).tap(x=515, y=2228).perform()  # 下载音频
        sleep(1)
        self.find_element(*elements.Btn_back).click()

    # 搜索进入测试用记录
    def enter_search_case(self):
        logging.info('====enter_search_case====')
        sleep(1)
        logging.info('1')
        # self.find_element(*elements.Btn_search_icon).click()
        # sleep(1)
        logging.info('2')
        self.find_element(*elements.Btn_search).click()
        sleep(1)
        logging.info('3')
        self.find_element(*elements.Btn_search).send_keys('测试用')
        sleep(1)
        self.find_element(*elements.Btn_search_confirm).click()
        sleep(1)
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
        self.find_element(*elements.Btn_search).send_keys('标题栏分组')
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

    # 详情页改名取消
    def change_record_name_cancel(self):
        self.find_element(*elements.first_record).click()
        sleep(1)
        self.find_element(*elements.record_title).click()
        sleep(1)
        self.find_element(*elements.Btn_exit).click()
        try:
            self.find_element(*elements.Btn_exit)
        except NoSuchElementException:
            logging.info('==== cancel success ====')
            self.find_element(*elements.Btn_back).click()
            return True
        else:
            logging.info('==== cancel fail ====')
            self.find_element(*elements.Btn_back).click()
            return False

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
        sleep(2)
        try:
            self.find_element(*elements.Btn_confirm)
        except NoSuchElementException:
            logging.info('==== delete record success ====')
            return True
        else:
            logging.info('==== delete record fail ====')
            return False

    def delete_record_cancel(self):
        deleted = self.find_element(*elements.first_record)
        TouchAction(self.driver).long_press(deleted).perform()
        self.find_element(*elements.Btn_cancel).click()
        try:
            self.find_element(*elements.Btn_confirm)
        except NoSuchElementException:
            logging.info('==== cancel delete success ====')
            return True
        else:
            logging.info('==== cancel delete fail ====')
            return False

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

    # 2.4.0需求
    def group_select(self):
        self.find_element(*elements.Icon_select).click()
        try:
            self.find_element(*elements.Btn_management_group)
        except NoSuchElementException:
            logging.info('==== Drop down failed ====')
            self.getScreenShot('Drop down failed')
            return False
        else:
            logging.info('==== Drop down success ====')
            return True

    def management_group(self):
        self.find_element(*elements.Btn_management_group).click()
        try:
            self.find_element(*elements.Btn_group_create1)
        except NoSuchElementException:
            logging.info('==== enter page fail ====')
            self.getScreenShot('enter page fail')
            return False
        else:
            logging.info('==== enter page success ====')
            return True

    def create(self):
        self.find_element(*elements.Btn_group_create1).click()
        sleep(1)
        self.find_element(*elements.Text_group_name).send_keys('测试')
        sleep(2)
        logging.info('==== click comfirm ====')
        self.find_element(*elements.Btn_group_comfirm).click()
        sleep(1)
        a = self.find_element(*elements.First_group)
        b = a.get_attribute("text")
        if b == "测试":
            logging.info('==== create success ====')
            return True
        else:
            logging.info('==== create fail ====')
            self.getScreenShot('create fail')
            return False

    def create_cancel(self):
        self.find_element(*elements.Btn_group_create1).click()
        sleep(1)
        self.find_element(*elements.Btn_group_cancel).click()
        try:
            self.find_element(*elements.Btn_group_cancel)
        except NoSuchElementException:
            logging.info('==== click btn_cancel success ====')
            return True
        else:
            logging.info('==== click btn_cancel fail ====')
            self.getScreenShot('click btn_cancel fail')
            return False

    def group_press_action(self):
        First_group = self.find_element(*elements.First_group)
        TouchAction(self.driver).long_press(First_group).perform()
        try:
            self.find_element(*elements.Btn_rename)
        except NoSuchElementException:
            logging.info('==== press fail ====')
            self.getScreenShot('press fail')
        else:
            logging.info('==== press success =====')

    def rename(self):
        self.group_press_action()
        sleep(1)
        self.find_element(*elements.Btn_rename).click()
        sleep(1)
        self.find_element(*elements.Text_rename).send_keys('修改名称')
        sleep(2)
        self.find_element(*elements.Btn_group_comfirm).click()
        a = self.find_element(*elements.First_group)
        b = a.get_attribute("text")
        if b == "修改名称":
            logging.info('==== rename success ====')
            return True
        else:
            logging.info('==== rename fail ====')
            self.getScreenShot('rename fail')
            return False

    def rename_cancel(self):
        self.group_press_action()
        sleep(1)
        self.find_element(*elements.Btn_rename).click()
        sleep(1)
        self.find_element(*elements.Btn_group_cancel).click()
        try:
            self.find_element(*elements.Btn_group_cancel)
        except NoSuchElementException:
            logging.info('==== click btn_cancel success ====')
            return True
        else:
            logging.info('==== click btn_cancel fail ====')
            self.getScreenShot('click btn_cancel fail')
            return False

    def rename_delete(self):
        self.group_press_action()
        First_group = self.find_element(*elements.First_group)
        TouchAction(self.driver).long_press(First_group).perform()
        sleep(1)
        self.find_element(*elements.Btn_group_delete).click()
        sleep(1)
        self.find_element(*elements.Btn_confirm).click()
        sleep(1)
        a = self.find_element(*elements.First_group)
        b = a.get_attribute("text")
        if b == "修改名称":
            logging.info('==== delete fail ====')
            self.find_element(*elements.Btn_back).click()
            self.getScreenShot('delete fail')
            return False
        else:
            logging.info('==== delete success ====')
            self.find_element(*elements.Btn_back).click()
            return True

    def title_group_create(self):
        self.find_element(*elements.record_title).click()
        sleep(1)
        self.find_element(*elements.Btn_group_create2).click()
        sleep(1)
        self.find_element(*elements.Text_group_name).send_keys('标题栏分组')
        sleep(2)
        self.find_element(*elements.Btn_group_comfirm).click()
        sleep(1)
        a = self.find_element(*elements.First_group2)
        b = a.get_attribute("text")
        if b == "标题栏分组":
            logging.info('==== create success ====')
            return True
        else:
            logging.info('==== create fail ====')
            self.getScreenShot('create fail ')
            return False

    def title_group_create_cancel(self):
        self.find_element(*elements.Btn_group_create2).click()
        sleep(1)
        self.find_element(*elements.Btn_group_cancel).click()
        try:
            self.find_element(*elements.Btn_group_create2)
        except NoSuchElementException:
            logging.info('==== click btn_cancel fail ====')
            self.getScreenShot('click btn_cancel fail')
            return False
        else:
            logging.info('==== click btn_cancel success ====')
            return True

    def check_in_group_choose(self):
        self.find_element(*elements.Btn_group_comfirm).click()
        sleep(1)
        a = self.find_element(*elements.Title_tip)
        b = a.get_attribute("text")
        if b == "标题栏分组":
            logging.info('==== choose group success ====')
            self.find_element(*elements.Icon_select).click()
            sleep(1)
            self.find_element(*elements.Btn_management_group).click()
            sleep(1)
            First_group = self.find_element(*elements.First_group)
            TouchAction(self.driver).long_press(First_group).perform()
            sleep(1)
            self.find_element(*elements.Btn_group_delete).click()
            sleep(1)
            self.find_element(*elements.Btn_confirm).click()
            sleep(1)
            self.find_element(*elements.Btn_back).click()
            return True
        else:
            logging.info('==== choose group fail ====')
            self.getScreenShot('choose group fail ')
            self.find_element(*elements.Icon_select).click()
            sleep(1)
            self.find_element(*elements.Btn_management_group).click()
            sleep(1)
            First_group = self.find_element(*elements.First_group)
            TouchAction(self.driver).long_press(First_group).perform()
            sleep(1)
            self.find_element(*elements.Btn_group_delete).click()
            sleep(1)
            self.find_element(*elements.Btn_confirm).click()
            sleep(1)
            self.find_element(*elements.Btn_back).click()
            return False

    def check_group_choose(self):
        self.find_element(elements.Icon_select).click()
        sleep(1)
        self.find_element(*elements.Second_group).click()
        a = self.find_element(*elements.Title_tip)
        b = a.get_attribute("text")
        if b == "不删除":
            logging.info('==== choose group success ====')
            return True
        else:
            logging.info('==== choose group fail ====')
            self.getScreenShot('choose group fail ')
            return False

    # ========防止闪退后腾讯会议未关闭，开启app始终在通话录音，无法继续测试

    def check_finish_record(self):
        logging.info('==== check_meeting ====')
        try:
            self.find_element(*elements.Btn_stop_record)
        except NoSuchElementException:
            logging.info('==== not in meeting ====')
            pass
        else:
            logging.info('==== in meeting,start close record and meeting ====')
            self.find_element(*elements.Btn_stop_record).click()
            try:
                self.find_element(*elements.name_bar)
            except NoSuchElementException:
                pass
            else:
                self.find_element(*elements.Btn_exit).click()
                sleep(1)
                self.find_element(*elements.Btn_back).click()
            m = MainPageView(self.driver)
            m.close_wemeet()
            m.stop_ximalaya()
            sleep(1)
            self.driver.start_activity('tws.iflytek.headset', 'tws.iflytek.ui.SplashActivity')