#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2017/12/7 21:59
# software:     PyCharm


from flask import Flask,render_template
from livereload import Server
from flask_script import Manager
from flask import request


app=Flask(__name__)
#要使用热加载功能，必须把debug开关打开
app.config['DEBUG']=True
manager=Manager(app)

@app.route("/")
def index():
    return render_template("index.html", title="<h2>Hello world</h2>")

@app.route('/services')
def services():
    return "service"

#可以指定多个URL到同一个函数中来
@app.route("/test/")
@app.route("/about")
def about():
    return "about"

@manager.command
def dev():
    live_server = Server(app.wsgi_app)
    # 监控文件变化参数是目录e.g:监控static文件夹  static/*.*
    live_server.watch("**/*.*")  # 监控整个项目
    live_server.serve(open_url=True)

@app.template_test("current_url")
def current_url(link):
    #request.url 是 http://127.0.0.1:5500/
    #request.path 是  /

    return link['href'] == request.path


if __name__=="__main__":
    manager.run()   #使用Python sample.py dev启动热加载