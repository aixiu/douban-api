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



@app.route('/')
def index():
    return 'Hello, world !!'

@app.route('/test')
def test():
    return 'Test'

if __name__ == '__main__':
    app.run()
