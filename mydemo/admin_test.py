# -*- coding: utf-8 -*-
# 玩玩而已，别当真
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get("http://admin6.t-lianni.com")

browser.maximize_window()
#登录
browser.find_element_by_name("username").send_keys("admin")
browser.find_element_by_name("password").send_keys("123456")
browser.find_element_by_id("loginBtn").click()

#点击订单管理
#https://www.cnblogs.com/qingchunjun/p/4208159.html  定位方法
time.sleep(3)
browser.find_element_by_xpath("//*[text()='订单管理']").click() #绝对路径/html/body/div[1]/aside/section/ul/li[2]/a/span


#打开全部订单并选择等待派单
time.sleep(2)
orderOnline = browser.find_element_by_xpath("//a[contains(@href, 'online')]") # "//a[contains(@href, ‘logout’)]"  ， "//*[text()=’全部订单’]"
ActionChains(browser).double_click(orderOnline).perform()
time.sleep(3)


# 选择派单时间 （下拉框处理）
Select(browser.find_element_by_name("time_type")).select_by_visible_text("派单时间")#select_by_visible_text("派单时间") #select_by_value("2")
dropDown = browser.find_element_by_name("timename").click()
time = browser.find_element_by_xpath("//*[text()='最近30日']").click()

#选择订单状态
Select(browser.find_element_by_name("type")).select_by_visible_text("平台")
Select(browser.find_element_by_name("status")).select_by_visible_text("等待配送")

'''
#选择订单编号
Select(browser.find_element_by_name("key")).select_by_visible_text("订单编号")
orderNum = browser.find_element_by_xpath("//input[@name='val']")
orderNum.send_keys("1546155214010219")
'''
#确定搜索
browser.find_element_by_xpath("//*[contains(text(),'搜索')]").click() #//*[text()='搜索'] 由于有空格，需要使用模糊查找

#更换配送员  （对话框处理）
browser.find_element_by_xpath("//button[contains(@data-url,'1526374495010337')]").click()
#browser.find_element_by_class_name("modal-content").find_element_by_css_selector("input[placeholder='配送员姓名/手机/ID']").send_keys("11325") #css_selector定位
# browser.find_element_by_css_selector(".form-control.staff").send_keys("11325") #css_selector定位

import time
time.sleep(3) #为何需要重新导入？否则报错，命名空间没有被破坏啊
browser.find_element_by_css_selector("#changstaffForm > div:nth-child(1) > input.form-control.staff").send_keys("11325") #css_selector定位
#div = browser.find_element_by_class_name("modal-content").find_element_by_xpath("//input[@type='text']")  #二次定位
#print(div)


#changDelyman = browser.find_element_by_class_name("form-group").find_element_by_name("deliveryman_id")
#changDelyman.clear().send_keys("11325")
'''

changDeliveryman = browser.find_element_by_xpath("//input[@name='staff' and class='form-control staff']").click()
changDeliveryman.clear().send_keys("11325")
browser.find_element_by_class_name("btn btn-primary").click()

'''