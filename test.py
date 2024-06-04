# Chrome driver_autoinstaller selenium을 사용하기 위해서는 최신버전의 chrome_driver가 필수 (https://trading-for-chicken.tistory.com/19)
import chromedriver_autoinstaller as AutoChrome
AutoChrome.install(True)

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.current_url
driver.get("https://arena.co.kr/product/list.html?cate_no=32")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(6)  # pause to allow loading of content
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # compare new height with the last height
        break
    last_height = new_height

driver.find_elements_by_css("ul.prdList > li.each_product")     
driver.find_elements_by_css("ul.prdList > li.each_product > div > a")