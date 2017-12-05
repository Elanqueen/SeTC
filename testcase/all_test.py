#coding = utf-8

import smtplib
import unittest
import HTMLTestRunner #引入HTMLTestRunner包
import time,os
from email.mime.text import MIMEText


#======================定义发送邮件================================
def send_mail(file_new):
	#发送邮箱
	mail_from = '发送邮箱'
	#收信箱
	mail_to = '接收邮箱'
	#'jieliuau@isoftstone.com'
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
	smtp.connect('smtp.163.com')
	#用户名密码
	smtp.login('邮箱','密码') #请填写发送用的邮箱和密码（注：提前开通邮箱的SMTP服务）
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

def creatsuite():
	testunit=unittest.TestSuite()
	test_dir = 'D:\Repositories\SeTC\\testcase'
	discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py',top_level_dir=None)
	for test_case in discover:
		print(test_case)
		testunit.addTests(test_case)
	return testunit
   
if __name__ == '__main__':
	 #获取当前时间
	now = time.strftime('%Y-%m-%d %H_%M_%S')
	#定义测试报告存放路径
	testreport = 'D:\Repositories\SeTC\\log\\'
	log_dir = testreport+now+'result.html'
	log_fp = open(log_dir,'wb')
	#定义测试报告
	runner = HTMLTestRunner.HTMLTestRunner(stream=log_fp,title='搜索测试报告',description='用例执行情况')
	alltestnames=creatsuite()
	runner.run(alltestnames)
	log_fp.close()
	send_report(testreport)  #发送报告



    
