# 取值Config-kyb_caps.yaml
from appium import webdriver
import yaml
import logging
import logging.config
import os

# 找到log配置文件
CON_LOG='../Config/log.conf'
# 读取配置文件
logging.config.fileConfig(CON_LOG)
# 读取最新的日志配置文件
logging=logging.getLogger()

def appium_desired():
    # 读取iflybuds.yaml中的数据
    with open('../Config/iflybuds.yaml','r',encoding='utf-8') as file:
        data=yaml.load(file)

    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=str(data['platformVersion'])
    desired_caps['deviceName']=data['deviceName']

    #os.path.dirname(__file__)返回脚本的路径，即文件路径中所在的目录（不包含文件名）
    base_dir = os.path.dirname(os.path.dirname(__file__))
    # os.path.join()连接两个或多个路径名
    app_path = os.path.join(base_dir, 'App', data['appname'])
    desired_caps['app']=app_path

    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    logging.info('start app...')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(8)
    return driver

