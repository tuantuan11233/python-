#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import hashlib
import httplib
import json
import urllib
import time
import urlparse
import os

public_key = ""
private_key = ""
project_id = ""  # 项目ID 请在Dashbord 上获取
base_url = "https://api.ucloud.cn"

java01_backendid = ""
java02_backendid = ""

class UCLOUDException(Exception):
    def __str__(self):
        return "Error"


def _verfy_ac(private_key, params):
    items = params.items()
    items.sort()

    params_data = ""
    for key, value in items:
        params_data = params_data + str(key) + str(value)

    params_data = params_data + private_key

    '''use sha1 to encode keys'''
    hash_new = hashlib.sha1()
    hash_new.update(params_data)
    hash_value = hash_new.hexdigest()
    return hash_value


class UConnection(object):
    def __init__(self, base_url):
        self.base_url = base_url
        o = urlparse.urlsplit(base_url)
        if o.scheme == 'https':
            self.conn = httplib.HTTPSConnection(o.netloc)
        else:
            self.conn = httplib.HTTPConnection(o.netloc)

    def __del__(self):
        self.conn.close()

    def get(self, resouse, params):
        resouse += "?" + urllib.urlencode(params)
        #print("%s%s" % (self.base_url, resouse))
        self.conn.request("GET", resouse)
        response = json.loads(self.conn.getresponse().read())
        return response

    def post(self, uri, params):
        #print("%s%s %s" % (self.base_url, uri, params))
        headers = {"Content-Type": "application/json"}
        self.conn.request("POST", uri, json.JSONEncoder().encode(params), headers)
        response = json.loads(self.conn.getresponse().read())
        return response


class UcloudApiClient(object):
    # 添加 设置 数据中心和  zone 参数
    def __init__(self, base_url, public_key, private_key):
        self.g_params = {}
        self.g_params['PublicKey'] = public_key
        self.private_key = private_key
        self.conn = UConnection(base_url)

    def get(self, uri, params):
        # print params
        _params = dict(self.g_params, **params)

        if project_id:
            _params["ProjectId"] = project_id

        _params["Signature"] = _verfy_ac(self.private_key, _params)
        return self.conn.get(uri, _params)

    def post(self, uri, params):
        _params = dict(self.g_params, **params)

        if project_id:
            _params["ProjectId"] = project_id

        _params["Signature"] = _verfy_ac(self.private_key, _params)
        return self.conn.post(uri, _params)

def get_ulb_status():
    if __name__ == '__main__':
        ApiClient = UcloudApiClient(base_url, public_key, private_key)
        Parameters = {
            "Action": "",
            "ULBId": "",
            "Region": ""
        }
        response = ApiClient.get("/", Parameters)
        ulb_status_list = response[u'DataSet'][0][u'VServerSet'][0][u'BackendSet']
        for i in ulb_status_list:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                  'Load Balancing Present State:' + str(i[u'Enabled']), 'Device IP address:' + str(i[u'PrivateIP']))

def update_java_ulb_status(java_backendid, status_new):
    if __name__ == '__main__':
        ApiClient = UcloudApiClient(base_url, public_key, private_key)
        Parameters = {
            "Action": "UpdateBackendAttribute",
            "ULBId": "",
            "Region": "cn-bj2",
            "BackendId": java_backendid,
            "Port": ,
            "Enabled": status_new
        }
        response = ApiClient.get("/", Parameters)
        return response


#1为开启，0为关闭负载均衡的该设备
update_java_ulb_status(java01_backendid, 0)
get_ulb_status()
time.sleep(30)

os.system('ssh root@java01 "ulimit -n205555 && /opt/play-runner/play start /data/xxlite"')

update_java_ulb_status(java01_backendid, 1)
get_ulb_status()

time.sleep(30)

update_java_ulb_status(java02_backendid, 0)
get_ulb_status()

time.sleep(30)
os.system('ssh root@java02 "ulimit -n205555 && /opt/play-runner/play start /data/xxlite"')

update_java_ulb_status(java02_backendid, 1)
get_ulb_status()
