from base.base import Base

import os
import base64


def pushFile(tag, pc_path, phone_path, driver=None):
    # tag 1:adb 2:appium
    if tag == 1:
        os.system("adb push %s %s" % (pc_path, phone_path))
    if tag == 2:
        with open(pc_path, 'r', encoding='utf-8') as f:
            data = str(base64.b64encode(f.read().encode('utf-8')), 'utf-8')
            driver.push_file(phone_path, data)


if __name__ == '__main__':
    driver = Base.init_driver
    # # appium校验
    # pushFile(tag=2, pc_path="./hello.txt", phone_path="/sdcard", driver=driver)

    # adb 方式校验
    pushFile(tag=1, pc_path="./hello.txt", phone_path="/sdcard")
