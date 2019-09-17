# coding=utf-8
"""
# @Time    : 9/16/19 2:59 PM
# @Author  : F0rGeEk@root
# @Email   : bat250@protonmail.com
# @File    : settings.py
# @Software: PyCharm
***********************************************************
███████╗ ██████╗ ██████╗  ██████╗ ███████╗███████╗██╗  ██╗
██╔════╝██╔═████╗██╔══██╗██╔════╝ ██╔════╝██╔════╝██║ ██╔╝
█████╗  ██║██╔██║██████╔╝██║  ███╗█████╗  █████╗  █████╔╝ 
██╔══╝  ████╔╝██║██╔══██╗██║   ██║██╔══╝  ██╔══╝  ██╔═██╗ 
██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗███████╗██║  ██╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
***********************************************************
"""
import os

# 远端接收数据的服务器
Params = {
    "server": "127.0.0.1",
    "port": 8000,
    'url': '/assets/report/',
    'request_timeout': 30,
}

# 日志文件配置

# PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')
PATH = "/root/Python/Projects/My_CMDB/Client/log/cmdb.log"
print(PATH)

# 更多配置，请都集中在此文件中