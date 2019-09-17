# coding=utf-8
"""
# @Time    : 9/17/19 11:34 AM
# @Author  : F0rGeEk@root
# @Email   : bat250@protonmail.com
# @File    : urls.py
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
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assets/', include('assets.urls')),
]
