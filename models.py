#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2017/11/20  10:53
# IDE:         PyCharm
# anthor:      ZT@gufan
from test_SQLAlchemy import db

class Role(db.Model):
    __tablename__="roles"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,index=True)
    def __repr__(self):
        return "<Role {}>".format(self.name)