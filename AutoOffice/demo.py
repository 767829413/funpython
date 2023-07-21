# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

try:
    browser.get("https://www.google.com.hk/")
    input = browser.find_element(By.ID, "APjFqb")
    input.send_keys("Python")
    input.send_keys(Keys.ENTER)

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "content_left")))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
    time.sleep(3)
finally:
    browser.close()
