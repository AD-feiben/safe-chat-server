#!/usr/bin/env python
# coding=utf-8

import logging
import tornado.options
import tornado.httpserver
import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient
from tornado.options import options, define
from app.application import Application
from utils import dbpool
import config


# 定义全局变量，命令参数
define('host', default=config.Host, help="run on the given host", type=str)
define('port', default=config.Port, help="run on the given port", type=int)
define("env", default='dev', help="chose env dev or prod", type=str)

AsyncHTTPClient.configure(None, max_clients=1000)


def main():
    tornado.options.parse_command_line()

    application = Application()
    http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    http_server.listen(options.port, options.host)

    print("=" * 100)
    print("* Server: Success!")
    print("* Host:   http://" + options.host + ":%s" % options.port)
    print("* Quit the server with Control-C")
    print("=" * 100)

    logging.info("=" * 100)
    logging.info("* Server: Success!")
    logging.info("* Host:   http://" + options.host + ":%s" % options.port)
    logging.info("* Quit the server with Control-C")
    logging.info("=" * 100)

    dbpool.init_app()

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print('\n* Server stopped!')
        logging.info('Server stopped!')
