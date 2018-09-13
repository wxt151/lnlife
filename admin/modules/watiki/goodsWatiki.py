# -*- coding: utf-8 -*-
'''
# 水票管理/平台水票管理
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.modules.comOperation import ComOperation,browser
goodWatikiInst = ComOperation()

def add_watikiMeal(addType = 1):
    """
    添加水票
        :param addtype:  添加水票/套餐 ;1 = 套餐,2 = 水票
        :return:
    """
    addBtnList = []
    if addType == 1:
        addBtnList = browser.find_elements_by_css_selector(".fa.fa-cubes")

    elif addType == 2:
        addBtnList = browser.find_elements_by_css_selector(".btn.btn-default.btn-sm.J-add-ticket")
    else:
        print("error parameter !!!")

    addBtnList[0].click()
    set_Para(addTyte = addType,watikiType = 2)

    # 点击确定提交
    browser.find_element_by_id("waterticketBut").click()
    goodWatikiInst.close_SweetAlert()
#
# def add_ticket(type = 1):
#     """
#     添加水票
#         :param type:  添加水票/套餐 ;1 = 套餐,2 = 水票
#         :param columns: 字典中的key
#         :return:
#     """
#     addWatikiBtn = browser.find_elements_by_css_selector(".btn.btn-default.btn-sm.J-add-ticket")
#     if len(addWatikiBtn) > 0:
#         addWatikiBtn[0].click()
#         locator = (By.CSS_SELECTOR,".modal-title.modal-addtitle")
#         modalTitle = goodWatikiInst.wait_element_visible(locator,2)
#         if modalTitle.text == "添加水票":
#             set_Para(addType = "水票",watikiType = "通用")
#             browser.find_element_by_id("waterticketBut").click()
#             goodWatikiInst.close_SweetAlert()
#         else:
#             print("弹窗加载超时了！")
#     else:
#         pass


def filter_condition():
    # 选择过滤条件
    from time import sleep
    sleep(5)
    Select(browser.find_element_by_name("status")).select_by_visible_text("售卖中")
    Select(browser.find_element_by_name("watikitype")).select_by_visible_text("专用水票")
    Select(browser.find_element_by_name("preferences")).select_by_visible_text("新用户优惠")

    Select(browser.find_element_by_name("type")).select_by_visible_text("商品名称")
    browser.find_element_by_css_selector("#form > div:nth-child(5) > input").send_keys("花果山")
    browser.find_element_by_css_selector("input[name = 'starttime']").send_keys("2018-01-01 00:00:00")
    browser.find_element_by_css_selector("input[name = 'endtime']").send_keys("2018-10-10 00:00:00")

    # 点击搜索按钮
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮

def order_watiki():
    eleList = browser.find_elements_by_css_selector(".fa.fa-arrows-v")
    if len(eleList) > 0:
        eleList[0].click()
        locator = (By.CSS_SELECTOR,".form-control.sort")
        sortInput = ComOperation.wait_element_visible(locator,2)
        print("sortInput is :",type(sortInput))
        if sortInput is not None:
            sortInput.clear()
            sortInput.send_keys("301")
            browser.find_element_by_id("watersortBut").click()
            goodWatikiInst.close_SweetAlert()
        else:
            pass
    else:
        print("水票列表为空")

def set_Para(addTyte = 1,watikiType = 1):
    """
     添加水票/套餐弹窗的参数选项设置
        :param addTyte:  添加水票/套餐 ;1 = 套餐,2 = 水票
        :param watikiType:  水票类型 ;1 = 专用,2 = 通用
        :return:
    """
    if addTyte == 1: #添加套餐
        pass
    elif addTyte == 2:
        if watikiType == 2: #通用水票
            import  time
            time.sleep(2)
            browser.find_element_by_id("ticktype2").click()  # 水票类型，通用
            Select(browser.find_element_by_name("ticket_num")).select_by_visible_text("18")  # 水票名称
            browser.find_element_by_css_selector(".select2-search__field").send_keys("巴马")
        else:
            browser.find_element_by_css_selector(".select2-search__field").send_keys("6616")
    else:
        print("error parameter !!! ")

    # 等待显示搜索结果
    import time
    time.sleep(1)
    locator = (By.CSS_SELECTOR, "ul.select2-selection__rendered>li")
    goodWatikiInst.wait_element_visible(locator, 2)
    goodWatikiList = browser.find_elements_by_css_selector("li[class^='select2-results__option']")  # 类名以value值开头
    goodWatikiList[0].click()

    # 共用设置的参数选项
    browser.find_element_by_id("package_name").send_keys("买2送1，超值套餐！！")  # 套餐名，选填
    Select(browser.find_element_by_name("priceid")).select_by_visible_text("买9送1") # 水票信息
    browser.find_element_by_name("sales").send_keys("0.01")  # 水票促销价
    settleNumEle = browser.find_element_by_name("settlenum")  # 起送数量
    settleNumEle.clear()
    settleNumEle.send_keys("2")
    browser.find_element_by_id("preferences").click()  # 参加新用户优惠

def show_rule():
    browser.find_element_by_css_selector(".btn.btn-default.btn-sm.J-rule").click()
    locator = (By.CSS_SELECTOR,".modal-content")
    goodWatikiInst.wait_element_visible(locator,2)
    time.sleep(3)
    goodWatikiInst.close_modal_content()

def put_off_shelves():
    putOffList = browser.find_elements_by_css_selector("button[data-action='下架']")
    print(len(putOffList))
    if len(putOffList) > 0:
        putOffList[0].click()
        locator = (By.CSS_SELECTOR,".sa-confirm-button-container")
        ele = goodWatikiInst.wait_element_visible(locator,2)
        print("确定要下架商品吗？")
        ele.click()
        print("下架成功")

    else:
        print("暂无数据")

def see_oplog():
    goodWatikiInst.see_oplog()
    time.sleep(2)
    goodWatikiInst.close_modal_content()

def see_goods_detail(goodName = "八桂大明山包装饮用水18L"):
    goodHref = browser.find_element_by_link_text(goodName)
    goodHref.click()
    print(goodHref.text)


if __name__ == "__main__":
    goodWatikiInst.openPages(first_level = "水票管理",second_level = "平台水票管理")
    goodWatikiInst.select_city(city = "南宁市")
    # filter_condition()
    # watiki_order()
    # add_ticket()
    # add_watikiMeal(2)
    # show_rule()
    # put_off_shelves()
    see_oplog()
    # see_goods_detail()



