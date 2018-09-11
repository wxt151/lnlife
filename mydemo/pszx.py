# -*- coding: utf-8 -*-
'''
# 配送中心后台/
'''

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
url = "http://pszx7.t-lianni.com/"
browser.get(url)
browser.maximize_window()
def loginPszx(username = "13877485916",password = "123456"):
    ele_user = browser.find_element_by_name("phone")
    ele_user.clear()
    ele_user.send_keys(username)
    ele_pwd = browser.find_element_by_name("password")
    ele_pwd.clear()
    ele_pwd.send_keys(password)
    ele_login = browser.find_element_by_id("loginBtn")
    ele_login.click()
    time.sleep(1)

def open_deliverymanStat():
    loginPszx()
    #点击红包管理
    browser.implicitly_wait(5)
    WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, u"配送员业绩")))
    browser.find_element_by_link_text("配送员业绩").click()  # 通过link文字精确定位元素
    time.sleep(1)

def get_Requests():
    import  requests


#导出列表
def export_excel():
    try:
        time.sleep(1)
        browser.find_element_by_css_selector(".fa.fa-file-excel-o").click()
    except Exception as err_msg:
        print(err_msg)



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
    open_deliverymanStat()
