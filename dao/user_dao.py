# coding=utf-8
import uuid

from utils.dbpool import create_cursor
from utils.my_exception import MyException, ErrorEnum
from utils import indicator_util


def add(data):
    """
    添加用户
    :param data:
    :return:
    """
    with create_cursor() as (conn, cursor):
        try:
            cursor.execute(
                'INSERT INTO `safe_chat`.`user` '
                ' (`id`,`nick_name`, `pwd_hash`, `salt`, `email`) '
                ' VALUES (%s, %s, %s, %s, %s) ',
                (data.get('id'),
                 data.get('nick_name'),
                 data.get('pwd_hash'),
                 data.get('salt'),
                 data.get('email')))
            conn.commit()
            return get_safely(data.get('id'))
        except Exception as e:
            raise MyException(ErrorEnum.SERVER_ERROR, e)


def get_safely(indicator):
    user = get(indicator)
    return out_filter(user)


def out_filter(user):
    """
    过滤用户敏感信息
    :param user: 用户对象
    :return: 过滤后的用户对象
    """
    if user is None:
        return user
    user['create_time'] = user['create_time'].strftime('%Y-%m-%d %H:%M:%S')
    user.pop('pwd_hash')
    user.pop('salt')
    user.pop('status')
    return user


def get(indicator):
    """
    获取用户信息
    :param indicator: 用户标识
    :return: 用户信息
    """
    try:
        uuid.UUID(indicator)
        key = 'id'
    except ValueError:
        if indicator_util.is_user_id(indicator):
            key = 'id'
        elif indicator_util.is_emil(indicator):
            key = 'email'
        else:
            raise MyException(ErrorEnum.ARG_ILLEGAL_VALUE)

    with create_cursor() as (conn, cursor):
        try:
            cond = "{}=%s".format(key, indicator.lower())
            sql = 'SELECT * FROM `safe_chat`.`user` WHERE {}'.format(cond)
            cursor.execute(sql, indicator)
            user = cursor.fetchone()
            return user
        except Exception as e:
            raise MyException(ErrorEnum.SERVER_ERROR, e=e)


def update(user_id, data):
    """
    修改用户资料
    :param user_id: 用户 id
    :param data:  用户资料
    :return: 用户信息
    """
    with create_cursor() as (conn, cursor):
        try:
            cursor.execute(
                ' SELECT '
                ' `nick_name`, `sex`, `phone`, `avatar`, `what_up`, `birth_date`'
                ' FROM `safe_chat`.`user` '
                ' WHERE `id`=%s', user_id)

            user = cursor.fetchone()
            user.update(data)

            cursor.execute(
                'UPDATE `safe_chat`.`user` SET '
                ' `nick_name`=%s, `sex`=%s, `phone`=%s, `avatar`=%s, `what_up`=%s, `birth_date`=%s'
                ' WHERE `id`=%s',
                (user.get('nick_name'), user.get('sex'), user.get('phone'),
                 user.get('avatar'), user.get('what_up'), user.get('birth_date'), user_id))
            conn.commit()

            return get_safely(user_id)
        except Exception as e:
            raise MyException(ErrorEnum.SERVER_ERROR, e=e)


def set_real_name(user_id, real_name):
    with create_cursor() as (conn, cursor):
        try:
            cursor.execute(
                'UPDATE `safe_chat`.`user` '
                'SET `real_name`=%s WHERE `id`=%s',
                (real_name, user_id))
            conn.commit()
            return get_safely(user_id)
        except Exception as e:
            raise MyException(ErrorEnum.SERVER_ERROR, e=e)


def set_pwd(data):
    """
    修改密码
    :param data: 包含 用户 id：user_id; 新密码：pwd_hash; 盐值: salt
    :return: user对象
    """
    with create_cursor() as (conn, cursor):
        try:
            conn.begin()
            user_id = data.get('user_id')
            pwd_hash = data.get('pwd_hash')
            salt = data.get('salt')

            cursor.execute(
                'UPDATE `safe_chat`.`user` SET `pwd_hash`=%s, `salt`=%s '
                ' WHERE `id`=%s', (pwd_hash, salt, user_id))
            conn.commit()
            return get_safely(user_id)
        except Exception as e:
            raise MyException(ErrorEnum.SERVER_ERROR, e=e)
