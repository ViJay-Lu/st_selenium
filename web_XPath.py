import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Edge()
browser.get('https://www.baidu.com')
browser.maximize_window()

#绝对路径定位
#browser.find_element(By.XPATH,"/html/body/div/div/div[3]/a[3]").click()

#browser.find_element(By.XPATH,"//input[@id='kw']").send_keys('selenium')
#browser.find_element(By.XPATH,"//input[@id='su']").click()

#CLASS有多个时，需要全部写上
#browser.find_element(By.XPATH,"//span[@class='s-top-right-text c-font-normal c-color-t s-top-right-new']").click()
#browser.find_element(By.XPATH,"//div[@id='s-top-left']/a[3]").click()

#根据span文本内容定位 （全匹配）
#browser.find_element(By.XPATH,"//span[text()='嫦娥六号月背样品首次展露真容']").click()
#包含匹配
browser.find_element(By.XPATH,"//span[contains(text(),'嫦娥')]").click()

time.sleep(3)
browser.close()
browser.quit()