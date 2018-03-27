#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2017/12/6  9:24
# IDE:         PyCharm
# anthor:      ZT@gufan
import os

from flask import Flask
from flask_bootstrap import Bootstrap  # 引用bootstrap
from flask_nav import Nav  # 使用导航栏需要引入这两个包
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy

# from app.main.views import init_views  #使用蓝图替换


nav=Nav()  #注册导航栏
nav.register_element('top',Navbar(u"Flask基础",
                                  View(u'主页','main.index_demo'),
                                  View(u'重定向','auth.Testredirect'),
                                  View(u'测试函数','main.index'),
                                  View(u'登录','auth.login')))

db=SQLAlchemy()
bootstrap=Bootstrap()



def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')  # 先使用from_pyfile()方法，不然后面的会被覆盖
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    nav.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    # init_views(app)
    from auth import auth as auth_blueprint
    from main import main as main_blueprint
    app.register_blueprint(auth_blueprint,url_prefix="/auth")
    app.register_blueprint(main_blueprint)
    return app


if __name__=="__main__":
    app=create_app()
    app.run("0.0.0.0",port=5006,debug=True)