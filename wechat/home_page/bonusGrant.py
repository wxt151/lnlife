# -*- coding: utf-8 -*-
'''
# 微信端-首页商品相关操作
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select

from common.browser import BrowserObj
from common.Logger import Log

import numpy as np
import common.openpyxlExcel as ope

url = "http://wechat6.t-lianni.com/login"
driver = BrowserObj(url)
browser = driver.open_browser()


browser.implicitly_wait(5)
log = Log(executor="Root",classification='wechat_home')


def read_buyer_data():
    # import csv
    # file = open(r"E:\wxt\lnlife\common\buyer300.csv", "r")
    # csv_reader = csv.reader(file)
    # #file.close()
    # return csv_reader

    # read = ope.OpenExcelPandas(r"E:\wxt\测试相关\测试用例\用户数据\3万数据.xlsx","3万数据")
    # df_excelData = read.internal_read_excel("用户ID")
    # df_excelData.loc[:,"验证码"] = np.array([5]*len(df_excelData))
    pass

def buyer_login():
    # buyer_phone = read_buyer()
    for row in range(1435,1500):
        funName = log.functionName("buyer_login")
        start_loc = dict(df_excelData.iloc[row])
        log.info("---->第%s行：用户ID:%s 手机：%s"%(row,str(start_loc["买家ID"]),str(start_loc["认证手机"])))
        #登录
        if len(str(start_loc["认证手机"]) ) == 11:
            user_ele = browser.find_element_by_css_selector("input[placeholder = '请输入手机号码']")
            user_ele.send_keys(str(start_loc["认证手机"]))
            pwd_ele = browser.find_element_by_css_selector("input[placeholder = '输入短信验证码']")
            pwd_ele.send_keys("123456")

            browser.find_element_by_id("J_login").click()
            #判断用户是否存在
            locator = (By.CSS_SELECTOR, "div.toast-cont")
            words_ele = wait_element_visible(locator)
            if words_ele and '不存在' in words_ele.text:
                data = words_ele.text
                log.info(data)
                start_loc["验证码"] = data
                df_excelData.iloc[row] = start_loc.values()
                user_ele.clear()
                pwd_ele.clear()
                time.sleep(3)
                continue
            else:
                # 如果未设置密码，暂不设置，如果已经设置密码，直接pass
                close_notice(False)
                # 如果有公告，关闭公告，否则pass
                close_notice(False)
                # 进入首页，领取红包
                data = click_home()

                buyer_logout()

                start_loc["验证码"] = data
                df_excelData.iloc[row] = start_loc.values()

        else:
            data = "手机号不正确"

            log.info(data)
            start_loc["验证码"] = data
            df_excelData.iloc[row] = start_loc.values()
            time.sleep(3)
            continue



#弹窗处理，confirm = True表示确认处理，否则只是关闭
def close_notice(confirm = True):
    time.sleep(1)
    locator = (By.CSS_SELECTOR,".am-dialog-brief")
    notice_ele  = wait_element_visible(locator,2)
    # print("notice_ele",notice_ele)
    if notice_ele:
        # print(notice_ele.text)
        if confirm:
            # 确认 class="am-dialog-button"
            browser.find_element_by_css_selector(".am-dialog-footer>button:nth-child(2)").click()
        else:
            # 取消 class="am-dialog-button cancel"
            browser.find_element_by_css_selector(".am-dialog-footer>button:nth-child(1)").click()
    else:
        # print("notice_ele is null:",notice_ele)
        pass




def click_home():
    time.sleep(1)
    browser.find_element_by_css_selector("a.nav-index").click()
    #browser.refresh()
    # print("弹窗领取红包活动")
    locator = (By.CSS_SELECTOR, "div.toast-cont")
    words_ele = wait_element_visible(locator)
    # print("words_ele", words_ele)
    try:
        if words_ele:
            # print('-------->',words_ele.text)
            funName = log.functionName("click_home")
            log.info(words_ele.text)
            returns = words_ele.text
        else:
                time.sleep(1)
                locator = (By.CSS_SELECTOR, ".close-bonus-btn")
                bonus_ele = wait_element_visible(locator)
                if bonus_ele:
                    bonus_ele.click()
                    log.info("领取红包成功")
                    returns = '领取红包成功'
                else:
                    funName = log.functionName("click_home")
                    log.info("搞鬼了")
                    returns = '搞鬼了'
    except Exception:
        returns = "报错了"
        pass
    finally:
        return  returns

def buyer_logout():
    time.sleep(3)
    browser.find_element_by_css_selector("a.nav-user").click()

    locator = (By.CSS_SELECTOR,"a.head")
    setting_ele = wait_element_visible(locator)
    if setting_ele:
        setting_ele.click()
        browser.find_element_by_link_text("退出登录").click()
        close_notice(confirm = True)
        browser.get(url)
    else:
        log.info("设置失败，强制退出")
        # browser.quit()
        browser.refresh()
        time.sleep(2)
        browser.find_element_by_css_selector("a.nav-user").click()

def wait_element_visible(locator,timeOut = 5):
    try:
        return ui.WebDriverWait(browser,timeOut).until(EC.visibility_of_element_located(locator))
    except Exception:
        return False

if __name__ == "__main__":

    file_path = r"E:\wxt\3W数据量.xlsx"
    file_name_xlsx = r"\数据量100000-11-20-13.xlsx"
    file_name_csv = r"\数据量100000-11-20-13.csv"

    #读取xlsx文件
    read = ope.OpenExcelPandas(file_path ,sheet = "10条数据")
    # 读取csv文件
    # read = ope.OpenExcelPandas(file_path + file_name_csv, sheet=',')
    # 不通过pandas来读取文档
    # read = ope.OpenExcelPandas(file_path + file_name_xlsx, sheet='数据量100000-11-20-13')
    # df_excelData = read.readCaseExcel()
    # print(df_excelData)  #手机号不是文本格式
    df_excelData = read.internal_pandas_read("买家ID")
    print(dict(df_excelData.iloc[2]))
    print(type(df_excelData.iloc[2]))
    print(type(df_excelData))
    df_excelData.loc[:, "验证码"] = np.array([5] * len(df_excelData))


    #
    # try:
    #     buyer_login()
    #     #read_buyer()
    #     # df.to_csv("foo.csv", index=False, encoding="gbk")
    #     df_excelData = df_excelData[1435:1500]
    #     df_excelData.to_csv(r"E:\wxt\测试相关\测试用例\用户数据\1435to1500.csv",index=False, encoding="utf-8")
    # except Exception as err_msg:
    #     log.info(err_msg)
    #     pass

