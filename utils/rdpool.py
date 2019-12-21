# coding:utf-8
import redis
from tornado.options import options

import config

rds = None


def init_app():
    global rds
    env = options.env

    if rds is None:
        rds = redis.Redis(host=config.Redis[env]['host'], port=config.Redis[env]['port'], decode_responses=True)

