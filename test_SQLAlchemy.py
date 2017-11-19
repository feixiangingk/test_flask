#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2017/11/16  17:48
# IDE:         PyCharm
# anthor:      ZT@gufan

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
basedir=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
print app.config['SQLALCHEMY_DATABASE_URI']

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)

app.run(debug=True)
