import allure

from Basic.Base import Base
from selenium.webdriver.common.by import By
import Page


class Search_Page:
    def __init__(self, driver):
        # 传如driver对象
        self.driver = driver
        # 实例化二次封装的类，用到封装好的操作函数
        self.base_object = Base(self.driver)

    @allure.step('我是测试步骤001')
    def input_search_text(self, text):
        allure.attach('点击输入框', '输入的前置条件')
        self.base_object.base_click_element(Page.search_button_before)
        allure.attach('输入搜索内容', '输入搜索内容为%s' % text)
        self.base_object.base_input_text(Page.search_button_after, text)

    def search_result(self):

        return self.base_object.base_find_element(Page.search_result)

    @allure.step('我是测试步骤002')
    def search_cancel(self):
        allure.attach('点击取消键', '取消搜索')
        self.base_object.base_click_element(Page.search_cancel)
