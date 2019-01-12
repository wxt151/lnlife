from selenium import webdriver
from time import sleep

mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

browser = webdriver.Chrome(chrome_options=options)
browser.get('http://wechat8.t-lianni.com/quick')

browser.find_element_by_link_text("首页").click()
sleep(1)
addGoodsBtn = browser.find_elements_by_css_selector(".J_add.shop-goods-add.icon-font.icon-plus-str")
addGoodsBtn[0].click()
sleep(1)
print("999999999999999")
browser.find_element_by_css_selector(".J_goBuy.m-cart-by")
ele = browser.find_element_by_link_text("去结算")
print(ele.text)
ele.click()
print("8888888888888888888")