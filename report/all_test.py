#coding = utf-8

import smtplib
import unittest
import HTMLTestRunner #引入HTMLTestRunner包
import time,os
from email.mine.text import MIMEText


#======================定义发送邮件================================
def send_mail(file_new):
	#发送邮箱
	mail_from = '2409852189@qq.com'
	#收信箱
	mail_to = 'jieliuau@isoftstone.com'
	#定义正文
	f = open(file_new,'rb')
	mail_body = f.read()
	f.close()
	msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
	#定义标题
	msg['Subject']=u'自动化测试报告'
	#定义发送时间（不定义的可能某些邮件客户端会不显示发送时间）
	msg['date']=time.strftime('%a,%d %b %Y %H:%M:%S %z')
	smtp=smtplib.SMTP()
	#连接SMTP服务器
	smtp.connect('smtp.qq.com')
	#用户名密码
	smtp.login('2409852189@qq.com','spicy000S')
	smtp.sendmail(mail_from,mail_to,msg.as_string())
	smtp.quit()
	print ('email has sent out')

#===========查找测试报告目录，找到最新生成的测试报告文件===========
def send_report(testreport):
	result_dir = testreport
	lists = os.listdir(result_dir)
	lists.sort(key=lambda fn :os.path.getmtime(result_dir+'\\'+fn))
	#print(u'最新测试生成的报告：'+lists[-1])
	#找到最新生成的文件
	file_new = os.path.join(result_dir,lists[-1])
	print(file_new)
	#调用发邮件模块
	send_mail(file_new)

#======================将用例添加到测试套件========================
'''
def creatsuite():
    
    testunit = unittest.TestSuite()
    #定义测试文件查找目录
    test_dir = '.\\testcase'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test_*.py',top_level_dir = None)
    #discover方法筛选出用例，添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunite.addTests(test_case)
	    print(testunit)
    return testunit
'''

def creatsuite():
	testunit=unittest.TestCase()
	testunit.addTest(testSearchText('test_search_onlytext'))
	return testunit

   
if __name__ == '__main__':
	 #获取当前时间
	now = time.strftime('%Y-%m-%d %H:%M:%S')
	#定义测试报告存放路径
	testreport = 'D:\\Python\\Workspace\\SDLabTest\\log'
	log_dir = testreport+now+'result.html'
	log_fp = file(log_dir,'wb')
	#定义测试报告
	runner = HTMLTestRunner.HTMLTestRunner(stream=log_fp,title='搜索测试报告',description='用例执行情况')
	alltestnames=creatsuite()
	runner.run(alltestnames)
	log_fp.close()
	send_report(testreport)  #发送报告



    
