#!/usr/bin/env python
# coding=utf-8

import logging
import tornado.options
from tornado.httpclient import AsyncHTTPClient
from tornado.options import define
import config


# 定义全局变量，命令参数
define('host', default=config.Host, help="run on the given host", type=str)
define('port', default=config.Port, help="run on the given port", type=int)
define("env", default='dev', help="chose env dev or prod", type=str)

AsyncHTTPClient.configure(None, max_clients=1000)


def main():
    tornado.options.parse_command_line()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print('\n* Server stopped!')
        logging.info('Server stopped!')
