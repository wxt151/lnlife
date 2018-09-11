# -*- coding: utf-8 -*-
"""
# 创建浏览器对象
"""

from selenium import webdriver
"""
方法1,实现__new__方法  
并在将一个类的实例绑定到类变量_instance上,  
如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回  
如果cls._instance不为None,直接返回cls._instance 
"""
# 使用 _instance 创建实例的时候无法带入参数
# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             print("创建浏览器实例")
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#         return cls._instance

class SingleTon(object):
    def __new__(cls, *args, **kwargs):
    #每一次实例化的时候，我们都只会返回这同一个instance
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingleTon, cls).__new__(cls)
        return cls.instance

class BrowserObj(SingleTon):
    def __init__(self,url):
        self.url = url

    def open_browser(self):
        # 创建浏览器对象
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get(self.url)
        # 等待网页加载，加载时间为10s，加载完就跳过
        self.browser.implicitly_wait(10)
        print(self.url, 'open_browser')
        return self.browser

    #   设置手机模式
    def mobile_phone_mode(self):
        try:
            from selenium.webdriver.chrome.options import Options
            # 有效的移动设备Galaxy S5,Nexus 5X,iPhone 8

            # mobile_emulation = {"deviceName": "iPhone 7"}

            mobile_emulation = {
                "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
                "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"}

            # mobile_emulation = {"browserName": "IE"}
            options = Options()
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            return options
        except:
            pass
            # self.writeLog('mobile_phone_mode')

if __name__ == "__main__":
    url = "http://admin6.t-lianni.com"
    browser = BrowserObj(url).open_browser()
    ele_user = browser.find_element_by_name("username")
    ele_user.clear()
    print("ele_user", ele_user)
    ele_user.send_keys("admin")
    ele_pwd = browser.find_element_by_name("password")
    ele_pwd.clear()
    ele_pwd.send_keys("123456")
    ele_login = browser.find_element_by_id("loginBtn")
    ele_login.click()
    