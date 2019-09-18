# coding=utf-8
"""
# @Time    : 9/18/19 3:07 PM
# @Author  : F0rGeEk@root
# @Email   : bat250@protonmail.com
# @File    : test_assets.py
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

import urllib.request
import urllib.parse

import os
import sys

# BASE_DIR = os.path.dirname(os.getcwd())
# # 设置工作目录，使得包和模块能够正常导入
# sys.path.append(BASE_DIR)
from Client.conf import settings


def update_test(data):
    """
    创建测试用例
    :return:
    """
    # 将数据打包到一个字典内，并转换为json格式
    data = {"asset_data": json.dumps(data)}
    # 根据settings中的配置，构造url
    url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'])
    print('正在将数据发送至： [%s]  ......' % url)
    try:
        # 使用Python内置的urllib.request库，发送post请求。
        # 需要先将数据进行封装，并转换成bytes类型
        data_encode = urllib.parse.urlencode(data).encode()
        response = urllib.request.urlopen(url=url, data=data_encode, timeout=settings.Params['request_timeout'])
        print("\033[31;1m发送完毕！\033[0m ")
        message = response.read().decode()
        print("返回结果：%s" % message)
    except Exception as e:
        message = "发送失败"
        print("\033[31;1m发送失败，%s\033[0m" % e)


if __name__ == '__main__':
    windows_data = {
        "os_type": "Windows",
        "os_release": "10 64bit 1903",
        "os_distribution": "Microsoft",
        "asset_type": "server",
        "cpu_count": 6,
        "cpu_model": "Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz",
        "cpu_core_count": 24,
        "ram": [
            {
                "slot": "A1",
                "capacity": 64,
                "model": "Physical Memory",
                "manufacturer": "kingstone ",
                "sn": "123456"
            },

        ],
        "manufacturer": "LENOVO",
        "model": "Y9000K 2019SE",
        "wake_up_type": 4,
        "sn": "33333-OEM-8992662-133322",
        "physical_disk_driver": [
            {
                "iface_type": "unknown",
                "slot": 0,
                "sn": "34567899876543456787654334566544",
                "model": "SAMSUNG SV100S264G ATA Device",
                "manufacturer": "(标准磁盘驱动器)",
                "capacity": 256
            },
            {
                "iface_type": "SATA",
                "slot": 1,
                "sn": "3123345654323456787654334765423",
                "model": "Seagate SV100S264G ATA Device",
                "manufacturer": "(标准磁盘驱动器)",
                "capacity": 1024
            },

        ],
        "nic": [
            {
                "mac": "14:CF:22:EF:33:33",
                "model": "[00000033] Realtek RTL8192CU Wireless LAN 802.11n USB 2.0 Network Adapter",
                "name": 33,
                "ip_address": "10.8.8.88",
                "net_mask": [
                    "255.255.255.0",
                    "64"
                ]
            },
            {
                "mac": "0A:01:33:33:00:00",
                "model": "[00000333] VmWare WorkStation Host-Only Ethernet Adapter",
                "name": 23,
                "ip_address": "192.168.56.13",
                "net_mask": [
                    "255.255.255.0",
                    "64"
                ]
            },
            {
                "mac": "14:CF:22:FF:48:33",
                "model": "Intel Adapter",
                "name": 17,
                "ip_address": "192.1.1.1",
                "net_mask": ""
            },


        ]
    }

    linux_data = {
        "asset_type": "server",
        "manufacturer": "IBM.",
        "sn": "F3LN113",
        "model": "K1 Power S922",
        "uuid": "4c4c4544-0039-4c10-804e-c6c04f333333",
        "wake_up_type": "Power Switch",
        "os_distribution": "Ubuntu",
        "os_release": "Ubuntu 16.04.4 LTS",
        "os_type": "Linux",
        "cpu_count": "8",
        "cpu_core_count": "32",
        "cpu_model": "POWER 9",
        "ram": [
            {
                "slot": "A1",
                "capacity": 128,
                "model": "Physical Memory",
                "manufacturer": "IBM",
                "sn": "666666"
            }
        ],
        "ram_size": 63.528997344970703,
        "nic": [],
        "physical_disk_driver": [
            {
                "model": "ST1033LM035-1RK001",
                "size": "931.53",
                "sn": "WL109C33"
            }
        ]
    }

    update_test(linux_data)
    update_test(windows_data)
