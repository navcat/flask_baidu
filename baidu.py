#!/usr/bin/python
#coding=utf-8

__author__ = "NavCat"

from flask import Flask, request, make_response
from flask import abort
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    """ 新闻首页 """
    return render_template('index.html')


@app.route('/cat/<name>/')
def cat(name):
    """ 新闻类别页面 """
    return render_template('cat.html', name=name)


@app.route('/detail/<int:pk>/')
def detail(pk):
    """ 新闻详情页 """
    return render_template('detail.html')


if __name__ == '__main__':
    app.run(debug=True)
