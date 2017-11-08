
'''
#coding=utf-8
import unittest
#加载测试文件
import testadd
import testsubstraction

suite = unittest.TestSuite()

suite.addTest(testadd.TestAdd("test_add"))
suite.addTest(testadd.TestAdd("test_add2"))
suite.addTest(testadd.TestAdd("test_add3"))

suite.addTest(testadd.TestSubstraction("test_sub1"))
suite.addTest(testadd.TestSubstraction("test_sub2"))

if __name-- == '__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
'''

#coding=utf-8
import unittest

def creatsuite():
    testunit = unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir='D:\Python\Workspace\Test'
    #定义discover方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,
                                                 pattern='test*.py',
                                                 top_level_dir=None)
    #discover方法筛选出用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print (testunit)
    return testunit

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(creatsuite())

