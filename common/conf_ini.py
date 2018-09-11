# -*- coding: utf-8 -*-
__author__ = 'wxt'
"""
ini配置文件读写的使用    
@file: conf_ini.py
@time: 2018/7/30
"""

import configparser

iniFileUrl="model.ini"
conf=configparser.ConfigParser() #生成conf对象
conf.read(iniFileUrl)   #读取ini配置文件

def readConfigFile():
    """
    sections:配置文件中[]中的值
    options:每组中的键
    items:键-值的列表形式
    """
    # # 获取每组类型中的section值
    # sections = conf.sections()  # 获取所有sections
    # print("---.ini文件中的section内容有：", sections)
    #
    # # 获取每行数据的键即指定section的所有keys值
    # sections_keys = conf.options(sections[0])
    # print("---database的所有键为：", sections_keys)
    #
    # # 指定section，option读取具体值
    # sections_value = conf.get(sections[0], sections_keys[4])
    # print("---database组的db值为：",sections_value )

    # 获取指定section的所有键值对
    sections_list = conf.items("database")
    # print("---database 的所有键-值为：", sections_list)

    sections_dict = dict(sections_list)
    # print(sections_dict)
    return sections_dict

def writeConfigFile():
    """
    根据分组名、键名修改为新键值
    @param sections: section分组名
    @param key: 分组中的key
    @param newvalue: 需要修改后的键值
    """
    conf.set("database", "db", "lnlife_20180716")  # 指定section和option则更新value

    conf.add_section("testwxt")  # 添加section组
    conf.set("testwxt", "d_key1", "value1")  # 给添加的section组增加option-value
    # 写回配置文件
    conf.write(open(iniFileUrl, "wb"))

if __name__ == "__main__":
    readConfigFile()
    # writeConfigFile()