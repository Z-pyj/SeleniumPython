import time

import allure
import pytest

from Page.page_setting import Search_Page
from Basic.Get_Driver import GetDriver
from Tools.get_log import GatLog
import Page
from Tools.read_data import package_param_data
from Tools.util_tools import UitilTools

# 实例化日志对象
log = GatLog.get_log()


class TestPjj:
    def setup_class(self):
        # 初始化driver
        self.driver = GetDriver.init_driver()

    def test_home(self):
        try:
            sources = self.driver.page_source
            print(sources)
        except Exception as e:
            UitilTools(self.driver).get_screenshot_file(e)
            raise e

    def teardown_class(self):
        # 结束driver
        GetDriver.quit_driver()


if __name__ == '__main__':
    TestPjj().test_home()
