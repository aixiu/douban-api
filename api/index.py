# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/11/14 12:42:57

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world !!'

@app.route('/test')
def test():
    return 'Test'

if __name__ == '__main__':
    app.run()
