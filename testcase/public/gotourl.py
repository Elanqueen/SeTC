#coding = utf-8
#testcase/public/login.py

import selenium.webdriver
import selenium.webdriver.Firefox
import time

def GotoUrl(url):
    driver=webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get(url)
    return driver
    
    
