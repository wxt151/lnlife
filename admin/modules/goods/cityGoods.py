# -*- coding: utf-8 -*-
'''
# 城市商品管理
'''

import time
# from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.login import logInOut
browser = logInOut.browser
admin = logInOut.LogIn()
admin.login()

def open_cityController():
    #点击商品管理
    browser.implicitly_wait(5)
    WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, u"商品管理")))
    browser.find_element_by_link_text("商品管理").click()  # 通过link文字精确定位元素
    time.sleep(1)
    # 展开城市商品管理
    locator = (By.LINK_TEXT, "城市商品管理")
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
    treeview_city_goods = browser.find_element_by_link_text("城市商品管理")
    ActionChains(browser).double_click(treeview_city_goods).perform()

def select_city():
    # 选择城市
    locator = (By.LINK_TEXT, "柳州市")
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
    browser.find_element_by_link_text("柳州市").click()

    # 判断是否出现"商品信息",出现则说明页面加载成功
    try:
        locator = (By.CSS_SELECTOR, "#datatatle > thead > tr.active > th:nth-child(1)")
        WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator))
    except Exception as err_msg:
        print("无法加载页面:%s", err_msg)

def search_setting():
    time.sleep(2)
    # 选择商品状态
    Select(browser.find_element_by_name("status")).select_by_visible_text("已下架")
    # 选择桶装水
    Select(browser.find_element_by_name("category")).select_by_visible_text("桶装水")
    #新用户优惠
    Select(browser.find_element_by_name("preferences")).select_by_visible_text("参加")
    # 输入商品ID
    browser.find_element_by_css_selector("input[placeholder = '商品编号/名称']").send_keys("6566")
    time.sleep(2)
    # 确定搜索
    browser.find_element_by_css_selector(".fa.fa-search").click()  # class = "fa fa-search"空格使用.代替

def first_shelf():
    # 首次上架商品
    try:
        browser.find_element_by_css_selector("button[data-url$='goods/sale']").click()
        # 等待出现弹窗标题【xx市】上架商品
        locator = (By.ID, "myModalLabel")
        WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator))
    except Exception as err_msg:
        print("上架商品失败：", err_msg)

    try:
        browser.find_element_by_css_selector("input.select2-search__field").send_keys("6652")
        time.sleep(1)
        #等待显示搜索结果
        locator = (By.CSS_SELECTOR, "ul.select2-results__options>li")
        WebDriverWait(browser, 4).until(EC.visibility_of_any_elements_located(locator))
        goodsList = browser.find_elements_by_css_selector("li[class^='select2-results__option']")  # 类名以value值开头
        resultText = goodsList[0].text
        if resultText == "未找到结果":
            print("未找到结果,请重新输入商品ID/名称")
            browser.find_element_by_css_selector("div.modal-footer > button.btn.btn-default").click()
        else:
            goodsList[0].click()
            #判断是否弹出自定义对话框
            locator = (By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible")
            isEverSale = EC.visibility_of_element_located(locator)
            if isEverSale == False:
                #输入的商品第一次上架，没有弹窗直接设置
                set_goodsInfo()
            else:
                # 获取弹窗内容，判断是已经上架出售，还是使用之前上架过的初始数据
                tipsText = browser.find_element_by_css_selector(".sweet-alert.showSweetAlert.visible").text
                isSaleAlready = "该商品已在当前城市上架出售"
                #该商品已在当前城市上架出售
                if isSaleAlready in tipsText:
                    print(isSaleAlready)
                    close_ok_window()
                    #取消{上架商品}
                    time.sleep(1)
                    #browser.find_element_by_css_selector("button:contains('取消')").click()  ???这种定位方式不行吗
                    browser.find_element_by_css_selector("div.modal-footer > button.btn.btn-default").click()
                    #body > div.modal.fade.in > div > div > div.modal-footer > button.btn.btn-default
                #这款商品之前有在该城市上架过
                else:
                    isSaleBefore = "这款商品之前有在该城市上架过"
                    print(isSaleBefore)
                    browser.find_element_by_css_selector(".sa-confirm-button-container").click()  # 是的，使用之前上架的数据
                    time.sleep(1)
                    browser.find_element_by_css_selector(".btn.btn-primary").click() #确定提交
                    close_ok_window()
    except Exception as err_msg:
        print("first_shelf",err_msg)

def close_ok_window():
    time.sleep(0.5)
    locator = (By.CSS_SELECTOR,".sweet-alert.showSweetAlert.visible")
    WebDriverWait(browser,3).until(EC.visibility_of_element_located(locator))
    browser.find_element_by_css_selector(".sa-confirm-button-container").click()  # 点击OK

def set_goodsInfo():
    try:
        time.sleep(2)
        browser.find_element_by_css_selector("#goodsForm > div:nth-child(3) > div > input").send_keys("18")  # 市场价
        browser.find_element_by_css_selector("#goodsForm > div:nth-child(4) > div > input").send_keys("15")  # 连你价
        browser.find_element_by_css_selector("#goodsForm > div:nth-child(5) > div > input").send_keys("10")  # 促销价
        browser.find_element_by_css_selector("#goodsForm > div:nth-child(6) > input").send_keys("132")  # 排序
        browser.find_element_by_css_selector("input[name='preferences']").click()  # 新用户优惠
        #browser.find_element_by_id("goodsFormBut").click() #确定按钮
    except Exception as err_msg:
        print("上架商品失败：%s", err_msg)


#编辑商品
def edit_cityGoods():
    #找到编辑按钮
    editList = browser.find_elements_by_css_selector("button[data-action='编辑']") #查找多个
    if len(editList) > 0:
        editList[0].click()
    else:
        print("当前城市暂无商品出售")
    # 等待编辑弹窗出现
    locator = (By.CSS_SELECTOR, "#myModalLabel")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator))
    browser.find_element_by_css_selector("#goodsFormBut").click()
    # 编辑成功，点击OK
    close_ok_window()



#下架商品
def put_off_shelves():
    # 找到下架按钮
    try:
        time.sleep(1)
        offList = browser.find_elements_by_css_selector("button[data-action='下架']")
        if len(offList) > 0:
            offList[0].click()
        else:
            print("当前城市暂无商品出售")
    except Exception as err_msg:
        print(err_msg)

    # 等待{你确认要下架}
    wait_popup_window()
    browser.find_element_by_css_selector(".sa-confirm-button-container").click()
    # 操作成功，点击OK
    close_ok_window()

def wait_popup_window():
    # 等待{你确认要下架}
    time.sleep(1)
    locator = (By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible")
    WebDriverWait(browser,4).until(EC.visibility_of_element_located(locator))


#查看日志
def see_operate_logs():
    try:
        time.sleep(1)
        logList = browser.find_elements_by_css_selector(".fa.fa-history")
        if len(logList) > 0:
            logList[0].click()
        else:
            print("当前城市暂无商品出售")
    except Exception as err_msg:
        print(err_msg)
    # 关闭日志窗口
    close_suspension_window()


#导出列表
def export_excel():
    try:
        time.sleep(1)
        browser.find_element_by_css_selector(".fa.fa-file-excel-o").click()
    except Exception as err_msg:
        print(err_msg)


#查看结算信息
def settlement_info():
    try:
        settlementList = browser.find_elements_by_css_selector("button[data-action='查看结算信息']")
        if len(settlementList) > 0:
            settlementList[0].click()
        else:
            print("当前城市暂无商品出售")
    except Exception as err_msg:
        print(err_msg)
    #查看后要手动关闭悬浮窗
    close_suspension_window()

#点击取消，关闭悬浮弹窗
def close_suspension_window():
    locator = (By.CSS_SELECTOR, "#myModalLabel")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator))
    time.sleep(1)
    browser.find_element_by_css_selector("button[class='close']").click()


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
    pass
    open_cityController()
    # select_city()
    #search_setting()
    #first_shelf()
    #edit_cityGoods()
    #put_off_shelves()
    #see_operate_logs()
    #export_excel()
    #settlement_info()
    # get_dataTables_info()