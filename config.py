# coding=utf-8
import os

App_Name = 'Safe Chat'

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
        'user': 'root',
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

Redis = {
    'dev': {
        'host': 'localhost',
        'port': '6379'
    },
    'prod': {
        'host': 'localhost',
        'port': '6379'
    }
}

Mail = {
    'host': 'smtp.qq.com',
    'user': '',
    'pass': ''
}

# 登录模式：单点登录或者多点登录，single或者multi
LoginMode = 'multi'

# Access Token过期时间，指最后一次访问后多久过期
# 一周后失效
AccessTokenTimeout = 604800
