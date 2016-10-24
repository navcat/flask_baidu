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
    # 模拟新闻数据
    news_list = [
        (1, "这里是新闻标题1", "1分钟前"),
        (2, "这里是新闻标题2", "1分钟前"),
        (3, "这里是新闻标题3", "1分钟前"),
        (4, "这里是新闻标题4", "1分钟前"),
        (5, "这里是新闻标题5", "1分钟前"),
    ]
    return render_template('index.html', news_list=news_list)


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
    # csrf key
    app.config['SECRET_KEY'] = 'hard to guess string'
