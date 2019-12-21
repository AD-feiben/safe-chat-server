import json
import os

from handlers.http import base_handler
from tornado import gen
from dao import user_dao_async as user_dao
from utils.code_util import verify_code
from utils.indicator_util import gen_user_id
from utils.my_exception import MyException, ErrorEnum
from utils.tools import gen_sha256


class RegisterHandler(base_handler.BaseHandler):

    @gen.coroutine
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        require_field = ['nick_name', 'pwd_hash', 'code_token', 'code']
        for key in require_field:
            val = data.get(key)
            if val is None or val == '':
                raise MyException(ErrorEnum.ARG_NULL, msg='`{}` is null'.format(key))

        ret = verify_code(code_token=data.get('code_token'), code=data.get('code'))
        email = ret.get('indicator')

        user = yield user_dao.get(email)
        if user is not None:
            raise MyException(ErrorEnum.USER_ALREADY_EXISTS)

        data['id'] = yield gen_user_id()
        data['email'] = email

        salt = os.urandom(12).hex()
        data['salt'] = salt
        data['pwd_hash'] = gen_sha256(data['pwd_hash'] + salt)

        ret = yield user_dao.add(data)
        return self.write(ret)

