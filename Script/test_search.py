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


class TestSearch:
    def setup_class(self):
        # 初始化driver
        self.driver = GetDriver.init_driver()


    @pytest.mark.parametrize('test_id,input_text', package_param_data())  # 参数传递三组参数，会运行三次

    def test_search(self, test_id, input_text):

        try:
            # 在设置中搜索
            sp = Search_Page(self.driver)
            allure.attach('输入搜索内容', '输入搜索内容为%s' % input_text)
            sp.input_search_text(input_text)
            allure.attach('点击取消键', '取消搜索')
            sp.search_cancel()
        except Exception as e:
            UitilTools(self.driver).get_screenshot_file(e)
            raise e

    def teardown_class(self):
        # 结束driver
        log.info("正在结束driver：{}".format(self.driver))
        GetDriver.quit_driver()


if __name__ == '__main__':
    TestSearch().test_search()
