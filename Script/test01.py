import time

from appium import webdriver
from selenium.webdriver.common.by import By

from Tools.swipetool import moveDemo

desired_caps = {}
# 系统
desired_caps['platformName'] = 'Android'
# 版本
desired_caps['platformVersion'] = '11'
# 设备号
desired_caps['deviceName'] = 'b8b46013'  # os.system("adb devices") 替换
# 包名
desired_caps['appPackage'] = 'com.liinji.liinjias.test'
# desired_caps['appPackage'] = 'com.liinji.ppgdeliver'
# 启动名
desired_caps['appActivity'] = 'activity.SplashActivity'
# desired_caps['appActivity'] = 'com.liinji.ppgdeliver.activity.WelcomeActivity'
# 安卓11
desired_caps['automationName'] = 'UIAutomator2'
# desired_caps['app'] = './xx.apk'
# 声明手机驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(2)
moveDemo(driver=driver).swipLeft(1000, 4)
driver.find_element_by_id('guide_now').click()
time.sleep(2)
driver.find_element_by_id('editLoginPhone').send_keys('18352833678')
driver.find_element_by_id('editTextloginPwd').send_keys('123456')
driver.find_element_by_id('register_notice_cb').click()
driver.find_element_by_id('butLogin').click()

time.sleep(4)
driver.tap([(93, 2719), (1347, 2882)], 500)
driver.tap([(93, 2719), (1347, 2882)], 500)
driver.tap([(93, 2719), (1347, 2882)], 500)
time.sleep(2)
driver.quit()
