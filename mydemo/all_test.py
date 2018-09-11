#coding=utf-8
import unittest
#这里需要导入测试文件
from test_case import baidu,baidu_copy
import HTMLTestRunner
import time

testunit=unittest.TestSuite()

#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(baidu_copy.Baidu1))

#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)

#定义个报告存放路径，支持相对路径。
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename = 'E:\\wxt\lnlife\\mydemo\\report\\'+ now +'result2.html'
fp = open(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'百度搜索测试报告',
description=u'用例执行情况：')
#执行测试用例
runner.run(testunit)

