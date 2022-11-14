# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/11/14 12:42:57

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello,python!'

if __name__ == '__main__':
    app.run()
