#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2017/11/16  17:48
# IDE:         PyCharm
# anthor:      ZT@gufan

from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import os
# from flask.ext.script import Manager
from flask_script import Manager
from flask_bootstrap import Bootstrap
db=SQLAlchemy()

def create_app():
    basedir=os.path.abspath(os.path.dirname(__file__))
    app=Flask(__name__)
    app.config.from_pyfile('settings.py') #先使用from_pyfile()方法，不然后面的会被覆盖

    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
    # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////'+"E:\\SyncWorkSpace\\test_flask\\data.sqlite"
    print app.config['SQLALCHEMY_DATABASE_URI']
    # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

    #sqlalchemy2.0以后SQLALCHEMY_TRACK_MODIFICATIONS代替了SQLALCHEMY_COMMIT_ON_TEARDOWN
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

    app.debug=True
    # bootstrap = Bootstrap(app)
    # manager=Manager(app)
    # >>>from test_SQLAlchemy import db
    # >>>db.create_all()
    # 这步完成以后，就生成了一个data.sqlite文件
    # db.create_all()
    db.init_app(app)
    return app




if __name__=="__main__":

    app=create_app()
    manager=Manager(app)
    manager.run()
    # app.run(debug=True)
