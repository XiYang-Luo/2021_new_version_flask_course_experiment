# -*- coding: utf-8 -*-
from flask import Blueprint
login = Blueprint("login",__name__)
# 导入蓝图下的模块 蓝图才能映射到对应的路由上
# from . import views
from . import login_server