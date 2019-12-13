import json
from handlers.http import base_handler
from tornado import gen


class RegisterHandler(base_handler.BaseHandler):

    @gen.coroutine
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        self.write(data)

