from Common.myunit import StartEnd
from BusinessView.recordingView import RecordingView
import logging
from Common.common_fun import Common


class TestRecordingpage(StartEnd):
    def test_01_change_to_recordingpage(self):
        logging.info('RECORDING TESTS')
        r = RecordingView(self.driver)
        r.check_finish_record()
        logging.info('==== test change to recording page ====')
        r.change_to_recording_page()
        # 断言已切换至录音记录界面
        self.assertTrue(r.check_page_is_recording)

    def test_02_check_enter_record(self):
        r = RecordingView(self.driver)
        logging.info('====check enter record====')
        r.enter_search_case()
        # 断言已进入记录
        self.assertTrue(r.check_in_testcase())

    # ============2.4.0新增===============
    def test_03_in_group_select(self):
        r = RecordingView(self.driver)
        logging.info('====check group select====')
        # 断言分组下拉是否正常显示
        self.assertTrue(r.group_select())

    def test_04_in_management_group_page(self):
        r = RecordingView(self.driver)
        logging.info('====check management_group page====')
        # 断言是否进入管理分组页面
        self.assertTrue(r.management_group())

    def test_05_in_create(self):
        r = RecordingView(self.driver)
        logging.info('====check cteate====')
        # 断言是否成功新建分组
        self.assertTrue(r.create())

    def test_06_in_create_cancel(self):
        r = RecordingView(self.driver)
        logging.info('====check cteate cancel====')
        # 断言是否成功取消创建分组
        self.assertTrue(r.create_cancel())

    def test_07_in_rename(self):
        r = RecordingView(self.driver)
        logging.info('====check rename====')
        # 断言是否成功修改名称
        self.assertTrue(r.rename())

    def test_08_in_rename_cancel(self):
        r = RecordingView(self.driver)
        logging.info('====check rename_cancel====')
        # 断言是否成功取消修改名称
        self.assertTrue(r.rename_cancel())

    def test_09_in_rename_delete(self):
        r = RecordingView(self.driver)
        logging.info('====check rename_delete====')
        # 断言是否成功删除分组
        self.assertTrue(r.rename_delete())

    def test_10_title_group_create(self):
        r = RecordingView(self.driver)
        logging.info('====check title_group_create====')
        # 断言是否成功创建分组
        self.assertTrue(r.title_group_create())

    def test_11_title_group_create_cancel(self):
        r = RecordingView(self.driver)
        logging.info('====check title_group_create_cancel====')
        # 断言是否成功取消分组
        self.assertTrue(r.title_group_create_cancel())

    def test_12_check_in_group_choose_success(self):
        r = RecordingView(self.driver)
        logging.info('====check check_group_choose====')
        # 断言是否成功选择分组
        self.assertTrue(r.check_in_group_choose())

    # ===================================================
    # 2.3.0去除
    # def test_05_check_content_more_dist(self):
    #     r = RecordingView(self.driver)
    #     logging.info('==== test contents dist ====')
    #     # 断言更多内容是否为空
    #     self.assertTrue(r.check_more_contents_dist())

    #
    # def test_06_check_more_cancel(self):
    #     r = RecordingView(self.driver)
    #     logging.info('====test check more cancel=====')
    #     # 断言正常关闭更多
    #     self.assertTrue(r.check_more_cancel())

    def test_13_check_content_more_url(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents share url ====')
        # 断言更多内容是否为空
        self.assertTrue(r.check_more_contents_url())

    def test_14_check_share_url(self):
        r = RecordingView(self.driver)
        logging.info('====test share url====')
        r.share_url_wechat()
        # 断言分享成功
        self.assertTrue(r.check_wechat_share())

    def test_15_share_back_success_url(self):
        r = RecordingView(self.driver)
        logging.info('====test url share back====')
        # 断言成功返回
        self.assertTrue(r.share_back())

    def test_16_check_content_more_text(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents share text ====')
        # 断言更多内容是否为空
        self.assertTrue(r.check_more_contents_text())

    def test_17_check_share_text(self):
        r = RecordingView(self.driver)
        logging.info('====test check ')
        r.share_text_wechat()
        # 断言分享成功
        self.assertTrue(r.check_wechat_share())

    def test_18_share_back_success_text(self):
        r = RecordingView(self.driver)
        logging.info('====test text share back====')
        # 断言成功返回
        self.assertTrue(r.share_back())

    # def test_13_check_content_more_email(self):
    #     r = RecordingView(self.driver)
    #     logging.info('==== test contents share email ====')
    #     # 断言更多内容是否为空
    #     self.assertTrue(r.check_more_contents_email())

    def test_19_check_content_more_out(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents share out ====')
        # 断言是否正常导出
        self.assertTrue(r.check_more_contents_out())

    def test_20_check_output_audio(self):
        r = RecordingView(self.driver)
        logging.info('====test check output audio====')
        self.assertTrue(r.output_audio())

    def test_21_check_output_text(self):
        r = RecordingView(self.driver)
        logging.info('====test check output text====')
        self.assertTrue(r.output_text())

    def test_22_check_content_more_copyall(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents copyall ====')
        # 断言全部复制功能是否有效
        self.assertTrue(r.check_more_contents_copyall())

    def test_23_check_content_more_translate(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents translate ====')
        # 断言是否可以正常翻译
        self.assertTrue(r.check_more_contents_translate())

    def test_24_check_content_more_origin(self):
        r = RecordingView(self.driver)
        logging.info('==== test contents origin ====')
        # 断言原始记录页面是否正常跳转
        self.assertTrue(r.check_more_contents_origin())

    def test_25_check_share_abst_url(self):
        r = RecordingView(self.driver)
        logging.info('====test check share abst url====')
        r.share_abst_url()
        # 断言分享成功
        self.assertTrue(r.check_wechat_share())

    def test_26_share_back_success_url(self):
        r = RecordingView(self.driver)
        logging.info('====test url share back====')
        # 断言成功返回
        self.assertTrue(r.share_back_abst())

    def test_27_check_share_abst_text(self):
        r = RecordingView(self.driver)
        logging.info('====test check share abst text====')
        r.share_abst_text()
        self.assertTrue(r.check_wechat_share())

    def test_28_share_back_success_text(self):
        r = RecordingView(self.driver)
        logging.info('====test text share back====')
        # 断言成功返回
        self.assertTrue(r.share_back_abst())

    def test_30_check_pause_speed(self):
        r = RecordingView(self.driver)
        logging.info('====test pause and speed change====')
        r.check_pause_speed()

    def test_31_check_cloud_upload(self):
        r = RecordingView(self.driver)
        logging.info('==== test cloud upload ====')
        # 断言是否上传云端
        self.assertTrue(r.upload_to_cloud())

    def test_32_check_record_deleted(self):
        r = RecordingView(self.driver)
        logging.info('====check testcase deleted====')
        r.delete_testcase()
        # 断言已经删除测试用记录
        self.assertTrue(r.check_testcase_deleted())

    def test_33_check_cancel_search(self):
        r = RecordingView(self.driver)
        c = Common(self.driver)
        c.check_crash_r()
        logging.info('==== test cancel search ====')
        # 断言是否取消搜索
        self.assertTrue(r.check_search_cancel())

    def test_34_delete_record_cancel(self):
        r = RecordingView(self.driver)
        logging.info('====test_delete_record_cancel')
        self.assertTrue(r.delete_record_cancel())

    def test_35_delete_first_record(self):
        r = RecordingView(self.driver)
        logging.info('====test_delete_record====')
        self.assertTrue(r.delete_record())

    def test_36_change_name_cancel(self):
        r = RecordingView(self.driver)
        logging.info('====test_change_name_cancel====')
        r.change_record_name_cancel()

    def test_37_check_cloud_updownload_in_record(self):
        r = RecordingView(self.driver)
        logging.info('==== test cloud upload ====')
        r.download_to_cloud_in_record()

    def test_38_check_download_inlist(self):
        r = RecordingView(self.driver)
        logging.info('====test_download_inlist====')
        r.download_inlist()

    # ===================2.4.0新增=====================

    def test_39_group_select(self):
        r = RecordingView(self.driver)
        logging.info('====check group select====')
        # 断言分组下拉是否正常显示
        self.assertTrue(r.group_select())

    def test_40_management_group_page(self):
        r = RecordingView(self.driver)
        logging.info('====check management_group page====')
        # 断言是否进入管理分组页面
        self.assertTrue(r.management_group())

    def test_41_create(self):
        r = RecordingView(self.driver)
        logging.info('====check cteate====')
        # 断言是否成功新建分组
        self.assertTrue(r.create())

    def test_42_create_cancel(self):
        r = RecordingView(self.driver)
        logging.info('====check cteate cancel====')
        # 断言是否成功取消创建分组
        self.assertTrue(r.create_cancel())

    def test_43_rename(self):
        r = RecordingView(self.driver)
        logging.info('====check rename====')
        # 断言是否成功修改名称
        self.assertTrue(r.rename())

    def test_44_rename_cancel(self):
        r = RecordingView(self.driver)
        logging.info('====check rename_cancel====')
        # 断言是否成功取消修改名称
        self.assertTrue(r.rename_cancel())

    def test_45_rename_delete(self):
        r = RecordingView(self.driver)
        logging.info('====check rename_delete====')
        # 断言是否成功删除分组
        self.assertTrue(r.rename_delete())

    # ================================================
