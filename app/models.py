#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2017/11/20  10:53
# IDE:         PyCharm
# anthor:      ZT@gufan

from app import create_app,db

class Role(db.Model):
    __tablename__="roles"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),nullable=True,unique=False)
    users=db.relationship("User",backref="role")

    def __repr__(self):
        return "<Role {}>".format(self.name)

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=False,nullable=True)
    email=db.Column(db.String(40),unique=True,nullable=True)
    password=db.Column(db.String(20),nullable=True)
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
    app = create_app()
    db.init_app(app)
    insert_Role()

