import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Edge()
browser.get('https://www.iviewui.com/view-ui-plus/component/form/cascader')
browser.maximize_window()

browser.find_elements(By.XPATH,"//input[@class='ivu-input ivu-input-default']")[1].click()
time.sleep(2)
browser.find_elements(By.XPATH,"//li[@class='ivu-cascader-menu-item ivu-cascader-menu-item-active']")[0].click()
time.sleep(2)
browser.find_elements(By.XPATH,"//li[@class='ivu-cascader-menu-item ivu-cascader-menu-item-active']")[1].click()
time.sleep(2)
browser.find_elements(By.XPATH,"//li[@class='ivu-cascader-menu-item ivu-cascader-menu-item-active']")[2].click()


time.sleep(2)
browser.close()