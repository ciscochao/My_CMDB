# coding=utf-8
"""
# @Time    : 9/16/19 2:58 PM
# @Author  : F0rGeEk@root
# @Email   : bat250@protonmail.com
# @File    : handler.py
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
import json
import time
import urllib.parse
import urllib.request
from Client.core import info_collection
from Client.conf import settings


class ArgvHandler(object):
    def __init__(self, args):
        self.args = args
        self.parse_args()

    def parse_args(self):
        """
        分析参数，如果有指定参数则执行，如果没有打印说明
        :return:
        """
        if len(self.args) > 1 and hasattr(self, self.args[1]):
            func = getattr(self, self.args[1])
            func()
        else:
            self.help_msg()

    @staticmethod
    def help_msg():
        # 帮助说明
        msg = '''
       参数名                 功能
       
       collect_data         测试收集硬件信息功能
        
       report_data          收集硬件信息并汇报
       '''
        print(msg)

    @staticmethod
    def collect_data():
        # 收集硬件信息，用于测试
        info = info_collection.InfoCollection()
        asset_data = info.collect()
        print(asset_data)

    @staticmethod
    def report_data():
        # 收集硬件信息并发送至服务端
        info = info_collection.InfoCollection()
        asset_data = info.collect()
        # 将数据打包转换称json格式
        data = {"asset_data": json.dumps(asset_data)}
        # 根据settings中的配置，构造urls
        url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'])
        print("正在将数据发送至:[%s] ..... " % url)

        """使用python自带的request发送post请求，发送前将数据转换为bytes类型"""
        try:
            data_encode = urllib.parse.urlencode(data).encode()
            response = urllib.request.urlopen(url=url, data=data_encode, timeout=settings.Params['request_timeout'])
            print("\033[31;1m发送完毕！\033[0m ")
            message = response.read().decode()
            print("返回结果：%s" % message)
        except Exception as e:
            message = '发送失败' + "错误原因： {}".format(e)
            print("\033[31;1m发送失败！错误原因： %s\033[0m " % e)

        # 记录日志
        # with open(settings.PATH, 'ab') as f:
        with open(settings.PATH, 'ab') as f:
            log = '发送时间： %s \t 服务器地址: %s \t 返回结果：%s \n' % (time.strftime('%Y-%m-%d %H-%M-%S'), url, message)
            f.write(log.encode())
            print('日志已记录完成！')
