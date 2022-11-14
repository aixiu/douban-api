# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/11/14 12:42:57

import json
import os
import random
from datetime import datetime

import requests
from flask import Flask, jsonify, request
import dbconfig

app = Flask(__name__)

# 解决浏览器中json数据，中文无法展示的问题
app.config['JSON_AS_ASCII']=False   # 中文正常化，解决乱码
app.config['JSON_SORT_KEYS']=False   # json不排序
app.config['JSONIFY_PRETTYPRINT_REGULAR']=True  # 输出json格式化完美显示
app.config["JSONIFY_MIMETYPE"] = "application/json;charset=utf-8"   # 指定浏览器渲染的文件类型，和解码格式；

@app.route('/')
def index():
    vod_douban_id  = request.args.get('id')
    
    if vod_douban_id is None or vod_douban_id == '':
        error_data = {
            'code': 400,
            'msg': '非法请求',
            'info': '本是清灯不归客，却因浊酒恋红尘。',
            'date': datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
        }
        return jsonify(error_data)

@app.route('/test')
def test():
    return 'Test'

if __name__ == '__main__':
    app.run()
