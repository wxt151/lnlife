"""
订单管理/全部订单
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from admin.modules.comOperation import ComOperation,browser
orderOnlineInst = ComOperation()

def select_time(timeType = "下单时间",dateType = "全部"):
    """
    时间选择
    :param timeType:    1.下单时间 2.派单时间 3.付款时间 4.完成时间
    :param userDefined: 0.今日 1.昨日 2.最近7日 3.最近30日 4.全部 5.自定义
    :return:
    """
    dateDict = {"今日":0,
                "昨日":1,
                "最近7日":2,
                "最近30日":3,
                "全部":4,
                "自定义":5}
    Select(browser.find_element_by_name("time_type")).select_by_visible_text(timeType)
    try:
        browser.find_element_by_id("reservationtime").click()
        timeInput = browser.find_elements_by_css_selector("div.ranges>ul>li")
        if len(timeInput) > 0:
            timeInput[dateDict[dateType]].click()
            if dateDict[dateType] < 5:
                # 指定时间：今日、昨日、最近7日、最近30日、全部
                pass
            else:
                # 自定义时间
                time.sleep(1)
                startTime = browser.find_element_by_name("daterangepicker_start")
                startTime.clear()
                startTime.send_keys("2018-01-01 00:00:00")
                endTime = browser.find_element_by_name("daterangepicker_end")
                endTime.clear()
                endTime.send_keys("2018-11-06 10:30:00")
                browser.find_element_by_css_selector(".applyBtn.btn.btn-small.btn-sm.btn-success").click()
    except Exception:
        pass

def select_label(*labelType):
    labelDict = {'预约': 'label_reserve',
                 '新用户': 'label_newuser',
                 '大客户': 'label_large',
                 '抢购': 'label_seckill',
                 '线下': 'label_offline',
                 '团购': 'label_groupbuy',
                 '水票': 'label_watiki'}
    # new_dict = {v: k for k, v in labelDict.items()}  # 字典键值翻转
    for label in labelType:
        browser.find_element_by_name(labelDict[label]).click()

def select_area(manager = "城西区-周莉",director = "城西区-陈健",shopName = "城西秀灵路配送点"):
    """
    区域：
    :param manager: 区域经理
    :param director:区域主管
    :param shopName: 所属区域
    :return:
    """
    Select(browser.find_element_by_name("manager")).select_by_visible_text(manager)
    time.sleep(0.5)
    Select(browser.find_element_by_name("director")).select_by_visible_text(director)
    time.sleep(0.5)
    Select(browser.find_element_by_name("area")).select_by_visible_text(shopName)

def select_status(type = "平台",status = "交易完成"):
    """
    状态：
    :param type: 订单类型，平台/店铺
    :param status: 订单状态，等待付款/交易关闭/等待派单/待成团/等待配送/配送中/交易完成，结合type使用
    :return:
    """
    Select(browser.find_element_by_name("type")).select_by_visible_text(type)
    time.sleep(0.5)
    Select(browser.find_element_by_name("status")).select_by_visible_text(status)

    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮

def select_order(key = "商品名称",val = "茶花山"):
    """
    订单：
    :param key:订单编号/支付编号/商品ID/商品名称
    :param val: 请输入关键字，结合key值
    :return:
    """
    Select(browser.find_element_by_name("key")).select_by_visible_text(key)
    browser.find_element_by_css_selector("input[name = 'val']").send_keys(val)

def select_buyer(buyerKey = "买家昵称",buyerVal = "桃子"):
    """
    买家：
    :param buyerKey:买家ID/买家昵称/收货人手机
    :param buyerVal:请输入关键字，结合 buyerKey 值
    :return:
    """
    Select(browser.find_element_by_name("buyer_key")).select_by_visible_text(buyerKey)
    browser.find_element_by_css_selector("input[name = 'buyer_val']").send_keys(buyerVal)

def select_other(otherKey = "配送区域ID",otherVal = "82"):
    """
    其他
    :param otherKey:配送区域ID/配送中心ID/配送中心名称/供应商ID/供应商名称/配送点ID/配送点名称
    :param otherVal:请输入关键字，结合 otherKey 值
    :return:
    """
    Select(browser.find_element_by_name("other_key")).select_by_visible_text(otherKey)
    browser.find_element_by_css_selector("input[name = 'other_val']").send_keys(otherVal)

def click_search():
    """
     搜索：点击搜索按钮
    :return:
    """
    # # 时间
    # select_time(timeType="下单时间", dateType="最近30日")
    # select_status(type="平台", status="等待派单")
    browser.find_element_by_css_selector(".fa.fa-search").click()  # 通过类名查找搜索按钮

def order_detail():
    """
    查看订单详情
    :return:
    """
    orderList = browser.find_elements_by_link_text("查看")
    if len(orderList) > 0:
        orderList[0].click()
        browser.back()
    else:
        pass

def order_close():
    """
    关闭订单
    :return:
    """
    # 先过滤出满足条件的订单
    select_time(timeType="下单时间", dateType="最近30日")
    click_search()

    orderList =  browser.find_elements_by_css_selector("button[data-url *= '/order/close']")
    if len(orderList) > 0:
        orderList[0].click()
        locator = (By.CSS_SELECTOR,"input[placeholder = '原因']")
        reasonInput = orderOnlineInst.wait_element_visible(locator)
        if reasonInput is not False:
            reasonInput.send_keys("收货地址错误")
            orderOnlineInst.onclick_confirm()
            time.sleep(1)
            orderOnlineInst.close_SweetAlert()
        else:
            pass
    else:
        pass

def order_reservation():
    """
    转预约
    :return:
    """
    select_time(timeType="下单时间", dateType="最近30日")
    select_status(type="平台", status="等待派单")
    click_search()
    orderList = browser.find_elements_by_css_selector("button[data-url $= 'reservation']")
    if len(orderList) > 0:
        orderList[0].click()
        locator = (By.CSS_SELECTOR, ".form-control.time")
        timeInput = orderOnlineInst.wait_element_visible(locator)
        if timeInput is not False:
            timeInput.send_keys("2018-11-10 17:50:00")
            browser.find_element_by_id("changBut").click()
            time.sleep(1)
            orderOnlineInst.close_SweetAlert()
        else:
            pass
    else:
        pass

def order_dispatch():
    """
    派单
    :return:
    """
    select_time(timeType="下单时间", dateType="最近30日")
    select_status(type="平台", status="等待派单")
    click_search()
    orderList = browser.find_elements_by_css_selector("button[data-url $= 'dispatch']")
    if len(orderList) > 0:
        orderList[0].click()
        locator = (By.CSS_SELECTOR, "input[name = 'staff']")
        # locator = (By.CSS_SELECTOR, ".form-control.staff")
        staffInput = orderOnlineInst.wait_element_visible(locator)
        if staffInput is not False:
            staffInput.send_keys("潘荣飞")
            browser.find_element_by_id("changBut").click()
            time.sleep(1)
            orderOnlineInst.close_SweetAlert()
        else:
            pass
    else:
        pass


def order_change_deliveryman(staffNew = "梁文杭"):
    """
    更换配送员  -- 与派单弹窗一样
    :param staffName : 新的配送员名称
    :return:
    """
    select_time(timeType="下单时间", dateType="最近30日")
    select_status(type="平台", status="等待配送")
    click_search()
    orderList = browser.find_elements_by_css_selector("button[data-url *= 'order/changdeliveryman']")
    if len(orderList) > 0:
        orderList[0].click()
        locator = (By.CSS_SELECTOR, "input[name = 'staff']")
        staffInput = orderOnlineInst.wait_element_visible(locator)
        if staffInput is not False:
            staffDiv = browser.find_element_by_css_selector("div.modal-body > div > div > div:nth-child(3) ") # > label > span:nth-child(1)
            staffCur = staffDiv.text
            if  staffNew in staffCur:
                # 与当前配送员相同
                print("与当前配送员相同，无需更换")
                browser.find_element_by_css_selector("div.modal-content > div.modal-footer > button.btn.btn-default").click()
            else:
                staffInput.send_keys(staffNew)
                browser.find_element_by_css_selector("#changstaffForm").click()
                orderOnlineInst.print_curTime() # 1等待时间测试
                staffExist = orderOnlineInst.wait_SweetAlert_visible()
                orderOnlineInst.print_curTime() # 2等待时间测试
                if staffExist is False:
                    # 配送员存在
                    browser.find_element_by_id("changBut").click()
                    time.sleep(1)
                    submitRes = orderOnlineInst.wait_SweetAlert_visible()
                    print("submitRes:", submitRes.text)
                    if "成功" in submitRes.text:
                        # 正常更换
                        orderOnlineInst.close_SweetAlert()
                        print("更换成功！新的配送员是：",staffNew)
                    else:
                        # 配送员不正确或配送员当前状态不能接单
                        orderOnlineInst.close_SweetAlert()
                        time.sleep(1)
                        browser.find_element_by_css_selector("div.modal-content > div.modal-footer > button.btn.btn-default").click()
                        print("配送员不是正常接单状态...")
                else:
                    # 配送员不存在
                    print("staffExist:", staffExist.text)
                    orderOnlineInst.close_SweetAlert()
                    time.sleep(1)
                    browser.find_element_by_css_selector("div.modal-content > div.modal-footer > button.btn.btn-default").click()
        else:
            print("更换配送员-弹窗失败")
    else:
        print("更换配送员-查找按钮失败")



if __name__ == "__main__":
    orderOnlineInst.openPages(first_level="订单管理", second_level="全部订单")
    order_change_deliveryman()
