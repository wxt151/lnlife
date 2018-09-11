# -*- coding: utf-8 -*-
__author__ = 'wxt'
"""
yaml配置文件读写的使用    
@file: conf_yaml.py
@time: 2018/7/30
"""

import yaml

f = open("model.yaml")
y = yaml.load(f)
print(type(y))
