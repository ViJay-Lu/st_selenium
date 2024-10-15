import time
from peewee import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser=webdriver.Edge()
browser.get('https://sahitest.com/demo/selectTest.htm')
browser.maximize_window()

select=Select(browser.find_element(By.ID,'s3Id'))
#根据下拉框下标查找
select.select_by_index(2)
time.sleep(2)
#根据html value找
select.select_by_value("o4val")
time.sleep(2)
#根据网页实际显示值找
select.select_by_visible_text("o3")
time.sleep(2)
browser.close()
browser.quit()