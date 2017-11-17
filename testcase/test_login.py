#coding = utf-8
#testcase/test_login

#导入page.page和constant.constant
import os,sys
root_path = os.path.abspath(os.path.dirname(os.getcwd()))
print(root_path)
sys.path.append(os.path.abspath(os.path.join(root_path,'page')))
print(os.path.abspath(os.path.join(root_path,'page')))
import page 
sys.path.append(os.path.abspath(os.path.join(root_path,'constant')))
import constant
path = os.path.abspath(os.path.join(root_path,'testcase'))
sys.path.append(os.path.abspath(os.path.join(root_path,'public')))
from  public.gotourl import GotoUrl
import public.login_fnc

import unittest
import xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse(constant.XML_LOGIN)
#得到文档元素对象
root = dom.documentElement

class testLogin(unittest.TestCase):
    '''登录测试用例'''
    def setup(self):
        self.driver = GotoUrl(constant.LOGIN_URL)

    def test_login_success(self):
        driver=self.driver

        dots = root.getElementByTagName('success')
        #获得success标签的username、password属性值
        username=dots[0].getAttribute('username')
        password=dots[0].getAttribute('password')

        #输入登录名、密码，实现登录
        login_fnc(driver,username,password)

        #获取断言信息进行断言
        text = driver.finf_element()

    def teardown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
        
        
