import json
import os

from handlers.http import base_handler
from tornado import gen
from dao import user_dao_async as user_dao
from utils import access_token_util
from utils.field_check import field_check
from utils.code_util import verify_code
from utils.indicator_util import gen_user_id
from utils.my_exception import MyException, ErrorEnum
from utils.tools import gen_sha256


class RegisterHandler(base_handler.BaseHandler):

    @gen.coroutine
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        require_field = ['nick_name', 'pwd_hash', 'code_token', 'code']
        field_check(data, require_field)

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


class LoginHandler(base_handler.BaseHandler):
    @gen.coroutine
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        # 登录方式 0-密码登录 1-验证码登录
        login_type = data.get('type') or 0

        if login_type == 0:
            (user, token) = yield self._login_pwd()
        elif login_type == 1:
            (user, token) = yield self._login_code()

        return self.write({'user': user, 'access_token': token})

    @gen.coroutine
    def _login_pwd(self):
        data = json.loads(self.request.body.decode('utf-8'))

        require_field = ['email', 'pwd_hash']
        field_check(data, require_field)

        email = data.get('email')
        pwd_hash = data.get('pwd_hash')

        user = yield user_dao.get(email)
        if user is None:
            raise MyException(ErrorEnum.USER_NOT_FOUND)
        salt = user.get('salt')
        temp = gen_sha256(pwd_hash + salt)
        if temp != user.get('pwd_hash'):
            raise MyException(ErrorEnum.INVALID_USERNAME_PASSWORD)

        user, token = yield self._gen_token(user)
        return user, token

    @gen.coroutine
    def _login_code(self):
        data = json.loads(self.request.body.decode('utf-8'))
        require_field = ['code_token', 'code']
        field_check(data, require_field)

        ret = verify_code(code_token=data.get('code_token'), code=data.get('code'))
        email = ret.get('indicator')
        user = yield user_dao.get(email)
        if user is None:
            raise MyException(ErrorEnum.USER_NOT_FOUND)
        user, token = yield self._gen_token(user)
        return user, token

    @gen.coroutine
    def _gen_token(self, user):
        user_id = user.get('id')
        token = yield access_token_util.gen_access_token(user_id, self.request.remote_ip)
        return user_dao.out_filter(user), token
