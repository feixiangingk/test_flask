#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2017/11/20  11:08
# IDE:         PyCharm
# anthor:      ZT@gufan

from flask_script import Manager
from test_SQLAlchemy import create_app
app=create_app()
manager=Manager(app)

if __name__=="__main__":
    #必须要此行，才能接受
    manager.run()