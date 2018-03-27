
#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/3/25 8:31
# software:     PyCharm

from flask_wtf import  FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class LoginForm(FlaskForm):
    username=StringField(label=u'用户名',validators=[DataRequired(message=u"用户名不能为空")])
    pwd=PasswordField(label=u'密码',validators=[DataRequired(message=u"密码不能为空")])
    submit=SubmitField(label=u"提交")

class RegisterForm(FlaskForm):
    username=StringField(label=u'用户名',validators=[DataRequired(message=u"用户名不能为空")])
    email=StringField(label=u"邮箱",validators=[DataRequired(message=u"邮箱不能为空"),Length(1,40),Email()])
    pwd=PasswordField(label=u'密码',validators=[DataRequired(message=u"密码不能为空"),EqualTo("pwd_t",message=u"两次密码必须一致")])
    pwd_t=PasswordField(label=u"密码确认",validators=[DataRequired(message=u'密码确认不能为空')])
    submit=SubmitField(label=u"立即注册")


