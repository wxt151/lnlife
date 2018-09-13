# -*- coding: utf-8 -*-
"""系统设置/参数设置"""

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui

from admin.modules.comOperation import ComOperation,browser

def switch_to_DeliveryDistance():
    # 切换送达距离
    locator = (By.LINK_TEXT, "送达距离")
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
    browser.find_element_by_link_text("送达距离").click()

def set_DeliveryDistance(distance = 100):
    """
    设置送达距离
    :param distance: 设置距离
    :return:
    """
    locator = (By.CSS_SELECTOR,".form-control.intonum.distance")
    set_ele = wait_element_visible(locator)
    if set_ele:
        set_ele.clear()
        set_ele.send_keys(distance)
        click_save_button()
        # click_OK_box()
    else:
        print("页面加载失败")

def click_save_button():
    """点击保存"""
    browser.find_element_by_css_selector(".btn.btn-primary.save").click()
    click_OK_box()

def click_OK_box():
    """操作成功，点击OK"""
    locator = (By.CSS_SELECTOR,".sweet-alert.showSweetAlert.visible")
    confirm_btn = wait_element_visible(locator)
    if confirm_btn:
        browser.find_element_by_css_selector(".sa-confirm-button-container>.confirm").click()
    else:
        pass

def wait_element_visible(locator,timeOut = 5):
    """
    等待页面某个元素出现
    :param locator: 元素定位
    :param timeOut: 等待超时
    :return: 元素出现，返回元素定位，否则返回False
    """
    try:
        #元素出现，返回元素的定位
        return ui.WebDriverWait(browser,timeOut).until(EC.visibility_of_element_located(locator))
    except Exception:
        return False



if __name__ == "__main__":
    paraSetInst = ComOperation()
    paraSetInst.openPages(first_level="系统设置", second_level="参数设置")
    switch_to_DeliveryDistance()
    set_DeliveryDistance(distance=100)