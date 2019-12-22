# coding=utf-8
import config
from handlers.http import index_handler
from handlers.http.user import user_handler
from handlers.http.common import email_handler

base = '%s/api' % config.Version
common_base = '%s/common' % base
user_base = '%s/user' % base

Routes = [
    (r"/", index_handler.IndexHandler),
    (r"/%s/register" % user_base, user_handler.RegisterHandler),
    (r"/%s/login" % user_base, user_handler.LoginHandler),
    (r"/%s/send-email" % common_base, email_handler.SendEmailHandler)
]
