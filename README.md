# grove-py

## 安装依赖
```
1.安装pyvenv
    sudo apt-get install python3-dev python3-venv python3-pip
2.启动虚拟环境
    cd ~/grove-py
    pyvenv env
    source ./env/bin/activate
3.在虚拟环境下安装第三方依赖
    cd ~/grove-py
    pip install --upgrade pip
    pip3 install -r requirement.txt
```

## 创建工程
```
1.新建工程
    cd ~/grove-py
    django-admin startproject mysite
2.启动服务器
    cd ~/grove-py/mysite
    python manage.py migrate
    python manage.py runserver
3.登陆
    http://127.0.0.1:8000/
```

## 创建应用
```
1.创建app
    cd ~/grove-py/mysite
    python manage.py startapp myapp
2.注册app
    编辑mysite/settings.py
3.创建模型
    编辑myapp/models.py
4.检查模型
    python manage.py check
5.激活模型
    python manage.py makemigrations myapp
6.运行迁移文件
    python manage.py sqlmigrate myapp 0001
7.创建表
    python manage.py migrate
```

## 创建管理端
```
1.创建一个管理员用户
    python manage.py createsuperuser
    mysiteadmin
    mysiteadmin@example.com
    charleeli
2.启动开发服务器
    python manage.py runserver
3.登陆管理端
    http://127.0.0.1:8000/admin/
```

## 升级数据库
```
1.启动虚拟环境
    cd grove-py
    pyvenv env
    source ./env/bin/activate

2.检查模型
    cd ./mysite
    python manage.py check

3.激活模型
    python manage.py makemigrations myapp

4.运行迁移文件
    python manage.py sqlmigrate myapp 0001

5.创建表
    python manage.py migrate
```
