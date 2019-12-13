# coding=utf-8
import config
from app.routes import Routes
import tornado.web


class Application(tornado.web.Application):
    def __init__(self):
        handlers = Routes
        settings = config.AppSettings
        tornado.web.Application.__init__(self, handlers, **settings)
