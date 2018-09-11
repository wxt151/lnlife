# -*- coding: utf-8 -*-
'''管理员登录'''
'''玩玩而已，别当真'''

from selenium import webdriver
import time
import unittest
from logInOut import LogIn,LogOut
import HTMLTestRunner

login_ins = LogIn("admin","123456")

class TestlogInOut(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass exec once",cls.__name__)

    def setUp(self):
        print('setup...')
        pass

    # 登录管理员后台用例
    def test_login(self):
        """管理后台登录"""
        #登录
        login_ins.login()

    def test_123456(self):
        """随意些的没有意义的用例"""
        assert "admin" == "ADMIN","not equal"

    def tearDown(self):
        print('tearDown...')
        pass
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass exec once",cls.__name__)
        LogOut.quit()

if __name__ == "__main__":
    #构造测试集
    suite = unittest.TestSuite() #定义一个单元测试容器
    suite.addTest(TestlogInOut("test_adminLogin")) #将测试用例加入到测试容器中
    #定义测试报告存放路径，支持相对路径
    filename = 'E:/wxt/lnlife/admin/login/log/result.html'
    fp = open(filename,'wb')
    print("fp is opend",fp)
    #定义测试报告

    #执行测试
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'管理后台登录测试报告',
        description=u'用例执行情况：')
    # 运行测试用例
    runner.run(suite)


