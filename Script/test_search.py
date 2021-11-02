import time

from Page.page_setting import Search_Page
from Basic.Get_Driver import GetDriver
from Tools.get_log import GatLog
import Page
from Tools.uitilTools import UitilTools

# 实例化日志对象
log = GatLog.get_log()


class TestSearch:
    def setup_class(self):
        # 初始化driver
        self.driver = GetDriver.init_driver()

    def test_search(self):

        try:
            # 在设置中搜索
            sp = Search_Page(self.driver)
            sp.input_search_text("WALN")
            print(Page.search_result)
            assert False
            # sp.search_cancel()
        except Exception as e:
            UitilTools(self.driver).get_screenshot_file(e)
            raise e

    def teardown_class(self):
        # 结束driver
        log.info("正在结束driver：{}".format(self.driver))
        GetDriver.quit_driver()


if __name__ == '__main__':
    TestSearch().test_search()
