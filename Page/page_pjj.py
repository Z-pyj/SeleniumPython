import allure

from Basic.Base import Base
from selenium.webdriver.common.by import By
import Page


class Search_Pjj:
    def __init__(self, driver):
        # 传如driver对象
        self.driver = driver
        # 实例化二次封装的类，用到封装好的操作函数
        self.base_object = Base(self.driver)

    @allure.step('输入用户名')
    def input_login_name(self, name):
        self.base_object.base_input_text(Page.search_button_after, name)
