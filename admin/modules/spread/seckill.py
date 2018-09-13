# -*- coding: utf-8 -*-
'''
# 推广管理/抢购活动
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.modules.comOperation import ComOperation,browser
seckillInst = ComOperation()

def additional_seckill():
    """
    追加抢购活动
    :return:
    """
    browser.find_element_by_css_selector("button[data-url *= '/seo/seckill/additional/10023']").click()
    time.sleep(1)

    locator = (By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible")
    Alert_ele = seckillInst.wait_element_visible(locator)
    if Alert_ele is not False:
        # 1.该商品存在尚未结束的抢购活动
        # 2.当前城市没有出售该水票(商品)或者已下架
        print(Alert_ele.text)
        locator = ".sa-confirm-button-container"
        browser.find_element_by_css_selector(locator).click()
        browser.refresh()
    else:
        # 3.正常追加抢购活动
        priceInput = browser.find_element_by_id("scarePrice")
        priceInput.clear()
        priceInput.send_keys("0.01")
        browser.find_element_by_id("number").send_keys("1")
        browser.find_element_by_id("reservationtime").send_keys("2018-11-01 00:00:00 - 2018-11-01 23:59:59")
        browser.find_element_by_css_selector(".applyBtn.btn.btn-small.btn-sm.btn-success").click()
        browser.find_element_by_id("traceBut").click()
        seckillInst.close_SweetAlert()

def create_seckill():
    """
    添加新活动
    :return:
    """
    browser.find_element_by_css_selector("button[data-url *= 'seckill/create']").click()
    locator = (By.ID,"goodsId")
    goodsIDInput = seckillInst.wait_element_visible(locator)
    if goodsIDInput is not False:
        goodsIDInput.send_keys("6673")
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
        browser.find_element_by_id("scarePrice").send_keys("0.01")
        # 如果上已经下架/隐藏中/未发布会弹窗提示错误
        locator = (By.CSS_SELECTOR,".sweet-alert.showSweetAlert.visible")
        Alert_ele = seckillInst.wait_element_visible(locator)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        if Alert_ele is not False:
            # 1.商品已经下架，输入商品ID时提示
            print(Alert_ele.text)
            locator = ".sa-confirm-button-container"
            browser.find_element_by_css_selector(locator).click()
            browser.refresh()
        else:
            # 2.商品有进行中的活动，提交时提示“添加失败”
            # 3.商品首次添加活动，或者活动已经结束
            browser.find_element_by_id("scareNum").send_keys("1")
            browser.find_element_by_id("starttime").send_keys("2018-11-01 00:00:00")
            browser.find_element_by_id("endtime").send_keys("2018-11-11 23:59:59")
            browser.find_element_by_id("scareBut").click()
            seckillInst.close_SweetAlert()
    else:
        pass


def filter_condition():
    """
     搜索：选择过滤条件
    :return:
    """
    Select(browser.find_element_by_name("status")).select_by_visible_text("已结束")   # 活动状态
    Select(browser.find_element_by_name("type")).select_by_visible_text("请选择")
    # browser.find_element_by_name("key").send_keys("")   # 输入搜索字段
    # 点击搜索按钮
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮

def see_oplog():
    browser.find_element_by_css_selector("button[data-url *= '/seo/seckill/oplog/10024']").click()
    time.sleep(3)
    seckillInst.close_modal_content()

if __name__ == "__main__":
    seckillInst.openPages(first_level = "推广管理",second_level = "抢购活动")
    browser.find_element_by_link_text("广州市").click()
    filter_condition()










