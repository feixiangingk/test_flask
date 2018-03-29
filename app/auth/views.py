#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/3/27 0:46
# software:     PyCharm
from flask import render_template,request,flash,redirect,url_for
from app.models import User
from app import db
from flask_login import login_user,logout_user


from .import auth
@auth.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)

@auth.route("/logout")
def logout():
    user=request.args.get("user")
    logout_user()
    return redirect(url_for("auth.login",message=u"{} 退出成功！".format(user)))

@auth.route("/register",methods=['POST','GET'])
def register():
    from .forms import RegisterForm
    registerForm=RegisterForm()

    if registerForm.validate_on_submit():
        user=User(name=registerForm.username.data,
                  email=registerForm.email.data,
                  password=registerForm.pwd.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login",message=u"{} 注册成功".format(registerForm.username.data)))

    return render_template("register.html",title=u"注册",form=registerForm)



@auth.route("/login", methods=["GET", "POST"])
def login():
    from app.auth.forms import LoginForm
    # print current_app.config['SECRET_KEY']
    loginForm = LoginForm()
    # if request.method == 'POST':
    #     flash(u'登录成功')
    if loginForm.validate_on_submit():
        user=User.query.filter_by(name=loginForm.username.data,password=loginForm.pwd.data).first()
        if user:
            login_user(user)
            return redirect(url_for("main.index_demo",message=u"{} 登录成功".format(user.name))) #为了让客户post之后有一次get请求刷新
        else:
            flash(u"信息认证失败")
    if request.args.get("message"):
        flash(request.args.get("message"))
    return render_template("login_demo.html", title=u"登录", form=loginForm)

#重定向到百度首页
@auth.route("/redirect")
def Testredirect():
    return render_template("user_demo.html")