#coding:utf-8

from flask import Flask,request
#flask重定向
from flask import url_for,redirect
import os
#导入操作cookie的包
from flask import make_response
from flask import render_template

#获取文件真正的名字secure_filename
from werkzeug.utils import secure_filename

#想要指定的URL匹配正则表达式，需用引用
from werkzeug.routing import BaseConverter

# Flask-Script==2.0.5
# livereload==2.3.2   这两个包用于热加载，调试
from flask.ext.script import Manager

# from flask.ext.

class RegexConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegexConverter,self).__init__(url_map)
        self.regex=items[0]


app = Flask(__name__)
#要使用热加载功能，必须把debug开关打开
app.config['DEBUG']=True
manager=Manager(app)


#使用正则表达式转换器
app.url_map.converters["regex"]=RegexConverter

@app.route('/')
def hello_world():
    # request.cookies['']
    return render_template("index.html",title="lesson3")

@app.route('/services')
def services():
    return "service"

#可以指定多个URL到同一个函数中来
@app.route("/test/")
@app.route("/about")
def about():
    return "about"

#动态路由:URL地址带有参数
@app.route("/user/<username>")
def user(username):
    return "username: "+username



#可以指定入参类型，路由转换器
@app.route("/id/<int:user_id>")
def id(user_id):
    return "user_id: {}".format(user_id)

#使用正则表达式
@app.route("/regex/<regex('[a-zA-Z]{3}'):input_arg>")
def regex(input_arg):
    return "regex is: {}".format(input_arg)


#指定方法
@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        print "POST",username,password
    elif request.method=="GET":
        username=request.args.get("username",None)
        password=request.args.get("password",None)
        print "GET",username,password

    #可以和HTML中form表单对应
    return render_template("login.html",method=request.method)

@app.route("/upload",methods=["GET","POST"])
def upload():
    if request.method=="POST":
        f=request.files['file']
        base_path=os.path.abspath(os.path.dirname(__file__))
        upload_path=base_path+"\\static\\uploads\\"
        print upload_path,secure_filename(f.filename)
        f.save(upload_path+secure_filename(f.filename))

        #这里的url_for不需要加  .
        return redirect(url_for("upload"))

    return render_template("upload.html")

#专门处理错误页的路由，需要指定错误码 使用该装饰器errorhandler
@app.errorhandler(404)
def page_not_fond(error):
    return render_template("404.html"),404

#用下面的方法实现热加载,要实现热加载，就必须用Python test_flask.py dev 启动
@manager.command
def dev():
    from livereload import Server
    live_server=Server(app.wsgi_app)
    #监控文件变化参数是目录e.g:监控static文件夹  static/*.*
    live_server.watch("**/*.*") #监控整个项目
    live_server.serve(open_url=True)

if __name__ == '__main__':
    #调试模式
    # app.run(debug=True)
    manager.run()  #使用这种方式启动必须在命令行输入 Python test_flask.py runserver


