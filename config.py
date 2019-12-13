# coding=utf-8
import os


ID = 1
Host = '0.0.0.0'
Port = 16800

Version = 'v1'

Instance_Id = Port * 100 + ID

# 应用启动配置
AppSettings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'views'),
    'static_path': os.path.join(os.path.dirname(__file__), 'statics'),
    'cookie_secret': 'safe_jasdi*22^da&&(002',
    'login_url': "/v1/user/login/pwd",
    'autoreload': True,
    'debug': True
}

Mysql = {
    'dev': {
        'host': 'localhost',
        'port': 3306,
        'user': 'chat',
        'pwd': 'root',
        'charset': 'utf8'
    },
    'prod': {
        'host': 'localhost',
        'port': 3306,
        'user': 'chat',
        'pwd': '',
        'charset': 'utf8'
    }
}
