#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2017/12/7 21:59
# software:     PyCharm


from flask import Flask,render_template
from livereload import Server


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",title="<h2>Hello world</h2>")

@app.route('/services')
def services():
    return "service"

#可以指定多个URL到同一个函数中来
@app.route("/test/")
@app.route("/about")
def about():
    return "about"
if __name__=="__main__":
    live_server=Server(app.wsgi_app)
    #监控文件变化参数是目录e.g:监控static文件夹  static/*.*
    live_server.watch("**/*.*") #监控整个项目
    live_server.serve(open_url=True)