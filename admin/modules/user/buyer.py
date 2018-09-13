# -*- coding: utf-8 -*-
'''
# 用户管理/买家管理
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.modules.comOperation import ComOperation,browser
buyerInst = ComOperation()


def filter_condition():
    """
    全部买家 搜索
    :return:
    """
    # 选择过滤条件
    from time import sleep
    sleep(2)
    Select(browser.find_element_by_name("interest")).select_by_visible_text("已关注") # 关注状态
    Select(browser.find_element_by_name("pstatus")).select_by_visible_text("已认证")   # 认证手机状态
    Select(browser.find_element_by_name("status")).select_by_visible_text("用户状态")   # 用户状态

    Select(browser.find_element_by_name("source")).select_by_visible_text("微信")     # 注册类型
    Select(browser.find_element_by_name("city")).select_by_visible_text("成都市")     # 全部城市
    browser.find_element_by_css_selector("input[name = 'starttime']").send_keys("2018-01-01 00:00:00")
    browser.find_element_by_css_selector("input[name = 'endtime']").send_keys("2018-10-20 00:00:00")

    # 点击搜索按钮
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮

def registe_buyer():
    # browser.find_element_by_css_selector("#datatatle > tbody > tr:nth-child(1) > td:nth-child(8) > a").click()
    browser.find_element_by_css_selector(".fa.fa-plus-square").click()
    locator = (By.ID,"phone")
    phoneInput = buyerInst.wait_element_visible(locator,2)
    if phoneInput is not False:
        phoneInput.send_keys("19914863532")
        browser.find_element_by_css_selector("#password").send_keys("123456")
        browser.find_element_by_css_selector("#phoneFormBut").click()
        buyerInst.close_SweetAlert()
    else:
        pass

def see_buyer_detail():
    goodHref = browser.find_elements_by_link_text("详细")
    if len(goodHref) > 0:
        goodHref[0].click()
    else:
        pass

if __name__ == "__main__":
    buyerInst.openPages(first_level = "用户管理",second_level = "买家管理")
    # filter_condition()
    # registe_buyer()
    see_buyer_detail()




