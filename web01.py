from selenium import webdriver
import time

from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.get('https://www.baidu.com')
browser.maximize_window()
#LINK_TEXT
'''
browser.find_elements(By.LINK_TEXT,"更多")[0].click()
browser.find_element(By.LINK_TEXT,"更多").click()
'''
#CSS_SELECTOR
#by id : add '#'
'''
browser.find_element(By.CSS_SELECTOR,'#kw').send_keys("selenium")
browser.find_element(By.CSS_SELECTOR,'#su').click()
'''
#by class : add '.'
'''
browser.find_element(By.CSS_SELECTOR,'.s_ipt').send_keys("selenium")
#组合定位
browser.find_element(By.CSS_SELECTOR,'input#su').click()
'''
#by name : [name='']
'''
browser.find_element(By.CSS_SELECTOR,"[name='wd']").send_keys("selenium")
browser.find_element(By.CSS_SELECTOR,"#su").click()
'''
#by tag
'''
#browser.find_element(By.CSS_SELECTOR,'a[href="http://news.baidu.com"]').click()
#browser.find_element(By.CSS_SELECTOR,'a[href="https://wenku.baidu.com/?fr=bdpcindex"]').click()
#模糊匹配-包含
#browser.find_element(By.CSS_SELECTOR,'a[href*="/news.baidu.co"]').click()
#匹配开头
#browser.find_element(By.CSS_SELECTOR,'a[href^="http://news.bai"]').click()
#匹配结尾
#browser.find_element(By.CSS_SELECTOR,'a[href$="s.baidu.com"]').click()
'''
#定位子元素
#browser.find_element(By.CSS_SELECTOR,'div#s-top-left>a').click()
#browser.find_elements(By.CSS_SELECTOR,'div#s-top-left>a')[2].click()
#browser.find_element(By.CSS_SELECTOR,'span.title-content-title').click()
#打开地图
#browser.find_element(By.CSS_SELECTOR,'div#s-top-left>a:nth-child(3)').click()
#打开贴吧
#browser.find_elements(By.CSS_SELECTOR,'div#s-top-left>a')[3].click()
#打开第一项--新闻
browser.find_element(By.CSS_SELECTOR,'div#s-top-left>a:first-child').click()
time.sleep(3)
browser.close()
browser.quit()

