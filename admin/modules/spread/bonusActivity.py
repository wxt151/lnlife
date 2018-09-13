# -*- coding: utf-8 -*-
'''
# 推广管理/领取红包活动
'''

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from admin.modules.comOperation import ComOperation,browser
bonusActivityInst = ComOperation()

def additional_bonus_activity():
    """
    追加已经结束的活动
    :return:
    """
    filter_condition(status = "已结束")
    additionBtn = browser.find_elements_by_css_selector("button[data-url *= '/bonus_activity/additional']")
    if len(additionBtn) > 0:
        additionBtn[0].click()
        locator = (By.ID, "number")
        numInput = bonusActivityInst.wait_element_visible(locator)
        if numInput is not False:
            numInput.send_keys("3")
            browser.find_element_by_id("reservationtime").send_keys("2018/11/02 00:00:00 - 2018/11/02 23:59:59")
            browser.find_element_by_css_selector(".applyBtn.btn.btn-small.btn-sm.btn-success").click()
            browser.find_element_by_id("traceBut").click()
            bonusActivityInst.onclick_confirm()
        else:
            pass
    else:
        pass

def create_bonus_activity():
    """
    创建活动二维码
    :return:
    """
    browser.find_element_by_css_selector("button[data-url *= '/bonus_activity/create']").click()
    locator = (By.ID,"activityname")
    nameInput = bonusActivityInst.wait_element_visible(locator)
    if nameInput is not False:
        nameInput.send_keys("测试定时器-红包活动状态")
        # 获取当前时间,便于调试，否则直接输入时间比较方便
        import datetime
        curTiem = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        delayTime = datetime.datetime.now() + datetime.timedelta(minutes=3)
        delayTimeD = delayTime.strftime('%Y-%m-%d %H:%M:%S')
        reservationTime = curTiem + " - " + delayTimeD
        print(reservationTime)
        browser.find_element_by_id("reservationtime").send_keys(reservationTime)
        browser.find_element_by_css_selector(".applyBtn.btn.btn-small.btn-sm.btn-success").click()
        Select(browser.find_element_by_name("activityobject")).select_by_visible_text("不限")
        browser.find_element_by_id("bonus").send_keys("10086")
        browser.find_element_by_id("bonusnum").send_keys("2")
        browser.find_element_by_id("activityBut").click()
        # 提交后，操作成功与否均会返回操作结果
        bonusActivityInst.onclick_confirm()
    else:
        pass

def edit_bonus_activity():
    filter_condition(status = "未开始")
    editBtn = browser.find_elements_by_css_selector("button[data-url *= '/bonus_activity/edit']")
    if len(editBtn) > 0:
        editBtn[0].click()
        locator = (By.ID, "activityname")
        nameInput = bonusActivityInst.wait_element_visible(locator)
        if nameInput is not False:
            nameInput.clear()
            nameInput.send_keys("红包活动状态-编辑")
            reservationTime = "2018/11/05 15:30:12 - 2018-11-15 15:40:12"
            browser.find_element_by_id("reservationtime").send_keys(reservationTime)
            browser.find_element_by_css_selector(".applyBtn.btn.btn-small.btn-sm.btn-success").click()
            time.sleep(2)
            # Select(browser.find_element_by_name("activityobject")).select_by_visible_text("不限制")
            # browser.find_element_by_id("bonus").send_keys("10086")
            # browser.find_element_by_id("bonusnum").send_keys("2")
            browser.find_element_by_id("editActivityBut").click()
            # 提交后，操作成功与否均会返回操作结果
            bonusActivityInst.onclick_confirm()
        else:
            pass
    else:
        pass

def finish_bonus_activity():
    """
    结束正在进行中的活动
    :return:
    """
    filter_condition(status = "进行中")
    finishBtn = browser.find_elements_by_css_selector("button[data-url *= '/bonus_activity/finish']")
    if len(finishBtn) > 0:
        finishBtn[0].click()
        bonusActivityInst.onclick_confirm()
        time.sleep(0.5)
        bonusActivityInst.close_SweetAlert()
    else:
        print("没有进行中状态的活动")


def filter_condition(status = "活动状态"):
    """
     搜索：选择过滤条件
    :return:
    """
    Select(browser.find_element_by_name("status")).select_by_visible_text(status)   # 活动状态
    # Select(browser.find_element_by_name("type")).select_by_visible_text("请选择")
    # browser.find_element_by_name("key").send_keys("")   # 输入搜索字段
    # 点击搜索按钮
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮


def oplog_bonus_activity():
    """
    活动记录
    :return:
    """
    oplogBtn = browser.find_elements_by_css_selector("button[data-url *= '/bonus_activity/oplog']")
    if len(oplogBtn) > 0:
        oplogBtn[0].click()
        bonusActivityInst.close_modal_content()
    else:
        pass



if __name__ == "__main__":
    bonusActivityInst.openPages(first_level = "推广管理",second_level = "领取红包活动")
    oplog_bonus_activity()










