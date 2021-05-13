# 该模块封装了一个类:BaseView,该类封装最基本的方法
class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    # 定位
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    # 获取屏幕大小
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动效果
    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)


