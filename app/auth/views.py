#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/3/27 0:46
# software:     PyCharm
from flask import render_template,request,flash
from .import auth
@auth.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


@auth.route("/login", methods=["GET", "POST"])
def login():
    from app.auth.forms import LoginForm
    loginform = LoginForm()
    if request.method == 'POST':
        flash(u'登录成功')
    return render_template("login_demo.html", title=u"登录", form=loginform)

#重定向到百度首页
@auth.route("/redirect")
def Testredirect():
    return render_template("user_demo.html")