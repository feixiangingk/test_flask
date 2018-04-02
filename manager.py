#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2017/11/20  11:08
# IDE:         PyCharm
# anthor:      ZT@gufan
from flask import current_app
from flask_migrate import Migrate, MigrateCommand, upgrade  # 加入脚本处理db迁移插件
from flask_script import Manager
from livereload import Server
from app import create_app,db
from app.models import User,Role

app=create_app()
manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command("db",MigrateCommand)

@manager.command
def dev():
    app.config.debug=True
    live_server = Server(app.wsgi_app)
    # 监控文件变化参数是目录e.g:监控static文件夹  static/*.*
    live_server.watch("**/*.*")  # 监控整个项目
    live_server.serve(open_url=True)

@manager.command #加入命令  测试方法
def test():
    pass

@manager.command #数据库初始化
def deploy():
    upgrade() #直接将upgrade命令绑定到deploy上

if __name__=="__main__":
    #必须要此行，才能接受
    manager.run()