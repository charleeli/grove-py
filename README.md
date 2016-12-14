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