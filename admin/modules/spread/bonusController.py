# -*- coding: utf-8 -*-
'''
# 推广管理/红包管理
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.login import logInOut

browser = logInOut.browser
admin = logInOut.LogIn()
admin.login()

def open_bonusController():
    #点击红包管理
    browser.implicitly_wait(5)
    WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, u"推广管理")))
    browser.find_element_by_link_text("推广管理").click()  # 通过link文字精确定位元素
    time.sleep(1)
    # 展开城市商品管理
    locator = (By.LINK_TEXT, "红包管理")
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
    treeview_city_goods = browser.find_element_by_link_text("红包管理")
    ActionChains(browser).double_click(treeview_city_goods).perform()

def switch_bonusSetting():
    # 选择红包设置
    locator = (By.LINK_TEXT, "红包设置")
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
    browser.find_element_by_link_text("红包设置").click()


def send_bonus():
    time.sleep(2)
    # 发放用户
    browser.find_element_by_css_selector("button[data-url='http://admin6.t-lianni.com/seo/bonus/sendred/10153']").click()
    locator = (By.CSS_SELECTOR,"#sendbonusForm")
    WebDriverWait(browser,3).until(EC.visibility_of_element_located(locator))
    #输入用户ID
    browser.find_element_by_css_selector("#userid").send_keys("427909")
    browser.find_element_by_css_selector("#sendFormBut").click()
    click_confirm_window()

#点击确定
def click_confirm_window():
    time.sleep(1)
    locator = (By.CSS_SELECTOR,".sweet-alert.showSweetAlert.visible")
    WebDriverWait(browser,3).until(EC.visibility_of_element_located(locator))
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


#屏蔽红包
def shield_bonus(isShield = True):
    try:
        time.sleep(0.5)
        shieldList = browser.find_elements_by_css_selector("button[data-action='屏蔽']")
        if len(shieldList) > 0:
            shieldList[0].click()
            if isShield:
                # 是的，屏蔽！
                click_confirm_window()
                # OK
                click_confirm_window()
            else:
                click_cancle_window()
        else:
            print("没有可屏蔽的红包")
    except Exception as err_msg:
        print("屏蔽失败：", err_msg)

#激活红包
def activate_bonus(isActivate = True):
    try:
        time.sleep(0.5)
        shieldList = browser.find_elements_by_css_selector("button[data-action='激活']")
        if len(shieldList) > 0:
            shieldList[0].click()
            if isActivate:
                #是的，激活！
                click_confirm_window()
                #OK
                click_confirm_window()
            else:
                click_cancle_window()
        else:
            print("没有可激活的红包")
    except Exception as err_msg:
        print("激活失败：", err_msg)

#创建红包，使用限制一共21种有效组合
def create_bonus(quantity = None,expiresType = 1,limitType = None,boolCreate = True):
    locator  = (By.CSS_SELECTOR,"button[data-url$='seo/bonus/create']")
    WebDriverWait(browser,3).until(EC.visibility_of_element_located(locator))
    browser.find_element_by_css_selector("button[data-url$='seo/bonus/create']").click()
    locator = (By.CSS_SELECTOR,"#myModalLabel")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator))
    if boolCreate:
        css_bonusName = "input[placeholder='红包名称']"
        css_discount = "input[name='discount']"
        css_quantuty = "input[name='quantity']"
        css_expiresType = "input[name='expiresType']" #3个选择
        id_limitType = {
            "Type":"I_Type",
            "Amount":"I_Amount",
            "Category":"I_Category",
            "Items":"I_Items",
            "Area":"I_Area"
        }
        browser.find_element_by_css_selector(css_bonusName).send_keys("测试红包")
        browser.find_element_by_css_selector(css_discount).send_keys("18")
        if quantity is not None:
            browser.find_element_by_css_selector(css_quantuty).send_keys("5") #设置红包个数
        else:
            pass
        #设置有效期类型
        expiresTypeList = browser.find_elements_by_css_selector(css_expiresType)
        if expiresType == 1: #当月有效
            expiresTypeList[0].click()
        elif expiresType == 2:#红包领取之日起x天有效
            expiresTypeList[1].click()
        else:
            expiresTypeList[2].click()
        #使用限制 多种组合，暂不实现
        if limitType is not None:
            # 水票可用
            #browser.find_element_by_id(id_limitType["Type"]).click()
            # 订单（水票）满 x 元可用
            browser.find_element_by_id(id_limitType["Amount"]).click()
            browser.find_element_by_css_selector("input[name = 'amount']").send_keys("5")
            #指定商品类目为，如果红包指定水票可用，则该限制不可
            #document.querySelectorAll('#I_Type')使用js在控制台可以看到这个属性值，但是还不知道如何获取
            typeChecked = browser.find_element_by_id(id_limitType["Type"])
            if False:
                print("红包指定水票可用，则该限制不可用")
                pass
            else:
                browser.find_element_by_id(id_limitType["Category"]).click()
                Select(browser.find_element_by_css_selector("#mainCategory")).select_by_visible_text("其他商品")
            #指定商品（水票）
            browser.find_element_by_id(id_limitType["Items"]).click()
            browser.find_element_by_css_selector("input[name = 'goodsIds']").send_keys("6566")
            #勾选指定地区
            browser.find_element_by_id(id_limitType["Area"]).click()
            Select(browser.find_element_by_css_selector("#city")).select_by_visible_text("柳州市")

            time.sleep(1)
            browser.find_element_by_css_selector("#bonusFormBut").click()
            click_confirm_window()
        else:
            pass
    else:
        css = "div.modal-footer > button.btn.btn-default"
        browser.find_element_by_css_selector(css).click()

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
    open_bonusController()
    # switch_bonusSetting()
    for i in range(1):
        send_bonus()

    #shield_bonus(False)
    #activate_bonus(False)
    #create_bonus(quantity=5, expiresType=1, limitType="all", boolCreate=True)
    # get_dataTables_info()
