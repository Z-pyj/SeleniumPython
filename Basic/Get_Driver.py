from appium import webdriver
from Tools.get_log import GatLog

# 实例化日志对象
log = GatLog.get_log()


class GetDriver:
    # 设置类属性
    driver = None

    # 获取driver
    @classmethod
    def init_driver(cls):
        # 启动参数
        desired_caps = {'platformName': 'Android', 'platformVersion': '11', 'noReset': True, 'deviceName': 'b8b46013',
                        'appPackage': 'com.android.settings', 'appActivity': '.MainSettings',
                        'automationName': 'UIAutomator2', 'unicodeKeyboard': True, 'resetKeyboard': True}
        # 手机驱动对象
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            log.info("正在结束driver:{}".format(cls.driver))
            cls.driver.quit()
            # 注意此处是一个大坑
            cls.driver = None
