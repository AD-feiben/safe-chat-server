# coding=utf-8

import logging
from enum import Enum, unique


class MyException(Exception):

    def __init__(self, err_enum, msg=None, e=None):
        if isinstance(err_enum, ErrorEnum):
            code = err_enum.value[0]
            msg = msg or err_enum.value[1]
        else:
            code = err_enum
        self.code = code
        self.msg = msg
        if e is not None:
            logging.exception(e)


@unique
class ErrorEnum(Enum):
    # 正常
    SERVER_OK = (10000, 'OK')
    # 服务器内部错误
    SERVER_ERROR = (10001, 'internal server error')
    # 无效Token
    INVALID_TOKEN = (10002, 'invalid token')
    # 缺少必要http header参数
    ARG_HTTP_HEADER_MISSING = (10003, "required http header parameter missing")
    # 必填参数为空
    ARG_NULL = (10004, "required arguments is null")
    # 参数值不合法
    ARG_ILLEGAL_VALUE = (10005, "illegal argument")
    # Session超时
    SESSION_TIMEOUT = (10006, "session timeout")
    # 无效签名
    INVALID_SIGNATURE = (10007, "invalid signature")
    # 加解密失败
    ENCRYPTION_DECRYPTION_FAILED = (10008, "encryption or decryption failed")
    # 无效的用户或密码
    INVALID_USERNAME_PASSWORD = (10009, "invalid username or password")
    # 用户不存在
    USER_NOT_FOUND = (10010, "user not found")
    # 用户已存在
    USER_ALREADY_EXISTS = (10011, "user already exists")
    # 无效的密码
    INVALID_PASSWORD = (10012, "invalid password")
    # 签权失败
    AUTHENTICATION_FAILED = (10013, "authentication failed")
    # 没有权限
    PERMISSION_DENIED = (10014, "permission denied")
    # 无效的验证码

    INVALID_VALIDATION_CODE = (10015, "invalid validation code")
    # 不支持该操作
    UNSUPPORTED_OPERATION = (10016, "unsupported operation")
    # 不允许修改操作
    NOT_ALLOW_UPDATE = (10017, "not allow update")
    # 不允许删除操作
    NOT_ALLOW_DELETE = (10018, "not allow delete")
    # 邮件发送错误
    MAIL_SEND_ERROR = (10031, "mail send error")
    # 短信发送错误
    SMS_SEND_ERROR = (10032, "sms send error")
    # 读文件错误
    FILE_READ_ERROR = (10040, "read file error")
    # 文件没有找到
    FILE_NOT_FOUND = (10041, "file not found")
    # 11000 微信平台返回的错误
    # 微信已被绑定
    WECHAT_IS_BOUND = (11001, "The WeChat has been bound")