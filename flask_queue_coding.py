#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:wy


from flask import Flask
from flask import request
import json
import requests
import time
import datetime
import os

app = Flask(__name__)

starttime = datetime.datetime.now()

# 重启队列接口
@app.route('/restart', methods=['GET'])
def send():
    if request.method == 'GET':
        print("开始处理重启队列", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        os.system('ssh root@10.19.132.85 "service supervisor restart"')
        print("队列重启成功", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        result = "队列消费端重启成功" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return result


@app.route('/test', methods=["GET", "POST"])
def aaa():
    url = request.url
    endtime = datetime.datetime.now()
    print(request.args)
    print(endtime - starttime)
    return url

# coding消息推送接口
@app.route('/v1/coding/post', methods=['POST'])
def codingpost():
    headers = {"Content-Type": "text/plain"}
    coding_url = ''
    if request.method == 'POST':
        print("开始处理 接收coding 通知: ")
        post_data = request.get_data()
        post_data = post_data.decode('utf-8')
        post_data = json.loads(post_data)
        if post_data['msgtype'] == 'text':
            print("接收请求数据: ", post_data)
        elif post_data['msgtype'] == 'markdown':
            post_data['markdown']['content'] = post_data['markdown'].pop('text')
            print("接收请求数据: ", post_data)
        req = requests.post(coding_url, json=post_data, headers=headers)
        print(req.json())
    return "success"

if __name__ == '__main__':
    app.run(host='10.10.84.75', port=8099)
