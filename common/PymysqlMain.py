# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: pymysql_main.py
@time: 2017/7/13 16:12
"""
import json

import pymysql

# from tools.configs.readModel import ReadModel
# from tools.configs import readModel


class pymysqls(object):
    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(pymysqls, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    # 数据库和游标一起创建
    def connects_cureors(self, host, port, user, passwd, db, charset):
        # 链接数据库，定义账号密码以及用户名
        self.connect = pymysql.Connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            charset=charset
        )
        self.cursor = self.cureors()
        return self.cursor

    # 连接数据库
    # def connects_readModel(self):
    #     conf = readModel.establish_con(model="model")
    #     host = conf.get("database", "host")
    #     port = int(conf.get("database", "port"))
    #     user = conf.get("database", "user")
    #     passwd = conf.get("database", "passwd")
    #     db = conf.get("database", "db")
    #     charset = conf.get("database", "charset")
    #
    #     # 链接数据库，定义账号密码以及用户名
    #     self.connect = pymysql.Connect(
    #         host=host,
    #         port=port,
    #         user=user,
    #         passwd=passwd,
    #         db=db,
    #         charset=charset
    #     )
    #     self.cursor = self.cureors()
    #     return self.connect

    def cureors(self):
        # 通过连接数据来获取游标
        self.cursor = self.connect.cursor()
        return self.cursor

    def json_str_dumps(self, result):
        # 使用json.dumps将数据转换为json格式，json.dumps方法默认会输出成这种格式"\u5377\u76ae\u6298\u6263"，加ensure_ascii=False，则能够防止中文乱码。
        # JSON采用完全独立于语言的文本格式，事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。
        # json.dumps()是将原始数据转为json（其中单引号会变为双引号），而json.loads()是将json转为原始数据。
        jsondatar = json.dumps(result, ensure_ascii=False)
        # 去除首尾的中括号
        return jsondatar[1:len(jsondatar) - 1]

    def total_vertical_selects(self, sql):
        # 查询全部数据，key相同储存在一起
        try:
            self.cursor.execute(sql)
            # 好像是打印字段的属性
            index = self.cursor.description
            # 定义一个容器:列表，
            result = []
            # fetchall():接收全部的返回结果行.
            for res in self.cursor.fetchall():
                # 定义一个字典
                row = {}
                # range(x):表示从0到x，不包括x
                # len:返回字符串、列表、字典、元组等长度
                for i in range(len(index)):
                    # index[i][0] 获取字段里属性中的局部信息

                    row[index[i][0]] = res[i]
                result.append(row)
                # print("selects_list %s" % row)
            return result
        except:
            import traceback
            error = traceback.format_exc()
            print('MySQL connect fail... %s ' % error)

    def single_cross_selects(self, sql):
        # 只查询单个内容，并且是每一行为一个单位
        try:
            self.cursor.execute(sql)
            # 好像是打印字段的属性
            index = self.cursor.description
            # 定义一个字典
            row = {}
            # fetchall():接收全部的返回结果行.
            res = self.cursor.fetchall()[0]

            for i in range(len(index)):
                # index[i][0] 获取字段里属性中的局部信息
                row[index[i][0]] = res[i]

            return row;
        except Exception as msg:
            print('MySQL connect fail... %s ' % msg)

    def closes(self):
        # 关闭游标
        self.cursor.close()
        # 关闭库链接
        self.connect.close()

    def testing(self):
        # 事务处理
        sql_1 = "UPDATE money SET saving = saving + 1000 WHERE account = '18012345678' "
        sql_2 = "UPDATE money SET expend = expend + 1000 WHERE account = '18012345678' "
        sql_3 = "UPDATE money SET income = income + 2000 WHERE account = '18012345678' "

        try:
            self.cursor.execute(sql_1)  # 储蓄增加1000
            self.cursor.execute(sql_2)  # 支出增加1000
            self.cursor.execute(sql_3)  # 收入增加2000
        except Exception as e:
            self.connect.rollback()  # 事务回滚
            print('事务处理失败', e)
        else:
            # 事务提交，如果不提交事务那就插入数据的语句就不会执行
            self.connect.commit()
            print('事务处理成功', self.cursor.rowcount)

#
if __name__ == '__main__':
    sql = ""
    from common.openpyxlExcel import PANDASDATA

    py = pymysqls()
    py.connects_cureors(host="192.168.10.203",port=3306,user="root",passwd="123456",
                        db="lnlife_20180701",charset="utf8")
    sql = """
    SELECT * FROM lnsm_city_goods WHERE city = 450100;
    # """
    results = py.total_vertical_selects(sql)
    print(results)
    # 数据转换
    pan = PANDASDATA(results)
    # daily = ["type", "city", "title", "content", "time", "status", "default"]
    df = pan.dataFrame()
    df.to_excel("0719.xlsx",index=False,encoding="utf-8")
    # print(df)
