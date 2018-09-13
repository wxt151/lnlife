# -*- coding: utf-8 -*-
'''
# 用户管理/配送点管理
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.modules.comOperation import ComOperation,browser
deliveryPointInst = ComOperation()


def add_deliveryPoint():
    browser.find_element_by_css_selector("button[data-url *= '/users/delivery_point/add']").click()
    locator = (By.CSS_SELECTOR,"input[name = 'phone']")
    inputPhone =  deliveryPointInst.wait_element_visible(locator)
    if inputPhone is not False:
        inputPhone.send_keys("18914863532")
        browser.find_element_by_name("loginpass").send_keys("123456")
        Select(browser.find_element_by_name("city")).select_by_visible_text("南宁市")
        time.sleep(0.5)
        Select(browser.find_element_by_name("distribution")).select_by_visible_text("南宁配送中心")
        browser.find_element_by_id("type1").click()
        browser.find_element_by_name("remarks").send_keys("程序添加的")
        browser.find_element_by_id("sendpointBut").click()
        deliveryPointInst.close_SweetAlert()
        # 完善信息
        browser.find_element_by_id("Storename").send_keys("金湖配送点")
        browser.find_element_by_id("range").send_keys("100")
        browser.find_element_by_id("address").send_keys("金湖路55号亚航财富中心29层")
        # 向富文本框输入内容
        # 首先定位到最外面的 iframe 框架：
        iframe = browser.find_element_by_css_selector("iframe.ke-edit-iframe")
        # 进入 iframe 框架
        browser.switch_to_frame(iframe)
        # 定位输入框写入内容
        browser.find_element_by_css_selector("body.ke-content").send_keys("自动化添加测试")
        # 退出 iframe 框架
        browser.switch_to_default_content()

        saveBtn = browser.find_element_by_id("shopFormBtn")
        while True:  # 点击多次保存才生效，不懂为啥
            saveBtn.click()
            locator = (By.CSS_SELECTOR, "div.sweet-alert.showSweetAlert.visible")
            sucessFlag = deliveryPointInst.wait_element_visible(locator)
            if sucessFlag is False:
                continue
            else:
                deliveryPointInst.close_SweetAlert()
                break
        browser.back()
    else:
        pass



def delete_deliveryPoint():
    """
    删除配送点
    :return:
    """
    modifyBtn = browser.find_elements_by_css_selector("button[data-url *= '/users/delivery_point/del/10694']")
    if len(modifyBtn) > 0:
        modifyBtn[0].click()
        time.sleep(1)
        browser.find_element_by_css_selector(".cancel").click()
    else:
        pass

def filter_condition():
    """
     搜索：选择过滤条件
    :return:
    """
    from time import sleep
    sleep(2)
    Select(browser.find_element_by_name("status")).select_by_visible_text("全部状态")   # 用户状态
    Select(browser.find_element_by_name("type")).select_by_visible_text("姓名") # 接单状态
    browser.find_element_by_name("key").send_keys("安吉")   # 输入搜索字段
    # 点击搜索按钮
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮

def modify_deliveryPoint():
    """
    修改配送点
    :return:
    """
    modifyBtn = browser.find_elements_by_css_selector("button[data-url *= '/users/delivery_point/modify/10640']")
    if len(modifyBtn) > 0:
        modifyBtn[0].click()
        time.sleep(1)
        browser.find_element_by_name("remarks").send_keys("什么也不想改")
        browser.find_element_by_id("sendpointBut").click()
        deliveryPointInst.close_SweetAlert()
    else:
        pass

def switch_city():
    """
    切换城市
    :return:
    """
    browser.find_element_by_link_text("柳州市").click()

def switch_shopType():
    """
    切换平台配送点/加盟店
    :return:
    """
    # browser.find_element_by_css_selector("a[href *= 'users/delivery_point?shopType=1']").click()
    browser.find_element_by_link_text("配送点").click()


def see_oplog():
    deliveryPointInst.see_oplog()
    time.sleep(2)
    deliveryPointInst.close_modal_content()

def op_deliveryPoint_detail():
    browser.find_element_by_css_selector("a[href *= '/users/delivery_point/detail_goods/494430']").click()
    stop_point_goods()

def stop_point_goods():
    goodsList = browser.find_elements_by_css_selector("button[data-url *= '/users/delivery_point/detail_goods/stop']")
    if len(goodsList) > 0:
        goodsList[0].click()
        time.sleep(1)
        browser.find_element_by_css_selector(".sa-confirm-button-container").click()
        time.sleep(1)
        deliveryPointInst.close_SweetAlert()
    else:
        pass


if __name__ == "__main__":
    deliveryPointInst.openPages(first_level = "用户管理",second_level = "配送点管理")
    # filter_condition()
    # modify_deliveryPoint()
    # delete_deliveryPoint()
    # see_oplog()
    # switch_shopType()
    # add_deliveryPoint()
    op_deliveryPoint_detail()





