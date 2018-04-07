#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/3/25 21:49
# software:     PyCharm
from flask import flash  # 显示登录成功 提示信息
from flask import render_template, current_app, request,url_for
from flask import redirect
from .import main
from ..models import Post,Comment
from forms import PostForm,CommentForm
from flask_login import current_user,login_required #必须为登录状态的装饰器
from ..import db

# def init_views(app):
#     #显式调用current_app  设置count属性，初始值=0


@main.route("/index_demo",endpoint="index_demo") #由于使用蓝图模式，这里的endpoint还是会自动变成mian.index_demo
def index_demo():
    print "index_demo endpoint:",request.endpoint
    if request.args.get("message"):
        flash(request.args.get("message"))
    return render_template("index_demo.html",title=u"欢迎来到谷帆的blog")

@main.app_template_test("current_link")
def is_current_link(link):
    return link == request.path


@main.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap_a.html")

@main.route("/")
def index():
    print "index_demo /:", request.endpoint
    user_agent=request.headers.get("User-Agent")
    print current_app.name #显示test_SQLAlchemy因为程序实例化在该模块
    current_app.count+=1
    print current_app.count
    # print app.url_map #url_map查看URL和视图函数之间的映射
    # return '<p>your browser is {} </p>'.format(user_agent)
    return redirect(url_for("main.index_demo"))

@main.route("/count",methods=["GET","POST"])
def count():
    if not hasattr(current_app,"count"):
        current_app.count=0
    current_app.count+=1 #测试成功，可以作为全局app容器管理全局变量
    return "current_app.count is {}".format(current_app.count)



#专门处理错误页的路由，需要指定错误码 使用该装饰器errorhandler
# @main.errorhandler(404) #这是普通app的使用方法
@main.app_errorhandler(404)#蓝图自定义错误使用方法
def page_not_found(error):
    return render_template("404.html",title=u"404页面不存在"),404

@main.route("/posts/<int:id>",methods=['GET','POST'])
def post(id):
    """
    post detail详情页
    :param id:
    :return:
    """
    post=Post.query.get_or_404(id) #根据model的id查出文章的对象

    #评论窗体
    form=CommentForm()

    #保存评论 #post方法路由到这里
    if form.validate_on_submit():
        #post请求，说明有一条新增 或是修改此时根据
        comment=Comment(body=form.body.data,post_id=post.id)
        db.session.add(comment)
        db.session.commit()
    #评论列表
    return  render_template("posts/detail.html",title=post.title,form=form,post=post)

# @main.route("/edit",methods=['GET','POST'])
@main.route("/edit/<int:id>",methods=['GET','POST'])
@login_required
def edit(id=0):
    '''
    新增和编辑在一起
    :param id:
    :return:
    '''
    form=PostForm()
    if id==0:
        #新增
        post=Post(author=current_user)
    else:
        #修改
        post=Post.query.get_or_404(id)

    if form.validate_on_submit():
        post.body=form.body.data
        post.title=form.title.data
        db.session.add(post)
        db.session.commit()
        return  redirect(url_for("main.post",id=post.id))
    return render_template("posts/edit.html",form=form,post=post,title=post.title)

@main.route("/create",methods=['GET','POST'])
def create_post():
    # post = Post(author=current_user)
    form = PostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data,body=form.body.data,author_id=current_user)
        # post.body = form.body.data
        # post.title = form.title.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("main.post", id=post.id))
    else:
        return render_template("posts/edit.html",form=form)
