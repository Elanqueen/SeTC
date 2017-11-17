#! /usr/bin/env python
#coding=utf-8

#导入page.page和constant.constant
import os,sys
root_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(os.path.abspath(os.path.join(root_path,'page')))
import page 
sys.path.append(os.path.abspath(os.path.join(root_path,'constant')))
import constant
path = os.path.abspath(os.path.join(root_path,'testcase'))
sys.path.append(os.path.abspath(os.path.join(root_path,'public')))
from  public.gotourl import GotoUrl

import public.login_fnc
import unittest
from selenium import webdriver
import xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse(constant.XML_SEARCH)
#得到文档元素对象
root = dom.documentElement

class testSearchText(unittest.TestCase):
    '''搜索测试'''
    def setUp(self):
        self.driver = GotoUrl(constant.LOGIN_URL)
        '''
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get(constant.LOGIN_URL)
        #self.driver.get('http://www.baidu.com')'''
        
    def test_search_onlytext(self): 
        driver=self.driver
        dots = root.getElementByTagName('only_text')
        #获得only_text标签的text属性值
        text=dots[0].getAttribute('text')
    
        #输入搜索内容        
        driver.find_element(pageSearch.txt).clear()
        driver.find_element(pageSearch.txt).sendkeys(text)
        driver.find_element(pageSearch.button).click()

        #获取断言信息进行断言
        page_title=driver.title
        self.assertEqual(page_title,' 	学术资源发现平台 - 腾讯传')

    def teardown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
    testSearchText()
