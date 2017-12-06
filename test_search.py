#coding=utf-8
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(),"public")))
import constant
from page import pageSearch
from wdencap import SeEncap
import  xml.dom.minidom
import unittest

# 打开xml文档
dom = xml.dom.minidom.parse(constant.XML_SEARCH)
# 得到文档元素对象
root = dom.documentElement

class testSearchText(unittest.TestCase,SeEncap):
    '''搜索测试'''

    def setUp(self):
        self.dr=SeEncap("chrome")
        self.dr.open(constant.LOGIN_URL)

    def test_search_onlytext(self):
        dots = root.getElementsByTagName('only_text')
        # 获得only_text标签的text属性值
        text = dots[0].getAttribute('text')

        # 输入搜索内容
        self.dr.type(pageSearch.txt,text)
        self.dr.click(pageSearch.ggjs)

        # 进行窗口切换
        self.dr.switch_to_new_window()

        # 获取断言信息进行断言
        page_title = self.dr.driver.title
        self.assertEqual(page_title, '学术资源发现平台 - 守望爱情')

    def teardown(self):
        self.dr.driver.quit()
        self.dr.assertEqual([], self.dr.verificationErrors)


if __name__ == '__main__':
    unittest.main()