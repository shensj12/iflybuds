from Common.myunit import StartEnd
from BusinessView.recordingView import RecordingView
import logging

class TestRecordingpage(StartEnd):
    def test_01_change_to_recordingpage(self):
        logging.info('RECORDING TESTS')
        r = RecordingView(self.driver)
        logging.info('==== test change to recording page ====')
        r.change_to_recording_page()
        # 断言已切换至录音记录界面
        self.assertEqual("录音记录", r.check_page_is_recording())

    def test_02_check_empty_record(self):
        r = RecordingView(self.driver)
        logging.info('==== test if record empty ====')
        # 断言是否有记录
        self.assertTrue(r.check_if_empty_record())

    def test_03_check_search_bar(self):
        r = RecordingView(self.driver)
        logging.info('====check search bar====')
        # 断言搜索框存在
        self.assertTrue(r.show_search_bar())

    def test_04_check_enter_record(self):
        r = RecordingView(self.driver)
        logging.info('====check enter record====')
        r.enter_search_case()
        # 断言已进入记录
        self.assertTrue(r.check_in_testcase())

    def test_05_check_content_more_dist(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents dist ====')
        # 断言更多内容是否为空
        self.assertTrue(r.check_more_contents_dist())
    #
    # def test_06_check_more_cancel(self):
    #     r = RecordingView(self.driver)
    #     logging.info('====test check more cancel=====')
    #     # 断言正常关闭更多
    #     self.assertTrue(r.check_more_cancel())

    def test_07_check_content_more_url(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents share url ====')
        # 断言更多内容是否为空
        self.assertTrue(r.check_more_contents_url())

    def test_08_check_share_url(self):
        r = RecordingView(self.driver)
        logging.info('====test share url====')
        r.share_url_wechat()
        # 断言分享成功
        self.assertTrue(r.check_wechat_share())

    def test_09_share_back_success_url(self):
        r = RecordingView(self.driver)
        logging.info('====test url share back====')
        # 断言成功返回
        self.assertTrue(r.share_back())

    def test_10_check_content_more_text(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents share text ====')
        # 断言更多内容是否为空
        self.assertTrue(r.check_more_contents_text())

    def test_11_check_share_text(self):
        r = RecordingView(self.driver)
        logging.info('====test check ')
        r.share_text_wechat()
        # 断言分享成功
        self.assertTrue(r.check_wechat_share())

    def test_12_share_back_success_text(self):
        r = RecordingView(self.driver)
        logging.info('====test text share back====')
        # 断言成功返回
        self.assertTrue(r.share_back())

    def test_13_check_content_more_email(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents share email ====')
        # 断言更多内容是否为空
        self.assertTrue(r.check_more_contents_email())

    def test_14_check_content_more_out(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents share out ====')
        # 断言更多内容是否为空
        self.assertTrue(r.check_more_contents_out())

    def test_15_check_output_audio(self):
        r = RecordingView(self.driver)
        logging.info('====test check output audio====')
        self.assertTrue(r.output_audio())

    def test_16_check_output_text(self):
        r = RecordingView(self.driver)
        logging.info('====test check output text====')
        self.assertTrue(r.output_text())

    def test_17_check_content_more_copyall(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents copyall ====')
        # 断言更多内容是否为空
        self.assertTrue(r.check_more_contents_copyall())

    def test_18_check_content_more_translate(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents translate ====')
        # 断言更多内容是否为空
        self.assertTrue(r.check_more_contents_translate())

    def test_19_check_content_more_origin(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents origin ====')
        # 断言更多内容是否为空
        self.assertTrue(r.check_more_contents_origin())

    def test_20_check_content_more_abstract(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents abstract ====')
        # 断言更多内容是否为空
        self.assertTrue(r.check_more_contents_abstract())

    def test_21_check_share_abst_url(self):
        r = RecordingView(self.driver)
        logging.info('====test check share abst url====')
        r.share_abst_url()
        # 断言分享成功
        self.assertTrue(r.check_wechat_share())

    def test_22_share_back_success_url(self):
        r = RecordingView(self.driver)
        logging.info('====test url share back====')
        # 断言成功返回
        self.assertTrue(r.share_back_abst())

    def test_23_check_share_abst_text(self):
        r = RecordingView(self.driver)
        logging.info('====test check share abst text====')
        r.share_abst_text()
        self.assertTrue(r.check_wechat_share())

    def test_24_share_back_success_text(self):
        r = RecordingView(self.driver)
        logging.info('====test text share back====')
        # 断言成功返回
        self.assertTrue(r.share_back_abst())

    def test_25_check_output_abst(self):
        r = RecordingView(self.driver)
        logging.info('====test check output abst====')
        # 断言导出成功
        self.assertTrue(r.output_abst())

    def test_26_check_pause_speed(self):
        r = RecordingView(self.driver)
        logging.info('====test pause and speed change====')
        r.check_pause_speed()

    def test_27_check_cloud_upload(self):
        r = RecordingView(self.driver)
        logging.info('==== test cloud upload ====')
        # 断言是否上传云端
        self.assertTrue(r.upload_to_cloud())

    def test_28_check_record_deleted(self):
        r = RecordingView(self.driver)
        logging.info('====check testcase deleted====')
        r.delete_testcase()
        # 断言已经删除测试用记录
        self.assertTrue(r.check_testcase_deleted())

    def test_29_check_cancel_search(self):
        r = RecordingView(self.driver)
        logging.info('==== test cancel search ====')
        # 断言是否取消搜索
        self.assertTrue(r.check_search_cancel())

    def test_30_delete_record_cancel(self):
        r = RecordingView(self.driver)
        logging.info('====test_delete_record_cancel')
        r.delete_record_cancel()

    def test_31_delete_first_record(self):
        r = RecordingView(self.driver)
        logging.info('====test_delete_record====')
        r.delete_record()

    def test_32_change_name_in_record(self):
        r = RecordingView(self.driver)
        logging.info('====test_change_name_in_record====')
        r.change_record_name()

    def test_33_change_name_cancel(self):
        r = RecordingView(self.driver)
        logging.info('====test_change_name_cancel====')
        r.change_record_name_cancel()

    def test_34_check_cloud_updownload_in_record(self):
        r = RecordingView(self.driver)
        logging.info('==== test cloud upload ====')
        r.download_to_cloud_in_record()

    def test_35_check_download_inlist(self):
        r = RecordingView(self.driver)
        logging.info('====test_download_inlist====')
        r.download_inlist()



