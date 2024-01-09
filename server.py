from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from apptest import app
from tornado.ioloop import IOLoop

s = HTTPServer(WSGIContainer(app))
s.listen(8088) # 监听 8080 端口
IOLoop.current().start()