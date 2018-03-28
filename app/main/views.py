#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/3/25 21:49
# software:     PyCharm
from flask import flash  # 显示登录成功 提示信息
from flask import render_template, current_app, request,url_for
from flask import redirect
from .import main

# def init_views(app):
#     #显式调用current_app  设置count属性，初始值=0


@main.route("/index_demo",endpoint="index_demo") #由于使用蓝图模式，这里的endpoint还是会自动变成mian.index_demo
def index_demo():
    print "index_demo endpoint:",request.endpoint
    return render_template("index_demo.html")

@main.app_template_test("current_link")
def is_current_link(link):
    return link == request.path


@main.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap_a.html")

@main.route("/")
def index():
    print "index_demo /:", request.endpoint
    user_agent=request.headers.get("User-Agent")
    print current_app.name #显示test_SQLAlchemy因为程序实例化在该模块
    current_app.count+=1
    print current_app.count
    # print app.url_map #url_map查看URL和视图函数之间的映射
    # return '<p>your browser is {} </p>'.format(user_agent)
    return redirect(url_for("main.index_demo"))

@main.route("/count",methods=["GET","POST"])
def count():
    if not hasattr(current_app,"count"):
        current_app.count=0
    current_app.count+=1 #测试成功，可以作为全局app容器管理全局变量
    return "current_app.count is {}".format(current_app.count)



#专门处理错误页的路由，需要指定错误码 使用该装饰器errorhandler
@main.errorhandler(404)
def page_not_fond(error):
    return "not this views!",404



