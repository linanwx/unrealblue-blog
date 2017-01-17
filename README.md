# 基于flask的个人博客系统搭建

## 待办事项
- [ ] 绘制目录下各个模块对应的功能图表，使读者很快对项目进行了解
- [ ] 将博客系统改为个人博客系统
- [ ] 测试其他部分是否完全正常工作
- [ ] 添加一键清除本地数据库和一键部署本地数据库的功能
- [ ] 将python库升级到最新版本
- [x] 调试python 3.5邮件系统，解决UTF-8编码问题
- [x] 添加环境变量自动导入功能
- [x] 添加gitignore忽略数据库文件和pycache文件
- [x] 更新到python 3.5版本
- [x] 基本测试happytree的程序

## 部署过程：

首先需要在本机上部署，之后使用nginx反向代理工具，可以将端口号暴露出去，这样其他人就可以在公网访问你的博客了，具体过程如下。

1. 安装virtualenv python虚拟环境，` pip install virtualenv ` 或者 `pip3 install virtualenv` 。然后使用virtualenv在一个合适的目录建立venv环境` virtualenv venv `，
2. 激活virtualenv环境，运行venv目录下的activate，`. venv/bin/activate`。
3. 安装所有requirements.txt中的模块, `pip install -r requirements.txt`。如果安装太慢，你可能需要配置pip的国内源。更改pip源的方法参见pip官方页面。
4. 导入坏境变量，编辑隐藏文件.env中的内容，进行如下修改

  * `export MAIL_USERNAME=email@example.com` (服务器发验证码用的邮箱，开启了smtp服务的邮箱账号，程序里默认使用qq邮箱，修改config文件可成其它类型邮箱)
  * `export MAIL_PASSWORD=password` (上面邮箱的密码，注意qq邮箱使用特殊16位密码)
  * `export FLASK_ADMIN=admin@example.com` (服务器运行后，使用该邮箱创建账号就是管理者)

5. 安装数据库迁移。输入以下命令

  * `python manager.py db init` (使用init命令创建迁移仓库，此时会多出migrations文件夹)
  * `python manager.py db migrate -m "initial migration"`(migrate命令用来自动创建迁移脚本)
  * `python manager.py db upgrade`(更新数据库，第一次使用该命令会新建一个数据库data-dev.sqlite)
  
6. 部署程序， `python manager.py deploy`
7. 在本地运行程序, `python manager.py runserver`打开http://127.0.0.1:5000 端口查看，按Ctrl+C退出程序。