#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2017/12/6  9:24
# IDE:         PyCharm
# anthor:      ZT@gufan
from flask import request
from test_SQLAlchemy import create_app
from flask import current_app #程序上下文，当前激活程序的程序实例
from flask import redirect,render_template

app=create_app()
#显式调用current_app  设置count属性，初始值=0
with app.app_context():
    current_app.count=0


@app.route("/")
def index():
    user_agent=request.headers.get("User-Agent")
    print current_app.name #显示test_SQLAlchemy因为程序实例化在该模块
    current_app.count+=1
    print current_app.count
    print app.url_map #url_map查看URL和视图函数之间的映射
    return '<p>your browser is {} </p>'.format(user_agent)

@app.route("/count",methods=["GET","POST"])
def count():
    if not hasattr(current_app,"count"):
        current_app.count=0
    current_app.count+=1 #测试成功，可以作为全局app容器管理全局变量
    return "current_app.count is {}".format(current_app.count)

#重定向到百度首页
@app.route("/redirect")
def Testredirect():
    return redirect("http://www.baidu.com")

#专门处理错误页的路由，需要指定错误码 使用该装饰器errorhandler
@app.errorhandler(404)
def page_not_fond(error):
    return "not this views!",404

@app.route("/user/<name>")
def user(name):
    return render_template("user.html",name=name)

if __name__=="__main__":
    app.run(debug=True)
