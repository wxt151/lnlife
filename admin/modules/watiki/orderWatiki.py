# -*- coding: utf-8 -*-
'''
# 水票管理/已售出平台水票
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.modules.comOperation import ComOperation,browser
orderWatikiInst = ComOperation()


def filter_condition():
    """
    已售出平台水票 搜索
    :return:
    """
    # 选择过滤条件
    from time import sleep
    sleep(2)
    Select(browser.find_element_by_name("category")).select_by_visible_text("专用水票") # 水票类型
    Select(browser.find_element_by_name("source")).select_by_visible_text("手动生成")   # 水票来源
    Select(browser.find_element_by_name("status")).select_by_visible_text("交易完成")   # 水票状态

    Select(browser.find_element_by_name("type")).select_by_visible_text("供货商品名称")     # 查询类型
    browser.find_element_by_css_selector("input[name = 'key']").send_keys("花果山") #请输入关键字
    browser.find_element_by_css_selector("input[name = 'timename']").click() # 下单时间
    time.sleep(1)
    timeList = browser.find_elements_by_css_selector("div.ranges>ul>li")
    if len(timeList) > 0:
        timeList[4].click()
    else:
        pass

    # 点击搜索按钮
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮

def see_watiki_details():
    browser.find_element_by_css_selector("#datatatle > tbody > tr:nth-child(1) > td:nth-child(8) > a").click()
    time.sleep(3)
    browser.back()

def put_off_shelves():
    putOffList = browser.find_elements_by_css_selector("button[data-action='下架']")
    print(len(putOffList))
    if len(putOffList) > 0:
        putOffList[0].click()
        locator = (By.CSS_SELECTOR,".sa-confirm-button-container")
        ele = orderWatikiInst.wait_element_visible(locator,2)
        print("确定要下架商品吗？")
        ele.click()
        print("下架成功")

    else:
        print("暂无数据")

def see_oplog():
    orderWatikiInst.see_oplog()
    time.sleep(2)
    locator = (By.CSS_SELECTOR,"body > div.modal.fade.in > div > div > div > div.modal-header > button")
    closeBtn = orderWatikiInst.wait_element_visible(locator)
    if closeBtn is not False:
        closeBtn.click()
    else:
        browser.refresh()
        print("刷新页面")

def see_goods_detail(goodName = "八桂大明山包装饮用水18L"):
    goodHref = browser.find_element_by_link_text(goodName)
    goodHref.click()
    print(goodHref.text)

def refund_watiki():
    refundBtn = browser.find_elements_by_css_selector(".fa.fa-mail-reply-all")
    if len(refundBtn) > 0:
        refundBtn[0].click()
        browser.find_element_by_css_selector("input[name = 'money']").send_keys("0")
        Select(browser.find_element_by_name("reason")).select_by_visible_text("商品下架/缺货")
        Select(browser.find_element_by_name("refundBonuses")).select_by_visible_text("退还")
        # browser.find_element_by_css_selector(".btn.btn-primary").click()
        browser.find_element_by_id("adFormBut").click()
        time.sleep(2)
        orderWatikiInst.close_SweetAlert()
    else:
        pass

def exchange_watiki():
    exchangeBtn = browser.find_elements_by_css_selector(".fa.fa-exchange")
    if len(exchangeBtn) > 0:
        exchangeBtn[0].click()
        browser.find_element_by_css_selector("input[name = 'watikiId']").send_keys("17103")
        browser.find_element_by_css_selector("input[name = 'usedWaterQuantity']").send_keys("0")
        browser.find_element_by_css_selector("input[name = 'remarks']").send_keys("自动化测试")
        # browser.find_element_by_css_selector(".btn.btn-primary").click()
        browser.find_element_by_id("makeorderBut").click()
        time.sleep(2)
        # orderWatikiInst.close_SweetAlert()
    else:
        pass

def see_settle_detailed():
    serverList = browser.find_elements_by_css_selector(".fa.fa-server")
    if len(serverList) > 0:
        serverList[0].click()
        time.sleep(2)
        orderWatikiInst.close_modal_content()
        # orderWatikiInst.close_SweetAlert()
    else:
        pass

if __name__ == "__main__":
    orderWatikiInst.openPages(first_level = "水票管理",second_level = "已售出平台水票")
    orderWatikiInst.select_city(city = "南宁市")
    # filter_condition()
    # see_watiki_details()
    # see_oplog()
    # refund_watiki()
    # exchange_watiki()
    see_settle_detailed()



