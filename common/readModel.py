# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: readModel.py
@time: 2017/12/20 23:30
@项目名称:operating
"""
import configparser
import os


def establish_con(model):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    configPath = os.path.join(cur_path, model + ".ini")
    conf = configparser.ConfigParser()
    conf.read(configPath)
    return conf


def url():
    conf = establish_con("excel")
    url = conf.get("excel", "parameterSetting")
    print(url)


def obtain_con(conf):
    email_smtp_server = conf.get("email", "smtp_server")
    email_port = conf.get("email", "port")
    email_sender = conf.get("email", "sender")
    email_psw = conf.get("email", "psw")
    email_receiver = conf.get("email", "receiver")
    print(conf)


if __name__ == '__main__':
    # cur_path = os.path.dirname(os.path.realpath(__file__))
    # configPath = os.path.join(cur_path,"model.ini")
    # conf = configparser.ConfigParser()
    # conf.read(configPath)
    # host = conf.get("database", "host")
    # print(host)
    connn = establish_con("excelmodel")
    syst = connn.get("excel", "systemsetup")
    dail = connn.get("excel", "dailybulletin")
    excel = os.path.join(syst, dail)
    print(excel)
