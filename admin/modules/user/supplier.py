# -*- coding: utf-8 -*-
'''
# 用户管理/配送中心管理
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.modules.comOperation import ComOperation,browser
supplierInst = ComOperation()


def add_supplier():
    """
    添加供应商
    :return:
    """
    browser.find_element_by_css_selector("button[data-url *= '/users/supplier/add']").click()
    locator = (By.CSS_SELECTOR, "input[placeholder = '供应商名称']")
    inputName = supplierInst.wait_element_visible(locator)
    if inputName is not False:
        inputName.send_keys("巴马活泉")
        browser.find_element_by_css_selector("input[placeholder = '认证手机']").send_keys("18914863531")
        Select(browser.find_element_by_id("province")).select_by_visible_text("广西")
        time.sleep(0.5)
        Select(browser.find_element_by_id("city")).select_by_visible_text("南宁市")
        browser.find_element_by_css_selector("input[placeholder = '详细地址']").send_keys("金湖路55号亚航财富中心29层")
        browser.find_element_by_css_selector("input[placeholder = '登录密码']").send_keys("123456")
        browser.find_element_by_css_selector("input[placeholder = '提现密码']").send_keys("123456")
        browser.find_element_by_css_selector("input[placeholder = '开户人姓名']").send_keys("袁渣渣")
        Select(browser.find_element_by_name("bank")).select_by_visible_text("建设银行")
        Select(browser.find_element_by_name("account_type")).select_by_visible_text("对私")
        browser.find_element_by_css_selector("input[name = 'cardID']").send_keys("6227000011040161024")
        browser.find_element_by_css_selector("input[name = 'cardadr']").send_keys("大柳树支行")
        browser.find_element_by_css_selector("input[name = 'inter_code']").send_keys("986357")
        browser.find_element_by_css_selector("input[name = 'remarks']").send_keys("自动添加")
        browser.find_element_by_id("addFormBut").click()
        supplierInst.close_SweetAlert()
    else:
        pass


def filter_condition():
    """
     搜索：选择过滤条件
    :return:
    """
    from time import sleep
    sleep(2)
    Select(browser.find_element_by_name("status")).select_by_visible_text("正常")   # 用户状态
    # 点击搜索按钮
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮

def modify_supplier():
    """
    修改配送中心 - 页面与添加配送中心一样，按照需求修改即可
    :return:
    """
    browser.find_element_by_css_selector("button[data-url *= '/users/supplier/edit/458207']").click()


def see_oplog():
    supplierInst.see_oplog()
    time.sleep(2)
    supplierInst.close_modal_content()

if __name__ == "__main__":
    supplierInst.openPages(first_level = "用户管理",second_level = "供应商管理")
    # add_supplier()
    # filter_condition()
    # modify_supplier()
    see_oplog()










