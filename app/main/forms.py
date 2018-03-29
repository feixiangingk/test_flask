#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2018/3/29  16:13
# IDE:         PyCharm
# anthor:      ZT@gufan

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email
#flask-pagedown flask-pagedown扩展使用的语法
from flask.ext.pagedown.fields import PageDownField

class PostForm(FlaskForm):
    title=StringField(label=u"标题",validators=[DataRequired()])
    body=PageDownField(label=u"正文",validators=[DataRequired()])
    submit=SubmitField(label=u"发表")

class CommentForm(FlaskForm):
    body=PageDownField(label=u"评论",validators=[DataRequired()])
    submit=SubmitField(label=u"发表")