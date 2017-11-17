#coding = utf-8
#testcase/public/login.py

from selenium import webdriver
import time

def GotoUrl(url):
    #driver=webdriver.Firefox()
    driver=webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(url)
    return driver
    
    
