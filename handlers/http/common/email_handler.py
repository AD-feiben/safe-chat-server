import json
import logging
import time

from handlers.http import base_handler
from tornado import gen

from utils.code_util import gen_code
from utils.email_util import send_mail_async
from utils.my_exception import MyException, ErrorEnum

code_temp_obj = open('views/code.html')
code_temp = ''

try:
    code_temp = code_temp_obj.read()
except Exception as e:
    logging.error(e)
finally:
    code_temp_obj.close()


class SendEmailHandler(base_handler.BaseHandler):
    @gen.coroutine
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))

        email = data.get('email')
        if email is None or email == '':
            raise MyException(ErrorEnum.ARG_NULL, msg='`email` is null')

        code, ret = gen_code('email', email, 600)

        yield send_mail_async(
            email,
            '邮件验证码',
            code_temp.format(
                email=email,
                code=code,
                href='http://122.51.101.169/',
                date=time.strftime('%Y-%m-%d %H:%M:%S'),
                year=time.strftime('%Y')
            ),
            'html'
        )

        return self.write(ret)
