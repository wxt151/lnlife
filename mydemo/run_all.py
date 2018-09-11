# coding:utf-8
import unittest
import os
import HTMLTestRunner
# import HTMLTestReportCN

# 获取当前文件所在目录
CUR_PATH = os.path.dirname(os.path.realpath(__file__))


def add_case(case_name='Case', rule='test_*.py'):
    # 加载所有的用例
    #case_path = os.path.join(CUR_PATH, case_name)
    case_path = case_name

    # 定义方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    print("用例所在位置 %s  执行的文件 %s " % (case_path, rule))
    return discover


def run_case(all_case, reportName='report'):
    # 设置时间格式
    import time
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    # 报告存放路径
    report_path = os.path.join(os.getcwd(), reportName)

    if not os.path.exists(report_path): os.mkdir(report_path)

    report_abspath = os.path.join(report_path, now + "result.html")
    print("新创建报告文件所在位置 %s " % report_abspath)

    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    # 获取最新的测试报告
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print("最新报告地方 %s" % lists[-1])

    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file

'''
def shangyigebanben():
    case_path = os.path.join(os.getcwd(), "PageWeb\\WebShop\\SystemSetup\\NoticeController")
    # 报告存放路径
    report_path = os.path.join(os.getcwd(), "report")

    # 设置时间格式
    import time
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    # html报告文件
    # report_abspath = os.path.join(report_path, "result" + now + ".html")
    report_abspath = os.path.join(report_path, now + "result.html")

    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="web_*.py",
                                                   top_level_dir=None)

    fp = open(report_abspath, "wb")
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(discover)
    fp.close()

'''
if __name__ == '__main__':
    # shangyigebanben()

    # 加载用例
    all_case = add_case("E:\wxt\lnlife\mydemo","baidu.py")

    # 生成测试报告的路径
    run_case(all_case)
    # 获取最新的而测试报告文件
    report_path = os.path.join(CUR_PATH, "report")  # 报告文件夹
    report_file = get_report_file(report_path)
