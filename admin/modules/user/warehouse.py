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
warehouseInst = ComOperation()


def add_warehouse():
    """
    添加配送中心
    :return:
    """
    browser.find_element_by_css_selector("button[data-url *= '/users/warehouse/add']").click()
    locator = (By.CSS_SELECTOR, "input[placeholder = '配送中心名称']")
    inputName = warehouseInst.wait_element_visible(locator)
    if warehouseInst is not False:
        inputName.send_keys("南宁第二配送中心")
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
        warehouseInst.close_SweetAlert()
    else:
        pass

def edit_settlement():
    forward_warehouse_detail()
    browser.find_element_by_css_selector("button[data-url *= '/users/warehouse/458208/goods/6663/settlement']").click()


def filter_condition():
    """
     搜索：选择过滤条件
    :return:
    """
    from time import sleep
    sleep(2)
    Select(browser.find_element_by_name("status")).select_by_visible_text("正常")   # 用户状态
    Select(browser.find_element_by_name("type")).select_by_visible_text("配送中心名称")
    browser.find_element_by_name("key").send_keys("南宁")   # 输入搜索字段
    # 点击搜索按钮
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮

def modify_warehouse():
    """
    修改配送中心 - 页面与添加配送中心一样，按照需求修改即可
    :return:
    """
    browser.find_element_by_css_selector("button[data-url *= '/users/warehouse/edit/521590']").click()

def forward_warehouse_detail():
    filter_condition()
    browser.find_element_by_css_selector("a[href *= '/users/warehouse/458208']").click()

def sale_warehouse_goods():
    """
    给商品铺货
    :return:
    """
    forward_warehouse_detail()
    browser.find_element_by_css_selector("button[data-url *= '/users/warehouse/458208/sale']").click()
    browser.find_element_by_css_selector("input.select2-search__field").send_keys("6663")
    time.sleep(0.5)
    locator = (By.CSS_SELECTOR, "ul.select2-results__options>li")
    WebDriverWait(browser, 2).until(EC.visibility_of_any_elements_located(locator))
    goodsList = browser.find_elements_by_css_selector("li[class^='select2-results__option']")  # 类名以value值开头
    if len(goodsList) > 0:
        if goodsList[0].text == "未找到结果":
            print("未找到结果,输入的商品名称/ID不存在")
        else:
            goodsList[0].click()
            locator = (By.CSS_SELECTOR, "div.sweet-alert.showSweetAlert.visible")
            print("*********",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            saleFlag = warehouseInst.wait_element_visible(locator,2)
            print("*********", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 最多应该是5s，为啥是10s
            print("*********",saleFlag)
            if saleFlag is not False:
                warehouseInst.close_SweetAlert()
                browser.refresh()
            else:
                browser.find_element_by_name("supplierPrice").send_keys("3.33")
                browser.find_element_by_name("warehousePrice").send_keys("4.44")
                browser.find_element_by_id("goodsFormBut").click()
                time.sleep(1)
                warehouseInst.close_SweetAlert()
    else:
        print("没有输入")


def see_oplog():
    warehouseInst.see_oplog()
    time.sleep(2)
    warehouseInst.close_modal_content()

if __name__ == "__main__":
    warehouseInst.openPages(first_level = "用户管理",second_level = "配送中心管理")
    # add_warehouse()
    # modify_deliveryPoint()
    # see_oplog()
    # filter_condition()
    # forward_warehouse_detail()
    sale_warehouse_goods()








