#coding=utf-8
import unittest
#这里需要导入测试文件
import HTMLTestRunner
import time
import os
from test_admin_login import TestLoginAdmin

testsuite = unittest.TestSuite()

#将测试用例加入到测试容器(套件)中
testsuite.addTest(unittest.makeSuite(TestLoginAdmin,'test'))

#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testsuite)


#定义个报告存放路径，支持相对路径。
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
cur_path = os.getcwd()
filename = cur_path + '\\log\\' + now + 'result.html'
# 'E:\\wxt\lnlife\\admin\\login\\log\\'+ now +'result2.html'
fp = open(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'连你管理后台测试报告',
description=u'用例执行情况：')
#执行测试用例
runner.run(testsuite)

