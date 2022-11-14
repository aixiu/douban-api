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
import api.dbconfig

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
    url = f'https://movie.douban.com/subject/{vod_douban_id}/'
    
    flie_path = f'./douban'
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
        }
        page_text = requests.post(url=url, headers=headers, timeout=20)
        page_text_data = requests.post(url=url, headers=headers, timeout=20)
        page_text_data.raise_for_status()
        page_text_data.encoding = page_text_data.apparent_encoding
        page_text = page_text_data.text
        
        vod_name = api.dbconfig.vod_name(page_text=page_text)
        vod_year = api.dbconfig.vod_year(page_text=page_text)
        vod_lang = api.dbconfig.vod_lang(page_text=page_text)
        vod_sub = api.dbconfig.vod_sub(page_text=page_text)
        vod_pic = api.dbconfig.vod_pic(page_text=page_text)
        vod_class = api.dbconfig.vod_class(page_text=page_text)
        vod_actor = api.dbconfig.vod_actor(page_text=page_text)
        vod_writer = api.dbconfig.vod_writer(page_text=page_text)
        vod_score = api.dbconfig.vod_score(page_text=page_text)                
        vod_content = api.dbconfig.vod_content(page_text=page_text)
        vod_area = api.dbconfig.vod_area(page_text=page_text)
        vod_director = api.dbconfig.vod_director(page_text=page_text)
        vod_pubdate = api.dbconfig.vod_pubdate(page_text=page_text)
        vod_duration = api.dbconfig.vod_duration(page_text=page_text)
        vod_remarks = api.dbconfig.vod_remarks(page_text=page_text)        
        vod_total =  vod_remarks
        vod_score_num =  random.randint(100, 1000)
        vod_score_all =  random.randint(200, 500)
        vod_douban_score =  vod_score        
        vod_reurl = url   # 豆瓣地址
        
        vod_data = {
            "vod_name": vod_name,
            "vod_sub": vod_sub,
            "vod_pic": vod_pic,
            "vod_year": vod_year,
            "vod_lang": vod_lang,
            "vod_class": vod_class,
            "vod_actor": vod_actor,
            "vod_content": vod_content,
            "vod_writer": vod_writer,
            "vod_area": vod_area,
            "vod_remarks": vod_remarks,
            "vod_director": vod_director,
            "vod_pubdate": vod_pubdate,
            "vod_total": vod_total,
            "vod_score": vod_score,
            "vod_douban_score": vod_douban_score,
            "vod_score_num": vod_score_num,
            "vod_score_all": vod_score_all,
            "vod_duration": vod_duration,
            "vod_reurl": vod_reurl,
            "vod_douban_id": vod_douban_id,        
        }        
        
        return jsonify(vod_data)
        
    except Exception :
        error_data = {
            'code': 404,
            'msg': 'ID不合法',
            'info': '一切有为法，如梦幻泡影，如露亦如电，当作如是观。',
            'date': datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
        }
        return jsonify(error_data)

@app.route('/test')
def test():
    return 'Test'

if __name__ == '__main__':
    app.run()
