# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/11/14 00:34:37

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world !!'

if __name__ == '__main__':
    app.run()