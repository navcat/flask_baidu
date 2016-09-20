#!/usr/bin/python
#coding=utf-8

__author__ = "NavCat"

from flask import Flask, request, make_response
from flask import abort

app = Flask(__name__)

@app.route("/")
def index():
    # abort(404)
    # return "<h1>Hello World</h1>"
    response = make_response("<h1>Hello World</h1>")
    response.set_cookie("status", 'ok')
    return response


@app.route("/user/<name>/")
def user(name):
    """ 打印用户的名字 """
    return "<h1>你好, %s</h1>" % name


@app.route("/info/")
def info():
    """ 获取请求信息 """
    user_agent = request.headers.get('User-Agent')
    return "<h1>您的浏览器是：%s</h1>" % user_agent


if __name__ == '__main__':
    app.run(debug=True)
