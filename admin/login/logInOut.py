# -*- coding: utf-8 -*-
'''管理员登录'''

from selenium import webdriver
import time
from common.browser import BrowserObj

url = "http://admin6.t-lianni.com/"
driver = BrowserObj(url)
browser = driver.open_browser()

class LogIn(object):
    def __init__(self,username = "admin",password = "123456"):
        self.username = username
        self.password = password

    def login(self):
        try:
            ele_user = browser.find_element_by_name("username")
            ele_user.clear()
            ele_user.send_keys(self.username)
            ele_pwd = browser.find_element_by_name("password")
            ele_pwd.clear()
            ele_pwd.send_keys(self.password)
            ele_login = browser.find_element_by_id("loginBtn")
            ele_login.click()
            time.sleep(1)
        except Exception as err_msg:
            print(err_msg)
            import os, datetime
            cur_path = os.path.dirname(__file__)
            log_path = cur_path + "/log/"
            basename = os.path.splitext(os.path.basename(__file__))[0]  # 获取当前文件的文件名
            logFileName = basename + "-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "error.png"
            browser.get_screenshot_as_file(log_path + logFileName)

class LogOut(object):
    @classmethod
    def logout(self):
        browser.find_element_by_xpath("//span[contains(text(),'admin')]").click()
        time.sleep(1)
        browser.find_element_by_link_text("登出").click()
        time.sleep(1)

    @classmethod
    def quit(self):
        browser.quit()

if __name__ == "__main__":
   admin = LogIn("admin","123456")
   print(admin)
   admin.login()
   LogOut.logout()
