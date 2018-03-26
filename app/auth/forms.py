#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/3/25 8:31
# software:     PyCharm

from flask_wtf import  Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username=StringField(label=u'用户名',validators=[DataRequired()])
    pwd=PasswordField(label=u'密码',validators=[DataRequired()])
    submit=SubmitField(label=u"提交")
