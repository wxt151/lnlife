# -*- coding: utf-8 -*-
'''
# 用户管理/配送员管理
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.modules.comOperation import ComOperation,browser
deliveryManInst = ComOperation()


def filter_condition():
    """
    配送员 搜索
    :return:
    """
    # 选择过滤条件
    from time import sleep
    sleep(2)
    Select(browser.find_element_by_name("status")).select_by_visible_text("全部状态")   # 用户状态
    Select(browser.find_element_by_name("workstatus")).select_by_visible_text("接单中") # 接单状态
    Select(browser.find_element_by_name("level")).select_by_visible_text("普通")   # 配送员职级

    Select(browser.find_element_by_name("type")).select_by_visible_text("绑定配送点ID")     # 查询字段
    browser.find_element_by_name("key").send_keys("10333")   # 输入搜索字段
    # 点击搜索按钮
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮

def set_workTime():
    browser.find_element_by_css_selector("button[data-url *= 'users/delivery_man/workTime']").click()
    locator = (By.ID,"begintime")
    begintime = deliveryManInst.wait_element_visible(locator,2)
    if begintime is not  False:
        begintime.clear()
        begintime.send_keys("10:00")
    else:
        pass
    endtime = browser.find_element_by_id("endtime")
    endtime.clear()
    endtime.send_keys("19:30")
    browser.find_element_by_id("setsaveBut").click()
    deliveryManInst.close_SweetAlert()

def add_deliveryMan():
    browser.find_element_by_css_selector("button[data-url $= '/users/delivery_man/add']").click()
    locator = (By.CSS_SELECTOR,".form-control.nickname")
    nameInput = deliveryManInst.wait_element_visible(locator)
    if nameInput is not False:
        nameInput.send_keys("城东祥宾-袁渣渣")
    else:
        pass
    browser.find_element_by_css_selector(".form-control.phone").send_keys("19914863531")
    browser.find_element_by_css_selector(".form-control.loginpass").send_keys("a123456")
    browser.find_element_by_css_selector("input[name = 'level']").click()
    Select(browser.find_element_by_id("province")).select_by_visible_text("广西")
    time.sleep(1)
    Select(browser.find_element_by_css_selector(".form-control.marginright.city")).select_by_visible_text("南宁市")
    time.sleep(1)
    Select(browser.find_element_by_name("shop")).select_by_visible_text("城东祥宾路配送点") # 10209
    browser.find_element_by_css_selector("input[name = 'usersort'][value = '2']").click()
    browser.find_element_by_css_selector("input[name = 'remarks']").send_keys("自动添加")
    browser.find_element_by_id("adddeliveryBut").click()
    deliveryManInst.close_SweetAlert()

def set_largeOrder():
    browser.find_element_by_css_selector("button[data-url $= '/users/delivery_man/large']").click()
    locator = (By.ID, "beginnumber")
    quantityInput = deliveryManInst.wait_element_visible(locator)
    if quantityInput is not False:
        quantityInput.clear()
        quantityInput.send_keys("5")
        browser.find_element_by_id("biguserBut").click()
        deliveryManInst.close_SweetAlert()
    else:
        pass

def see_oplog():
    deliveryManInst.see_oplog()
    time.sleep(2)
    deliveryManInst.close_modal_content()

def modify_workStatus():
    modifyBtn = browser.find_elements_by_css_selector("button[data-url *= '/users/delivery_man/modifyWorkStatus']")
    if len(modifyBtn) > 0:
        modifyBtn[0].click()
        time.sleep(1)
        browser.find_element_by_id("userssort1").click()
        browser.find_element_by_id("statusBut").click()
        deliveryManInst.close_SweetAlert()
    else:
        pass



if __name__ == "__main__":
    deliveryManInst.openPages(first_level = "用户管理",second_level = "配送员管理")
    # filter_condition()
    # set_workTime()
    # add_deliveryMan()
    # set_largeOrder()
    # see_oplog()
    modify_workStatus()




