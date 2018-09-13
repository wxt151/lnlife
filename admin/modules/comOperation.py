# -*- coding: utf-8 -*-
"""管理后台各个页面相同操作"""

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui
from admin.login import logInOut

adminInst = logInOut.LogIn()  # 实例化，全局变量，模块被加载时执行创建
adminInst.login()            # 登录管理后台
browser = logInOut.browser  # 获取管理后台浏览器对象

class ComOperation():
    """管理后台网页通用操作类"""

    # def openPages(self,first_level, second_level):
    #     """打开某个具体页面，如订单管理/全部订单"""
    #     # 点击一级导航目录
    #     browser.implicitly_wait(5)
    #     WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, first_level)))
    #     browser.find_element_by_link_text(first_level).click()  # 通过link文字精确定位元素
    #     time.sleep(1)
    #     # 双击二级导航目录
    #     locator = (By.LINK_TEXT, second_level)
    #     WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
    #     treeview_city_goods = browser.find_element_by_link_text(second_level)
    #     ActionChains(browser).double_click(treeview_city_goods).perform()

    def openPages(self,first_level, second_level):
        """打开某个具体页面，如订单管理/全部订单"""
        # 点击一级导航目录
        locator = (By.LINK_TEXT, first_level)
        level1 = ComOperation.wait_element_visible(locator, 3)
        if level1 is not False:
            level1.click()
        else:
            print("导航树商品管理元素定位失败")
        time.sleep(1)
        # 双击二级导航目录
        locator = (By.LINK_TEXT, second_level)
        level2 = ComOperation.wait_element_visible(locator, 3)
        ActionChains(browser).double_click(level2).perform()

    def select_city(self,city = "柳州市"):
        # 选择城市
        locator = (By.LINK_TEXT, city)
        WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
        browser.find_element_by_link_text(city).click()


    def export_excel(self):
        """导出列表"""
        try:
            time.sleep(1)
            browser.find_element_by_css_selector(".fa.fa-file-excel-o").click()
        except Exception as err_msg:
            print(err_msg)

    def open_orderOnline(self):
        # 点击订单管理
        locator = (By.LINK_TEXT, u"订单管理")
        ele = ComOperation.wait_element_visible(locator, 3)
        if ele is not False:
            ele.click()
        else:
            print("导航树商品管理元素定位失败")

        time.sleep(1)

        # 双击全部订单
        locator = (By.LINK_TEXT, u"全部订单")
        ele = ComOperation.wait_element_visible(locator, 3)
        if ele is not False:
            ele.click()
        else:
            print("全部订单子树定位失败")

    @staticmethod
    def wait_element_visible(locator, timeOut=5):
        """等待页面元素显示"""
        try:
            return WebDriverWait(browser,timeOut).until(EC.visibility_of_element_located(locator))
        except Exception as errMsg:
            print(errMsg)
            return False

    def wait_SweetAlert_visible (self):
        """等待弹窗出现"""
        locator = (By.CSS_SELECTOR, "div.sweet-alert.showSweetAlert.visible")
        try:
            return WebDriverWait(browser,3).until(EC.visibility_of_element_located(locator))
        except Exception as errMsg:
            print(errMsg)
            return False

    def close_modal_content(self):
        """关闭模态框，例如关闭{操作记录}"""
        locator = (By.CSS_SELECTOR, "div.modal-dialog>div.modal-content>div.modal-header>button.close")
        # locator = (By.CSS_SELECTOR, "button.close > span")
        close_btn_ele = self.wait_element_visible(locator, 2)
        if close_btn_ele is not False:
            close_btn_ele.click()
        else:
            # 查看记录，无需刷新页面
            print("刷新页面")
            browser.refresh()

    def close_SweetAlert (self):
        """关闭SweetAlert弹窗"""
        SweetAlert = self.wait_SweetAlert_visible()
        if SweetAlert is not False:
            browser.find_element_by_css_selector(".sa-confirm-button-container").click()
        else:
            pass

    def onclick_confirm(self):
        confirm = self.wait_SweetAlert_visible()
        if confirm is not False:
            browser.find_element_by_css_selector(".sa-confirm-button-container").click()
        else:
            pass


    def find_oplog_button(self):
        oplog_list = browser.find_elements_by_css_selector(".fa.fa-history")
        return oplog_list

    def find_dispatch_button(self):
        dispatch_list = browser.find_elements_by_css_selector(".fa.fa-male")
        return dispatch_list

    # 查看日志
    def see_oplog(self):
        try:
            oplogList = browser.find_elements_by_css_selector(".fa.fa-history")
            if len(oplogList) > 0:
                oplogList[0].click()
            else:
                print("当前城市暂无商品出售")
        except Exception as err_msg:
            print(err_msg)

    def print_curTime(self):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))


if __name__ == "__main__":
    # 点开某个页面
    goodWatikiInst = ComOperation()
    goodWatikiInst.openPages(first_level="水票管理", second_level="平台水票管理")

