# -*- coding: utf-8 -*-
'''
# 推广管理/红包管理/
'''

import time
# from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.login import logInOut


browser = logInOut.browser
def open_bonusController():
    logInOut.adminLogin()
    #点击红包管理
    browser.implicitly_wait(5)
    WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, u"推广管理")))
    browser.find_element_by_link_text("推广管理").click()  # 通过link文字精确定位元素
    time.sleep(1)
    # 展开红包管理
    locator = (By.LINK_TEXT, "红包管理")
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
    treeview_city_goods = browser.find_element_by_link_text("红包管理")
    ActionChains(browser).double_click(treeview_city_goods).perform()

def switch_bonusSendRecord():
    # 选择红包发放记录
    locator = (By.LINK_TEXT, "红包发放记录")
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
    browser.find_element_by_link_text("红包发放记录").click()

def search_bonusSendRecord():
    #红包状态
    Select(browser.find_element_by_id("status")).select_by_visible_text("未使用")
    #按红包编号搜索
    Select(browser.find_element_by_id("type")).select_by_visible_text("红包编号")
    browser.find_element_by_id("key").send_keys("10058")
    #红包获取时间
    #browser.find_element_by_id("starttime").click()
    #time.sleep(0.5)
    #browser.find_element_by_css_selector("body > div > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.Wday").click()
    #time.sleep(0.3)
    #browser.find_element_by_id("dpOkInput").click()
    #browser.find_element_by_id("endtime").click()
    #time.sleep(0.5)
    #browser.find_element_by_css_selector("body > div > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.Wtoday").click()
    #time.sleep(0.3)
    #browser.find_element_by_id("dpOkInput").click()
    #点击搜索
    browser.find_element_by_css_selector(".fa.fa-search").click()

#导出列表
def export_excel():
    try:
        time.sleep(1)
        browser.find_element_by_css_selector(".fa.fa-file-excel-o").click()
    except Exception as err_msg:
        print(err_msg)


def disable_bonus(boolCanle = True):
    cancleBobusList = browser.find_elements_by_css_selector("button[data-action='红包作废']")
    if len(cancleBobusList) > 0:
        cancleBobusList[0].click()
        wait_Popup_window()
        if boolCanle:
            browser.find_element_by_css_selector("input[placeholder='原因']").send_keys("测试看看作废状态是否发生变化")
            #点击确认
            click_confirm_window()
            #点击OK
            wait_Popup_window()
            click_confirm_window()
        else:
            click_cancle_window()
    else:
        print("没有可以作废的红包")

def wait_Popup_window():
    time.sleep(0.2)
    locator = (By.CSS_SELECTOR,".sweet-alert.showSweetAlert.visible")
    WebDriverWait(browser,3).until(EC.visibility_of_element_located(locator))

#点击确定
def click_confirm_window():
    browser.find_element_by_css_selector(".sa-confirm-button-container").click()  # 点击OK

#点击取消，关闭弹窗
def click_cancle_window():
    try:
        locator = (By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible")
        WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator))
        time.sleep(1)
        browser.find_element_by_css_selector(".sa-button-container>button").click()
    except Exception as err_msg:
        print("取消失败原因：",err_msg)

def operation_record():
    recordList = browser.find_elements_by_css_selector(".fa.fa-list-ol")
    if len(recordList) > 0:
        recordList[0].click()
        locator = (By.ID,"myModalLabel")
        WebDriverWait(browser,3).until(EC.visibility_of_element_located(locator))
        browser.find_element_by_css_selector(".close").click()
    else:
        print("无操作记录可查看")
#获取记录数
def get_dataTables_info():
    dataTables = browser.find_element_by_css_selector(".dataTables_info")
    text_dataTables = dataTables.text
    print(text_dataTables)
    # 正则表达式提取数字
    import re
    findResult = re.findall(r'\d+', text_dataTables)
    print(findResult)

    goodsNum = int(findResult[1])  # 共多少条记录
    pageBtnList = browser.find_elements_by_css_selector("li[class^='paginate_button']")  # 共多少页
    pageBtnNum = len(pageBtnList)
    print("翻页按钮数为：", pageBtnNum)
    if goodsNum % 10 == 0:
        pageNum = goodsNum // 10
    else:
        pageNum = goodsNum // 10 + 1

    if goodsNum <= 10:
        if pageNum == pageBtnNum:  # 只有1页时相等
            print("only onepage right")
        else:
            print("page error")
    else:
        if pageNum == pageBtnNum - 1:  # 大于1页时，页数+下一页
            print("page right")
        else:
            print("page error")


if __name__ == "__main__":
    open_bonusController()
    #disable_bonus(False)
    #operation_record()
    export_excel()
