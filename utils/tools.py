import base64
import hashlib
import uuid


def gen_sha256(msg):
    sha256 = hashlib.sha256()
    sha256.update(msg.encode(encoding='utf-8'))
    return sha256.hexdigest()


def gen_id1():
    """
        uuid以hex输出
        """
    return uuid.uuid4().hex


def gen_id3():
    """
    对uuid进行base64编码，且去掉等号、替换'+'和'/'
    """
    guid = str(base64.b64encode(uuid.uuid4().bytes), encoding="utf8")
    return guid.replace('==', '').replace('+', 'AD').replace('/', 'DS')
