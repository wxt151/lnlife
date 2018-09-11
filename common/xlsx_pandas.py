# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: OpenpyxlExcel.py
@time: 2017/12/9 18:39
@项目名称:operating
http://openpyxl.readthedocs.io/en/latest/ 读取excel
http://blog.csdn.net/tanzuozhev/article/details/76713387 pandas迭代
http://www.cnblogs.com/chaosimple/p/4153083.html 十分钟搞定pandas
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.set_index.html 官网
https://pandas.pydata.org/pandas-docs/stable/index.html官网
https://www.cnblogs.com/en-heng/p/5630849.html 函数解释
https://jingyan.baidu.com/article/36d6ed1f6c54b01bcf488312.html pandas数据合并
"""

import os
import sys
import time

import pandas as pd


file_name = r"E:\wxt\3W数据量.xlsx"
sheet_name="10条数据"

def read_excel_xlsx(file_name,sheet_name):
    """
    返回一个矩阵，index值从0~n
    :param file_name: 文件名，涵盖路径
    :param sheet_name: 工作簿sheet名
    :return:
    """
    # pandas读取xlsx数据
    df = pd.read_excel(file_name,sheet_name )
    return df

def dict_to_dataFram(data = None,index = None,columns = None,dtype = None,copy = False):
    """
    将字典数据转换为矩阵
    :param data: 字典d = {'col1': [1, 2], 'col2': [3, 4]}
    :param index:序列号，可以设置，默认从0~n
    :param columns: 列名,取字典的keys值
    :param dtype:数据类型，默认为int64
    :param copy: 默认为False
    :return:返回一个矩阵
    """
    df = pd.DataFrame(data,index,columns)
    return df


def set_df_index(df,column):
    """
    :param df: 需要设置的矩阵数据
    :param column: 目标数据值 比如column = list(df["买家ID"])
    :return:新的矩阵，index = column
    """
    df = df.set_index([column])
    # return df
    return df.fillna(value='')

def get_df_index_value():
    df = read_excel_xlsx(file_name, sheet_name)
    column = list(df["买家ID"])
    df = set_df_index(df,column)
    index_value = df.loc[250326] #已经重置过索引值
    # index_value = df.iloc[0] #原始索引值为0
    return dict(index_value)#返回某一行的数据，将矩阵转换为字典形式返回

if __name__ == '__main__':
    df = read_excel_xlsx(file_name, sheet_name)
    dict_data = df.index
    print(type(dict_data))
    print(dict_data)
    for i in dict_data:
        print(df.iloc[i])