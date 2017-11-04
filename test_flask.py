#coding:utf-8

from flask import Flask,request
from flask import render_template

#想要指定的URL匹配正则表达式，需用引用
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegexConverter,self).__init__(url_map)
        self.regex=items[0]


app = Flask(__name__)

#使用正则表达式转换器
app.url_map.converters["regex"]=RegexConverter

@app.route('/')
def hello_world():
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
    #可以和HTML中form表单对应
    return render_template("login.html",method=request.method)


if __name__ == '__main__':
    #调试模式
    app.run(debug=True)
