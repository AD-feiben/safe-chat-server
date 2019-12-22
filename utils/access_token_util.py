import json

import config
from utils import tools, rdpool


async def gen_access_token(user_id, remote_ip):
    if user_id is None or remote_ip is None:
        return None

    token = tools.gen_id1()

    record = {'token': token, 'remote_ip': remote_ip}
    key = _key(user_id, token)
    rdpool.rds.set(key, json.dumps(record), config.AccessTokenTimeout)

    return token


async def verify_access_token(user_id, token, remote_ip):
    key = _key(user_id, token)

    data = rdpool.rds.get(key)
    if data is None:
        return False
    record = json.loads(data)

    if record['token'] == token and record['remote_ip'] == remote_ip:
        rdpool.rds.expire(key, config.AccessTokenTimeout)
        return True
    else:
        return False


async def remove_access_token(user_id, token):
    rdpool.rds.delete(_key(user_id, token))
    return True


def _key(user_id, token):
    if config.LoginMode == 'single':
        return 'safe-chat/user/login/{}'.format(user_id)
    else:
        return 'safe-chat/user/login/{}/{}'.format(user_id, token)
