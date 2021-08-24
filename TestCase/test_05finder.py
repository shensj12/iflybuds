from Common.myunit import StartEnd
from BusinessView.finderView import FinderView
import unittest
import logging
from Common.common_fun import Common


class TestFinderPage(StartEnd):

    def test_01_enter_finderpage(self):
        logging.info('>>--------FINDER TESTS---------->')
        logging.info('==== check enter finder page ====')
        f = FinderView(self.driver)
        f.change_to_finder_page()
        # 断言已切换至发现界面
        self.assertEqual("发现", f.check_page_is_finder())

    def test_02_enter_relaxpage(self):
        logging.info('==== test enter relax page ====')
        f = FinderView(self.driver)
        f.enter_relax()
        # 断言已进入放松空间
        self.assertTrue(f.check_in_relaxation())

    def test_03_check_time_off(self):
        logging.info('==== test time off ====')
        f = FinderView(self.driver)
        f.set_time_off()
        # 断言定时关闭存在
        self.assertTrue(f.check_time_off())

    def test_04_swipe_to_sleep_music(self):
        logging.info('====test sleep music====')
        f = FinderView(self.driver)
        f.swipe_to_sleep_music()
        f.change_song()
        # 断言已进入睡眠音乐
        self.assertEqual("睡眠音乐", f.check_in_sleep_music())

    def test_05_swipe_to_meditation(self):
        logging.info('====test meditation====')
        f = FinderView(self.driver)
        f.swipe_to_meditation()
        # 断言已进入冥想时刻
        self.assertEqual("冥想时刻", f.check_in_meditation())

    def test_06_swipe_to_collection(self):
        logging.info('====test collection====')
        f = FinderView(self.driver)
        f.swipe_to_collection()
        # 断言已进入收藏音乐
        self.assertEqual("收藏音乐", f.check_in_collection())

    def test_07_minimise_music(self):
        logging.info('====test minimise music====')
        f = FinderView(self.driver)
        f.minimise_music()
        # 断言音乐成功最小化
        self.assertTrue(f.check_music_minimisation())



    # def test_07_check_voice_dial(self):
    #     logging.info('==== check voice dial ====')
    #     f = FinderView(self.driver)
    #     f.enable_voice_dial()
    #     # 断言是否已启用语音拨号
    #     self.assertTrue(f.check_voicedial_enabled())



