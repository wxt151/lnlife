# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: pymysql_LN.py
@time: 2018/7/30
"""
import json
import pymysql

# from tools.configs.readModel import ReadModel
# from tools.configs import readModel


class PyMysqls(object):
    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(PyMysqls, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    # 数据库和游标一起创建
    def connects_cureors(self, host, port, user, passwd, db, charset):
        # 链接数据库，定义账号密码以及用户名
        self.connect = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            charset=charset
        )
        self.cursor = self.connect.cursor()
        return self.cursor

    def json_str_dumps(self, result):
        # 使用json.dumps将数据转换为json格式，json.dumps方法默认会输出成这种格式"\u5377\u76ae\u6298\u6263"，加ensure_ascii=False，则能够防止中文乱码。
        # JSON采用完全独立于语言的文本格式，事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。
        # json.dumps()是将原始数据转为json（其中单引号会变为双引号），而json.loads()是将json转为原始数据。
        jsondatar = json.dumps(result, ensure_ascii=False)
        # 去除首尾的中括号
        return jsondatar[1:len(jsondatar) - 1]

    def select_all(self, sql):
        # 查询全部数据，key相同储存在一起
        try:
            self.cursor.execute(sql)
            select_results = self.cursor.fetchall()
            # 返回各个字段的属性值，比如长度，是否允许为空 例如('goods_id', 3, None, 10, 10, 0, False)
            desc = self.cursor.description
            results = []
            for clounm in select_results:
                row = {}
                for i in range(0,len(clounm)):
                    row[desc[i][0]] = clounm[i]
                results.append(row)
            return results
        except:
            import traceback
            error = traceback.format_exc()
            print('MySQL connect fail... %s ' % error)

    def select_one(self, sql):
        try:
            self.cursor.execute(sql)
            select_results = self.cursor.fetchone()
            # 返回各个字段的属性值，比如长度，是否允许为空 例如('goods_id', 3, None, 10, 10, 0, False)
            desc = self.cursor.description
            results = {}
            for i in range(0, len(select_results)):
                results[desc[i][0]] = select_results[i]
            return results
        except:
            import traceback
            error = traceback.format_exc()
            print('MySQL connect fail... %s ' % error)

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


if __name__ == '__main__':

    from common.openpyxlExcel import PANDASDATA

    import common.conf_ini as conf
    db = conf.readConfigFile()
    print(db)

    py = PyMysqls()
    py.connects_cureors(host=db["host"],port=int(db["port"]),user=db["user"],passwd=db["passwd"],
                        db=db["db"],charset=db["charset"])


    # py.connects_cureors(host="192.168.10.203",port=3306,user="root",passwd="123456",
    #                     db="lnlife_20180701",charset="utf8")
    # py.connects_cureors(host)
    sql = """
    SELECT * FROM lnsm_city_goods WHERE city = 450100;
    """
    results = py.select_all(sql)
    # results = py.select_one(sql)
    print(results)
    # 数据转换成矩阵
    pan = PANDASDATA(results)
    # 默认列名字典顺序,设置自己的排序列表
    columns = ['id', 'goods_id', 'city', 'price','retail_price',
               'promote_price','sort','status','new_user_preferences',
               'update_time','add_time']
    df = pan.dataFrame(columns=columns)
    df.to_excel(r"E:\wxt\自动化测试资料\Python\Python 编程\pyMysql\0730-1.xlsx",index=False,encoding="utf-8",columns=columns)
    # print(df)

