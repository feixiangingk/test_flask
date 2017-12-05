#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2017/11/20  10:53
# IDE:         PyCharm
# anthor:      ZT@gufan
from test_SQLAlchemy import create_app

from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(create_app())

class Role(db.Model):
    __tablename__="roles"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),index=True,unique=False)

    def __repr__(self):
        return "<Role {}>".format(self.name)

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=False)
    role_id=db.Column(db.Integer,db.ForeignKey("roles.id"))

    def __repr__(self):
        return "User {}".format(self.username)

def insert_Role():
    admin_role=None
    if Role.query.filter_by(name="Moderator").count()==0:
        mod_role = Role(name="Moderator")
        db.session.add(mod_role)
    if Role.query.filter_by(name="Admin").count()==0:
        admin_role = Role(name="Admin")
        db.session.add(admin_role)
    # db.session.add_all([mod_role,admin_role])
    db.session.commit()

if __name__=="__main__":
    insert_Role()

