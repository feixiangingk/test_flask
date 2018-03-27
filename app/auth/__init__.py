#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/3/27 0:43
# software:     PyCharm

#使用蓝图组织代码
from flask import Blueprint
auth=Blueprint("auth",__name__)
import views
