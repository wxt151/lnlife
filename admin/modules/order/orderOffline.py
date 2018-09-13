"""
订单管理/线下订单
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from admin.modules.comOperation import ComOperation,browser
orderOfflineInst = ComOperation()

def order_add():
    """
    生成线下订单
    :return:
    """
    browser.find_element_by_css_selector("button[data-url $= '/order/add']").click()
    try:
        locator = (By.NAME, "phone")
        nameInput = orderOfflineInst.wait_element_visible(locator,5)
        nameInput.send_keys("13878857334")
        browser.find_element_by_css_selector("#phoneform > div:nth-child(2) > ul").click()
        time.sleep(1)
        browser.find_element_by_id("phoneFormBut").click()
    except Exception as errMsg :
        print(errMsg)

    try:
        browser.find_element_by_css_selector("div.addresslist.more > div:nth-child(2)").click()
        payType = browser.find_elements_by_css_selector("input[name = 'paytype']")
        payType[1].click()
        browser.find_element_by_css_selector(".col-md-12.J-addgood").click()
    except Exception as errMsg:
        print(errMsg)
    # 添加商品
    try:
        addBtn = browser.find_elements_by_css_selector(".changnum.increase")
        if len(addBtn) > 0 :
            addBtn[1].click()
            browser.find_element_by_id("addgoodsBut").click()
            # 选择送达时间
            Select(browser.find_element_by_id("J_deliveryDay")).select_by_visible_text("11月09日 今天")
            Select(browser.find_element_by_id("J_deliveryHour")).select_by_visible_text("尽快送达")
            browser.find_element_by_id("noteorder").send_keys("订单要尽快送达哦")
            browser.find_element_by_id("noteoperation").send_keys("自动化下单的")
            browser.find_element_by_id("orderFormBut").click()
            orderOfflineInst.close_SweetAlert()
        else:
            print("该收货地址没有商品")
    except Exception as errMsg:
        print(errMsg)

if __name__ == "__main__":
    orderOfflineInst.openPages(first_level="订单管理", second_level="线下订单")
    order_add()