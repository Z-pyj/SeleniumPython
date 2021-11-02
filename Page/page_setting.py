from Basic.Base import Base
from selenium.webdriver.common.by import By
import Page


class Search_Page:
    def __init__(self, driver):
        # 传如driver对象
        self.driver = driver
        # 实例化二次封装的类，用到封装好的操作函数
        self.base_object = Base(self.driver)

    def input_search_text(self, text):
        self.base_object.base_click_element(Page.search_button_before)
        self.base_object.base_input_text(Page.search_button_after, text)

    def search_result(self):
        return self.base_object.base_find_element(Page.search_result)

    def search_cancel(self):
        self.base_object.base_click_element(Page.search_cancel)
