import json
import random

from utils import tools, rdpool
from utils.my_exception import MyException, ErrorEnum


def gen_code(what, indicator, timeout):
    code_token = tools.gen_id3()
    code = random.randint(100000, 999999)
    rdpool.rds.set(_key(code_token, code), json.dumps({'what': what, 'indicator': indicator}), timeout)
    return code, {'code_token': code_token, 'timeout': timeout}


def verify_code(code_token, code):
    key = _key(code_token, code)
    data = rdpool.rds.get(key)

    if data is None:
        raise MyException(ErrorEnum.INVALID_VALIDATION_CODE)

    rdpool.rds.delete(key)
    record = json.loads(data)
    return record


def _key(code_token, code):
    return 'safe-chat/code/{}/{}'.format(code_token, code)
