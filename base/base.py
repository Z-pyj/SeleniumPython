from appium import webdriver


class Base:
    def Init_driver(self):
        desired_caps = {}
        # 系统
        desired_caps['platformName'] = 'Android'
        # 版本
        desired_caps['platformVersion'] = '11'
        # 设备号
        desired_caps['deviceName'] = 'b8b46013'  # os.system("adb devices") 替换
        # 包名
        desired_caps['appPackage'] = 'com.liinji.liinjias'
        # 启动名
        desired_caps['appActivity'] = '.MainNewActivity'
        # desired_caps['app'] = './xx.apk'
        # 声明手机驱动对象
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return driver


if __name__ == '__main__':
    driver = Base().Init_driver()
    code = driver.page_source
    print(code)
