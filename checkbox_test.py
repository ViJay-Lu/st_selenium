import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Edge()
browser.get('https://www.iviewui.com/view-ui-plus/component/form/checkbox')
browser.maximize_window()

browser.find_element(By.XPATH,"//span[text()='Twitter']").click()
time.sleep(2)
browser.find_element(By.XPATH,"//span[text()='Facebook']").click()
time.sleep(2)
browser.find_element(By.XPATH,"//span[text()='Github']").click()
time.sleep(2)
browser.find_element(By.XPATH,"//span[text()='Snapchat']").click()
time.sleep(2)
browser.find_element(By.XPATH,"//span[text()='香蕉']/preceding-sibling::span/input[@value='香蕉']").click()
time.sleep(2)
browser.find_elements(By.XPATH,"//span[text()='苹果']")[0].click()
time.sleep(2)
browser.find_element(By.XPATH,"//span[text()='西瓜']").click()
time.sleep(2)

browser.close()
browser.quit()
