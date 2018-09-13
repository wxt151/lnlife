# -*- coding: utf-8 -*-
'''
# 商品库管理
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

def open_goods():
    #点击商品管理
    browser.implicitly_wait(5)
    WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, u"商品管理")))
    browser.find_element_by_link_text("商品管理").click()  # 通过link文字精确定位元素
    time.sleep(1)
    # 展开商品库管理
    locator = (By.LINK_TEXT, "商品库管理")
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located(locator))
    treeview_city_goods = browser.find_element_by_link_text("商品库管理")
    ActionChains(browser).double_click(treeview_city_goods).perform()


def search_setting():
    time.sleep(2)
    # 选择桶装水
    Select(browser.find_element_by_name("category")).select_by_visible_text("桶装水")
    # 桶类型，是否押金
    Select(browser.find_element_by_name("deposit")).select_by_visible_text("免桶押金")
    # 输入商品ID
    browser.find_element_by_css_selector("input[placeholder = '商品编号/名称']").send_keys("6616")
    time.sleep(2)
    # 确定搜索
    browser.find_element_by_css_selector(".fa.fa-search").click()  # class = "fa fa-search"空格使用.代替


def add_goods():
    # 添加商品
    browser.find_element_by_css_selector("div.box-tools").click()
    # 等待页面加载
    # locator = (By.CSS_SELECTOR,"form-control.categorysmall")
    # WebDriverWait(browser,5).until(EC.visibility_of_element_located(locator))
    time.sleep(2)

    Select(browser.find_element_by_name("second_cid")).select_by_visible_text("桶装水")
    Select(browser.find_element_by_name("goods_brands_id")).select_by_visible_text("百崖禄桂")
    browser.find_element_by_id("goodsname").send_keys("百崖禄桂桶装水18L-1")
    # 默认是免桶押金
    browser.find_element_by_css_selector("input[value='2']").click()

    # 上传图片
    """
    # https://jingyan.baidu.com/article/925f8cb8df6f11c0dde056c1.html
    # https://www.cnblogs.com/fnng/p/4188162.html : selenium借助AutoIt识别上传（下载）详解
    """
    import os
    browser.find_element_by_css_selector("object#SWFUpload_0").click()
    os.system("upfile.exe")

    # 向富文本编辑器输入内容 https://blog.csdn.net/ever_mwumli/article/details/77945844
    """
    首先定位到最外面的 iframe 框架:
    进入 iframe 框架：
    定位输入框写入内容：
    """
    iframe =  browser.find_element_by_css_selector("iframe.ke-edit-iframe")
    browser.switch_to_frame(iframe)
    browser.find_element_by_css_selector("body.ke-content").send_keys("新品上市")
    browser.switch_to_default_content()
    # 点击提交后，有可能弹窗提示成功
    time.sleep(15)
    updategoods = browser.find_element_by_css_selector(".btn.btn-primary.materialok")
    # updategoods = browser.find_element_by_id("updategoods") 使用id可以定位到，但是无法提交
    print(updategoods.text)
    updategoods.click()
    print("*****")

    # close_ok_window()

def close_ok_window():
    time.sleep(0.5)
    locator = (By.CSS_SELECTOR,".sweet-alert.showSweetAlert.visible")
    WebDriverWait(browser,3).until(EC.visibility_of_element_located(locator))
    browser.find_element_by_css_selector(".sa-confirm-button-container").click()  # 点击OK

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

#查看日志
def see_logs():
    try:
        time.sleep(1)
        logList = browser.find_elements_by_css_selector(".fa.fa-history")
        if len(logList) > 0:
            logList[0].click()
        else:
            print("没有发布商品")
    except Exception as err_msg:
        print(err_msg)
    # 关闭日志窗口
    close_suspension_window()

#点击取消，关闭悬浮弹窗
def close_suspension_window():
    locator = (By.CSS_SELECTOR, "#myModalLabel")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(locator))
    time.sleep(1)
    browser.find_element_by_css_selector("button[class='close']").click()


#导出列表
def export_excel():
    try:
        time.sleep(1)
        browser.find_element_by_css_selector(".fa.fa-file-excel-o").click()
    except Exception as err_msg:
        print(err_msg)


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
    open_goods()
    # search_setting()
    # add_goods()
    # see_logs()
    # export_excel()
    get_dataTables_info()
