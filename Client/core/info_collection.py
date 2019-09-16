# coding=utf-8
"""
# @Time    : 9/16/19 2:59 PM
# @Author  : F0rGeEk@root
# @Email   : bat250@protonmail.com
# @File    : info_collection.py
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
import sys
import platform


class InfoCollection(object):
    # 判断当前平台，根据不同平台选择不同方法进行信息收集
    def collect(self):
        try:
            func = getattr(self, platform.system().lower())
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            sys.exit("不支持当前操作系统: [%s]!" % platform.system())

    @staticmethod
    def linux():
        from ..plugins.collect_linux_info import collect
        return collect()

    @staticmethod
    def windows():
        from ..plugins.collect_windows_info import collect
        return collect()

    @staticmethod
    def build_report_data(data):
        pass
        return data






    def build_report_data(data):
        pass
        return data

