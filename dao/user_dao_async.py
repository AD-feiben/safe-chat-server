# coding=utf-8

from . import user_dao


async def add(data):
    return user_dao.add(data)


async def get(indicator):
    return user_dao.get(indicator)


async def get_safely(indicator):
    return user_dao.get_safely(indicator)


async def update(user_id, data):
    return user_dao.update(user_id, data)


def out_filter(*args, **kwargs):
    return user_dao.out_filter(*args, **kwargs)
