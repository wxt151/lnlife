# -*- coding: utf-8 -*-
"""
# 创建浏览器对象
"""

from selenium import webdriver

# 解决弹窗请安装Flash的问题
from selenium import webdriver
# 设置selenium 自动加载flash  https://blog.csdn.net/weixin_41607151/article/details/80486964
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
prefs = {
    "profile.managed_default_content_settings.images":1,
    "profile.content_settings.plugin_whitelist.adobe-flash-player":1,
    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player":1,
}
chromeOptions.add_experimental_option('prefs',prefs)
# driver = webdriver.Chrome(chrome_options=chromeOptions)

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
        self.browser = webdriver.Chrome(chrome_options=chromeOptions)
        self.browser.maximize_window()
        self.browser.get(self.url)
        # 等待网页加载，加载时间为10s，加载完就跳过，隐性等待这个时间如果最长，系统会选择这个最长时间作为超时时间
        self.browser.implicitly_wait(3)
        return self.browser

    #   设置手机模式
    def mobile_phone_mode(self):
        try:
            from selenium.webdriver.chrome.options import Options
            # 用chrome的Mobile emulation模拟手机浏览器测试手机网页
            # https://blog.csdn.net/huilan_same/article/details/52856200

            # 第一种方法：device name来确定我们要模拟的手机样式
            # mobile_emulation = {"deviceName": "iPhone 7"}

            # 第二种方法：直接指定分辨率以及UA标识
            mobile_emulation = {
                "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
                "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"}

            options = Options()
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            return options
        except:
            pass
            # self.writeLog('mobile_phone_mode')

if __name__ == "__main__":
    url = "http://wechat7.t-lianni.com/"
    browser = BrowserObj(url)
    browser.mobile_phone_mode()