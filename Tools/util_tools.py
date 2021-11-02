import base64
import os
import time
from Tools.get_log import GatLog
import time

# 实例化日志对象
from Tools.read_data import Read_Data

log = GatLog.get_log()


class UitilTools:

    def __init__(self, driver):
        self.driver = driver
        self.sizes = self.driver.get_window_size()

    def swipeUp(self, t=1000, n=1):
        """向上滑动屏幕"""
        x1 = self.sizes['width'] * 0.5
        y1 = self.sizes['height'] * 0.75
        y2 = self.sizes['height'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, t=1000, n=1):
        """向下滑动屏幕"""
        x1 = self.sizes['width'] * 0.5
        y1 = self.sizes['height'] * 0.25
        y2 = self.sizes['height'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, t=1000, n=1):
        """向左滑动屏幕"""
        x1 = self.sizes['width'] * 0.85
        y1 = self.sizes['height'] * 0.5
        x2 = self.sizes['width'] * 0.15
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t=1000, n=1):
        """向右滑动屏幕"""
        x1 = self.sizes['width'] * 0.25
        y1 = self.sizes['height'] * 0.5
        x2 = self.sizes['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def pushFile(self, pc_path, phone_path, driver=None):
        # tag 1:adb 2:appium
        if self == 1:
            os.system("adb push %s %s" % (pc_path, phone_path))
        if self == 2:
            with open(pc_path, 'r', encoding='utf-8') as f:
                data = str(base64.b64encode(f.read().encode('utf-8')), 'utf-8')
                driver.push_file(phone_path, data)

    def get_screenshot_file(self, e):
        log.info("发生错误:%s，正在截图，请到Image目录下查看".format(self.driver) % e)
        self.driver.get_screenshot_as_file("./Image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
