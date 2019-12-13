# coding=utf-8

from handlers.http import base_handler


class IndexHandler(base_handler.BaseHandler):
    def get(self):
        return self.write('Hello safe chat')
