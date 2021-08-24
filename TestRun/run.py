import logging
import sys
import time
import unittest
from HTMLTestRunnerCN import HTMLTestRunner

path = 'G:\\iflybuds'
sys.path.append(path)

test_dir = '../TestCase'
report_dir = '../Report'

# 批量调用用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + ' test_report.html'

with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title='iflybuds测试报告',
                                           description='针对iflybuds2.0.7 Android app 测试报告')
    logging.info('start run test case...')

    runner.run(discover)
