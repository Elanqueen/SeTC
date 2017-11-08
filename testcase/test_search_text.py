#! /usr/bin/env python
#coding=utf-8

import unittest
from testcase.public.gotourl import GotoUrl
from constant.constant import *
import xml.dom.minidom


#打开xml文档
dom = xml.dom.minidom.parse(constant.XML_SEARCH)
#得到文档元素对象
root = dom.documentElement

class testSearchText(unittest.TestCase):
	'''搜索测试'''
    def setup(self):
        self.driver = GotoUrl(constant.LOGIN_URL)

    def test_search_onlytext(self):
        driver=self.driver

        dots = root.getElementByTagName('only_text')
        #获得only_text标签的text属性值
        text=dots[0].getAttribute('text')
    
        #输入搜索内容        
        driver.find_element(pageSearch.txt).clear().sendkeys(text)
        driver.find_element(pageSearch.button).click()

        #获取断言信息进行断言
        page_title=driver.title
        self.assertEqual(page_title,' 	学术资源发现平台 - 腾讯传')

    def teardown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
