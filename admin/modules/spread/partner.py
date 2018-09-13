# -*- coding: utf-8 -*-
'''
# 推广管理/连你邀请人
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.modules.comOperation import ComOperation,browser
partnerInst = ComOperation()


def add_partner():
    """
    添加邀请人
    :return:
    """
    browser.find_element_by_link_text("邀请人管理").click()
    browser.find_element_by_css_selector("button[data-url *= '/seo/partner/add']").click()
    locator = (By.CSS_SELECTOR,"input[placeholder = '手机号/ID']")
    phoneIDInput = partnerInst.wait_element_visible(locator)
    if phoneIDInput is not False:
        phoneIDInput.send_keys("19914863531")
    else:
        pass

    time.sleep(1)
    locator = (By.CSS_SELECTOR, "ul.select2-selection__rendered>li")
    partnerInst.wait_element_visible(locator, 2)
    partnerInstList = browser.find_elements_by_css_selector("li[class ^= 'select2-results__option']")  # 类名以value值开头
    partnerInstList[0].click()

    browser.find_element_by_id("name").send_keys("桃子")
    browser.find_element_by_id("type4").click()
    Select(browser.find_element_by_id("city")).select_by_visible_text("南宁市")
    browser.find_element_by_id("day").send_keys("3")
    browser.find_element_by_id("percen").send_keys("50")
    browser.find_element_by_id("bonus").send_keys("10086")
    browser.find_element_by_id("partnerBut").click()
    time.sleep(3)
    partnerInst.close_SweetAlert()

def set_partner_default():
    """
    邀请人默认值设置
    :return:
    """
    browser.find_element_by_link_text("邀请人管理").click()
    browser.find_element_by_css_selector("button[data-url *= '/seo/partner/default']").click()
    locator = (By.ID,"day")
    dayInput = partnerInst.wait_element_visible(locator)
    if dayInput is not False:
        # 输入框原本有默认值，需要清空再输入
        dayInput.clear()
        dayInput.send_keys("365")
        commisInput = browser.find_element_by_id("commission")
        commisInput.clear()
        commisInput.send_keys(20)
    else:
        pass
    browser.find_element_by_id("biguserBut").click()
    time.sleep(1)
    partnerInst.close_SweetAlert()

def personal_promotion_effect():
    browser.find_element_by_link_text("邀请人管理").click()
    browser.find_element_by_link_text("桃子").click()

if __name__ == "__main__":
    partnerInst.openPages(first_level = "推广管理",second_level = "连你邀请人")
    personal_promotion_effect()










