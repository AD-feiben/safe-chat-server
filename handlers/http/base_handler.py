# coding=utf-8

from tornado.web import RequestHandler
from utils.my_exception import MyException


class BaseHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.write_error(404, 'Not found or not implement')

    def send_error(self, status_code: int = 500, **kwargs):
        if 'exc_info' in kwargs:
            exception = kwargs['exc_info'][1]
            if isinstance(exception, MyException):
                self.write_error(exception.code, exception.msg)

    def write_error(self, code, msg=None):
        if msg is None:
            msg = 'Unknown failure'

        self.write({'error': {'code': code, 'message': msg}})
        self.finish()

