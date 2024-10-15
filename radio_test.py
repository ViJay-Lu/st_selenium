import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Edge()
browser.get('https://www.iviewui.com/view-ui-plus/component/form/radio')
browser.maximize_window()

#browser.find_elements(By.XPATH, '//span[contains(text(),"Apple")]')[0].click()
#等价于上面，因为页面只能找到两个元素，默认找第一个
#browser.find_element(By.XPATH, '//span[contains(text(),"Apple")]').click()

#跟上面两个找的是同一个元素位置
browser.find_element(By.XPATH, '//span[text()="Apple"]/preceding-sibling::span/input').click()
time.sleep(2)
browser.find_elements(By.XPATH, '//span[contains(text(),"Android")]')[0].click()
time.sleep(2)
browser.find_elements(By.XPATH, '//span[contains(text(),"Windows")]')[0].click()
time.sleep(2)

browser.close()
browser.quit()