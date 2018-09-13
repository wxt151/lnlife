# -*- coding: utf-8 -*-
'''
# 财务管理/交易明细
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.modules.comOperation import ComOperation,browser
tradeInst = ComOperation()

def filter_condition(status = "活动状态"):
    """
     搜索：选择过滤条件
    :return:
    """
    browser.find_element_by_name("starttime").send_keys("2018-10-01 00:00:00")   # 输入搜索字段
    # browser.find_element_by_id("dpOkInput").click()
    browser.find_element_by_name("endtime").send_keys("2018-10-31 23:59:59")  # 输入搜索字段
    # browser.find_element_by_id("dpOkInput").click()
    # 点击搜索按钮
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮





if __name__ == "__main__":
    tradeInst.openPages(first_level = "财务管理",second_level = "交易明细")
    filter_condition()










