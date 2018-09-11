# -*- coding: utf-8 -*-
'''
# 推广管理/团购活动
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.login import logInOut

browser = logInOut.browser

class GroupBuy(object):
    def admin_login(self):
        admin = logInOut.LogIn()
        admin.login()

    def open_groupBuy(self):
        #点击推广管理
        browser.implicitly_wait(5)
        WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, u"推广管理")))
        browser.find_element_by_link_text("推广管理").click()  # 通过link文字精确定位元素
        time.sleep(1)
        # 双击展开团购活动
        locator = (By.LINK_TEXT, "团购活动")
        WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
        treeview_city_goods = browser.find_element_by_link_text("团购活动")
        ActionChains(browser).double_click(treeview_city_goods).perform()

    def add_groupBuy(self):
        # 点击添加团购
        add_btn = ".btn.btn-default.btn-sm.modal-btn"
        browser.find_element_by_css_selector(add_btn).click()

        # 勾选桶装水，默认选中水票
        locator = (By.CSS_SELECTOR, "#activitytype1")
        ele = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
        if ele is not False:
            print(ele)
            ele.click()
        else:
            pass

        # 定位当前页面所有的输入框
        input_ele = "input.select2-search__field"
        inputList = browser.find_elements_by_css_selector(input_ele)
        # 绑定商品
        inputList[0].send_keys("巴马")
        time.sleep(1)
        # 等待显示搜索结果
        locator = (By.CSS_SELECTOR, "ul.select2-selection__rendered>li")
        WebDriverWait(browser, 4).until(EC.visibility_of_any_elements_located(locator))
        goodsList = browser.find_elements_by_css_selector("li[class^='select2-results__option']")  # 类名以value值开头
        resultText = goodsList[0].text
        if resultText == "未找到结果":
            pass
        else:
            goodsList[0].click()


        browser.find_element_by_id("scarePrice").send_keys("0.01")
        browser.find_element_by_id("scareNum").send_keys("5")
        # 获取当前时间
        import datetime
        curTiem = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        delayTime = datetime.datetime.now() + datetime.timedelta(minutes=5)
        delayTimeF = delayTime.strftime('%Y-%m-%d %H:%M:%S')
        print("curTiem",curTiem)
        print("delayTimeF",delayTimeF)
        browser.find_element_by_id("endtime").send_keys(delayTimeF)
        browser.find_element_by_css_selector("input[id = 'name']").send_keys("团购-桶装水小程序支付")

        # 发团人
        inputList[1].send_keys("15220089922")
        time.sleep(1)
        # 等待显示搜索结果
        locator = (By.CSS_SELECTOR, "ul.select2-selection__rendered>li")
        WebDriverWait(browser, 4).until(EC.visibility_of_any_elements_located(locator))
        sponsorList = browser.find_elements_by_css_selector("li[class^='select2-results__option']")  # 类名以value值开头
        resultText = sponsorList[0].text
        if resultText == "未找到结果":
            pass
        else:
            sponsorList[0].click()

        browser.find_element_by_css_selector(".btn.btn-primary").click()
        # 执行成功，需要关闭OK对话框
        self.click_confirm_window()


    #点击确定
    def click_confirm_window(self):
        time.sleep(1)
        locator = (By.CSS_SELECTOR,".sweet-alert.showSweetAlert.visible")
        WebDriverWait(browser,3).until(EC.visibility_of_element_located(locator))
        browser.find_element_by_css_selector(".sa-confirm-button-container").click()  # 点击OK


if __name__ == "__main__":
    groupbuy  = GroupBuy()
    groupbuy.admin_login()
    groupbuy.open_groupBuy()
    groupbuy.add_groupBuy()
    time.sleep(2)
    browser.quit()


