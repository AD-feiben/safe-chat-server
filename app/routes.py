# coding=utf-8
import config
from handlers.http import register_handler, index_handler

base = '%s/api' % config.Version
user_base = '%s/user' % base

Routes = [
    (r"/", index_handler.IndexHandler),
    (r"/%s/register" % user_base, register_handler.RegisterHandler)
]
