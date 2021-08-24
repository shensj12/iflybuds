from Common.myunit import StartEnd
from BusinessView.guidepageView import guidepageView
import logging


class TestGuidepage(StartEnd):
    def test_01_disagreePopup_success(self):
        logging.info('GUIDE TESTS')
        g = guidepageView(self.driver)
        logging.info('==== test_disagreePopup ====')
        # 不同意弹框是否正常弹出
        self.assertTrue(g.check_conbx())

    def test_02_disagree_exit_success(self):
        g = guidepageView(self.driver)
        logging.info('==== test_disagree_exit ====')
        # 断言点击同意退出后APP是否正常退出
        self.assertTrue(g.check_exit())

    def test_03_agree_success(self):
        g = guidepageView(self.driver)
        logging.info('==== test_agree ====')
        # 断言是否进入权限知晓页
        self.assertTrue(g.check_agree())

    def test_04_peragree_success(self):
        g = guidepageView(self.driver)
        logging.info('==== test_peragree ====')
        # 断言是否进入登录页
        self.assertTrue(g.check_peragree())