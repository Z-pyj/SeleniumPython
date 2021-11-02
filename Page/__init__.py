from selenium.webdriver.common.by import By  # selenium原生定位策略集

'''
手机设置页面
'''
# 搜索框
search_button_before = (By.ID, "android:id/input")
# 输入框
search_button_after = (By.XPATH, "//*[@class='miui.widget.ClearableEditText']")
# 搜索结果
search_result = (By.XPATH, "//*[contains(@text, 'WLAN 扫描调节')]")
# 取消
search_cancel = (By.XPATH, "//*[contains(@text, '取消')]")
