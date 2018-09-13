# -*- coding: utf-8 -*-
'''
# 用户管理/焦点设置
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.modules.comOperation import ComOperation,browser
focusSetInst = ComOperation()


def add_focus_ad():
    """
    添加焦点广告
    :return:
    """
    browser.find_element_by_css_selector("button[data-url *= '/seo/ad/create?type=1&postion_id=3&city=0']").click()
    locator = (By.NAME,"title")
    titleInput = focusSetInst.wait_element_visible(locator)
    if titleInput is not False:
        titleInput.send_keys("好水任你喝")
        browser.find_element_by_name("jump_url").send_keys("http://wechat6.t-lianni.com/")
        browser.find_element_by_id("reservationtime").send_keys("2018/10/26 09:00:00 - 2018/10/28 09:00:00 ")
        browser.find_element_by_css_selector(".applyBtn.btn.btn-small.btn-sm.btn-success").click()
        browser.find_element_by_name("sort").send_keys("106")
        # 上传文件
        import os
        time.sleep(1)
        # browser.find_element_by_css_selector(".fa.fa-paperclip").click()
        # browser.find_element_by_css_selector("btn.btn-default.btn-file").click()
        browser.find_element_by_css_selector("#adForm > div:nth-child(8) > div").click()
        os.system("upfile.exe")
    else:
        pass

def del_focus_ad():
    """
    删除焦点广告
    :return:
    """
    browser.find_element_by_css_selector("button[data-url *= '/seo/ad/delete/60']").click()
    time.sleep(2)
    browser.find_element_by_css_selector(".sa-confirm-button-container").click()
    time.sleep(1)
    focusSetInst.close_SweetAlert()

def modify_focus_ad():
    """
    修改焦点广告
    :return:
    """
    browser.find_element_by_css_selector("button[data-url *= '/seo/ad/edit/110']").click()


def see_rules_declaration():
    """
    查看规则说明
    :return:
    """
    browser.find_element_by_css_selector(".btn.btn-default.btn-sm.explain").click()
    time.sleep(2)
    focusSetInst.close_modal_content()

if __name__ == "__main__":
    focusSetInst.openPages(first_level = "推广管理",second_level = "焦点设置")
    see_rules_declaration()










