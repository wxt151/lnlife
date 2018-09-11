# -*- coding: utf-8 -*-
"""
# 创建浏览器对象
"""

from selenium import webdriver

class BrowserObj(object):
    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(BrowserObj, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def single_browser(self):
        # 返回已经创建了的浏览器对象
        return self.browser

    def chrome_browser(self):
        try:
            self.browser = webdriver.Chrome()
            # 实现全局变量的引用
        except Exception as msg:
            self.writeLog()

    # 运行浏览器
    def url_opens(self, url=None):

        print("浏览器开始执行初始化")

        # 创建浏览器对象
        self.chrome_browser()
        self.browser.maximize_window()

        self.browser.get(url)
        # 等待网页加载，加载时间为10s，加载完就跳过
        self.browser.implicitly_wait(10)

        print("浏览器打开完毕..........")
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
            self.writeLog('mobile_phone_mode')