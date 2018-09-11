# -*- coding: utf-8 -*-
"""管理后台共用操作类"""

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui

from admin.login import logInOut
browser = logInOut.browser
admin = logInOut.LogIn()
admin.login()

class WebOperator():
    """网页通用操作类"""

    def wait_element_visible(self,locator, timeOut=5):
        """等待页面元素显示"""
        try:
            return ui.WebDriverWait(browser, timeOut).until(EC.visibility_of_element_located(locator))
        except Exception:
            print("元素不可见，返回False")
            return False

    def close_SweetAlert (self):
        """操作结果成功或者失败，关闭弹窗"""
        locator = (By.CSS_SELECTOR, "div.sweet-alert.showSweetAlert.visible")
        Alert_ele = self.wait_element_visible(locator)
        if Alert_ele is not False:
            locator = ".sa-confirm-button-container"
            browser.find_element_by_css_selector(locator).click()
        else:
            print("没有弹窗")
            pass

    def close_modal_content(self):
        """关闭模态框，例如关闭{操作记录}"""
        # locator = (By.CSS_SELECTOR, "h4#myModalLabel.modal-title") #不懂为啥用标题定位不到
        close_btn_css = "div.modal-dialog>div.modal-content>div.modal-header>button.close"
        locator = (By.CSS_SELECTOR, close_btn_css)
        close_btn_ele = self.wait_element_visible(locator)
        if close_btn_ele is not False:
            close_btn_ele.click()
        else:
            # 查看记录，无需刷新页面
            print("刷新页面")
            browser.refresh()

    def commit_confirm_button(self):
        browser.find_element_by_css_selector("#changBut").click()

    def find_oplog_button(self):
        oplog_list = browser.find_elements_by_css_selector(".fa.fa-history")
        return oplog_list

    def find_dispatch_button(self):
        dispatch_list = browser.find_elements_by_css_selector(".fa.fa-male")
        return dispatch_list

if __name__ == "__main__":
    webObj = WebOperator()
    import time
    # 点击订单管理
    time.sleep(2)
    # WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, u"订单管理")))
    browser.find_element_by_link_text("订单管理").click()
    browser.find_element_by_link_text("等待接单").click()  # 通过link文字精确定位元素
    time.sleep(1)

    btn_list = webObj.find_dispatch_button()
    if len(btn_list) > 0:
        btn_list[0].click()
        locator = (By.CSS_SELECTOR,"input.form-control.staff")
        staff_input = webObj.wait_element_visible(locator)
        if staff_input is not False:
            staff_input.send_keys("504840")
            webObj.commit_confirm_button()
            webObj.close_SweetAlert()
            time.sleep(3)
            browser.quit()
    else:
        pass
    # webObj.modal_content()





