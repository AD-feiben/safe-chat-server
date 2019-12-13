# coding=utf-8
import pymysql
from tornado.options import options
from DBUtils.PooledDB import PooledDB
from contextlib import contextmanager
import config

# 数据库连接池
pool = None


def init_app():
    env = options.env
    mysql_config = config.Mysql[env]

    global pool
    if pool is None:
        config_opt = {
            'host': mysql_config['host'],
            'port': mysql_config['port'],
            'user': mysql_config['user'],
            'password': mysql_config['pwd'],
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor
        }
        pool = PooledDB(pymysql, **config_opt)


@contextmanager
def create_cursor():
    conn = pool.connection()
    cursor = conn.cursor()
    try:
        yield conn, cursor
    finally:
        cursor.close()
        conn.close()
