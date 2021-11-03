from selenium.webdriver.support.wait import WebDriverWait
from Tools.get_log import GatLog
import time

# 实例化日志对象
log = GatLog.get_log()


class Base(object):
    driver = None

    def __init__(self, driver):
        self.driver = driver
        log.info("初始化driver:{}".format(self.driver))

    def base_find_element(self, loc, timeout=10):
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))

    def base_click_element(self, loc):
        # 封装点击操作
        log.info("正在点击元素：{}".format(loc))
        self.base_find_element(loc).click()

    def base_input_text(self, loc, text):
        # 封装输入操作
        self.fm = self.base_find_element(loc)
        self.fm.clear()  # 需要先清空输入框，防止有默认内容
        log.info("正在输入：{}".format(text))
        self.fm.send_keys(text)


