#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2017/11/20  10:53
# IDE:         PyCharm
# anthor:      ZT@gufan
import datetime
from . import create_app,db,loginManager
from flask_login import UserMixin #是用flask_login插件需要让用户继承它
from markdown import markdown #为了转换markdown为HTML的string

class Role(db.Model):
    __tablename__="roles"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),nullable=True,unique=False)
    users=db.relationship("User",backref="role")

    #数据初始化 可以Python shell中执行:
    #from app import db
    #from app.models import Role
    #Role.seed()
    @staticmethod
    def seed():
        db.session.add_all(map(lambda r:Role(name=r),["Guests","Administrators"]))
        db.session.commit()

    def __repr__(self):
        return "<Role {}>".format(self.name)

class User(UserMixin,db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=False,nullable=True)
    email=db.Column(db.String(40),unique=True,nullable=True)
    password=db.Column(db.String(20),nullable=True)
    role_id=db.Column(db.Integer,db.ForeignKey("roles.id"))
    posts=db.relationship("Post",backref="author")

    def __repr__(self):
        return "User {}".format(self.name)

    @staticmethod
    def on_created(target, value,oldvalue, initiator):
        target.role_id=Role.query.filter_by(name="Guests").first().id


#该方法是flask_login必备方法
@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#SQLAlchemy触发器功能  http://docs.sqlalchemy.org/en/latest/orm/events.html
db.event.listen(User.name,'set',User.on_created)


class Post(db.Model):
    __tablename__="posts"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    body=db.Column(db.String,nullable=False)
    body_html=db.Column(db.String,nullable=False)
    created=db.Column(db.DateTime,index=True,default=datetime.datetime.utcnow)

    author_id=db.Column(db.Integer,db.ForeignKey("users.id")) #和User建立关系

    comments=db.relationship('Comment',backref="post") #建立外键关系 反向引用
    def __repr__(self):
        return "Post {}".format(Post.title)
    @staticmethod
    def on_body_changed(target, value,oldvalue, initiator):
        if value in [None,""]:
            target.body_html=""
        else:
            target.body_html=markdown(value)
db.event.listen(Post.body,"set",Post.on_body_changed)



class Comment(db.Model):
    __tablename__="comments"
    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.String)
    created=db.Column(db.DateTime,index=True,default=datetime.datetime.utcnow)
    post_id=db.Column(db.Integer,db.ForeignKey("posts.id"))

    def __repr__(self):
        return "Comment {}".format(Comment.id)


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

