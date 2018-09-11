# -*- coding: utf-8 -*-
'''
# 评价管理
'''

from selenium.webdriver.common.action_chains import ActionChains 
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.login import logInOut
browser = logInOut.browser
admin = logInOut.LogIn()
admin.login()

def open_commentControl():
    print("open_commentControl start calling...")
    # 点击商品管理browser.implicitly_wait(5)
    WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, u"商品管理")))
    browser.find_element_by_link_text("商品管理").click()  # 通过link文字精确定位元素
    time.sleep(1)

    # 双击评价管理
    locator = (By.LINK_TEXT, "评价管理")
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
    comment_treeview = browser.find_element_by_link_text("评价管理")
    ActionChains(browser).double_click(comment_treeview).perform()
    # 判断是否出现商品信息,出现则说明页面加载成功
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, "商品")))

def search_comment():
    print("search_comment start calling...")
    # 选择完成时间为最近30日
    Select(browser.find_element_by_name("timeType")).select_by_visible_text("完成时间")
    browser.find_element_by_css_selector("input[placeholder='请选择时间区间']").click()
    time.sleep(1)
    timeList = browser.find_elements_by_css_selector("div[class='ranges']>ul>li")  # 查找下拉框所有可选的选项
    if len(timeList) > 0:
        timeList[3].click()
    else:
        print("error")
    #点击搜索按钮
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮
def tab_order_type():
    # 切换平台订单
    time.sleep(1)
    browser.find_element_by_link_text("平台订单").click()

#删除评论
def delete_comment():
    deleteList = browser.find_elements_by_css_selector("button[data-action='删除评价']")
    if len(deleteList) > 0:
        deleteList[0].click()
    else:
        print("没有评论可删除")
    #您确认要删除评价？
    sweet_alter_visble()

#恢复显示评价
def recover_comment():
    recoverList = browser.find_elements_by_css_selector("button[data-action='显示评价']")
    if len(recoverList) > 0:
        recoverList[0].click()
    else:
        print("没有评论可恢复")
    # #您确认要恢复评价？
    sweet_alter_visble()

#导出列表
def export_excel():
    try:
        time.sleep(1)
        browser.find_element_by_css_selector(".fa.fa-file-excel-o").click()
    except Exception as err_msg:
        print(err_msg)

# 一次弹窗处理
def sweet_alter_visble():
    locator = (By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator))
    if True:
        browser.find_element_by_css_selector(".sa-confirm-button-container").click()  # 是的，显示评价！
        confirm_ok()
    else:
        browser.find_element_by_css_selector(".sa-button-container>button").click()  # 取消弹窗

# 操作成功弹窗关闭
def confirm_ok():
    locator = (By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator))
    time.sleep(1)
    browser.find_element_by_css_selector(".sa-confirm-button-container").click()  # OK



if __name__ == "__main__":
    open_commentControl()
    # search_comment()
    # #delete_comment()
    # recover_comment()
    # export_excel()


