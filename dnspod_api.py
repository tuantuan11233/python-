#!/miniconda3/bin/python3
# -*- coding:utf-8 -*-

import requests, json, datetime
from requests.adapters import HTTPAdapter
import tornado.ioloop
import tornado.web


domain = ''
login_token = ''
ulb_ip = ''
dns_pod_api_url = ''

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_argument("message"))

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

#查看xxwolo.com域名的状态
def DomainInfo():
    url = 'https://dnsapi.cn/Domain.Info'
    data = {
        "login_token": login_token,
        "format": "json",
        "domain": domain
    }
    req = requests.post(url=url, data=data)
    return req.text

#创建xxwolo.com域名的的A记录，默认线路的解析到ulb_ip上，传入二级域名
def DomainCreate(sub_domain):
    url = 'https://dnsapi.cn/Record.Create'
    record_type = 'A'
    record_line = '默认'
    data = {
        "login_token": login_token,
        "format": "json",
        "domain": domain,
        "sub_domain": sub_domain,
        "record_type": record_type,
        "record_line": record_line,
        "value": ulb_ip
    }
    req = requests.post(url=url, data=data)
    return req.text

#查看xxwolo.com二级域名的的A记录，传入二级域名
def DomainSelect(sub_domain):
    url = 'https://dnsapi.cn/Record.List'
    record_type = 'A'
    record_line = '默认'
    data = {
        "login_token": login_token,
        "format": "json",
        "domain": domain,
        "sub_domain": sub_domain,
        "record_type": record_type,
        "record_line": record_line
    }
    req = requests.post(url=url, data=data)
    return req.text

#修改xxwolo.com域名的的A记录，传入要修改的二级域名及ip
def DomainModify(sub_domain, modify_ip):
    record_id = json.loads(DomainSelect(sub_domain))['records'][0]['id']
    url = 'https://dnsapi.cn/Record.Modify'
    record_type = 'A'
    record_line = '默认'
    data = {
        "login_token": login_token,
        "format": "json",
        "domain": domain,
        "record_id": record_id,
        "sub_domain": sub_domain,
        "record_type": record_type,
        "record_line": record_line,
        "value": modify_ip
    }
    req = requests.post(url=url, data=data)
    return req.text

#删除xxwolo.com域名的的A记录，传入要修改的二级域名及ip
def DomainRemove(sub_domain):
    record_id = json.loads(DomainSelect(sub_domain))['records'][0]['id']
    url = 'https://dnsapi.cn/Record.Remove'
    data = {
        "login_token": login_token,
        "format": "json",
        "domain": domain,
        "record_id": record_id
    }
    req = requests.post(url=url, data=data)
    return req.text

#定义DnsPod类用于tornado框架路由实例化后访问,get传参请求
class DnsPod(tornado.web.RequestHandler):
    def get(self):
        try:
            #偶发性api接口不稳定，添加链接重试机制
            retry = requests.Session()
            retry.mount('https://', HTTPAdapter(max_retries=3))
            req = retry.post(dns_pod_api_url, timeout=5)
            if req.status_code == 200:
                print(req.status_code, "success")
            start_time = datetime.datetime.now()
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            action = self.get_argument('action')
            if action == 'select':
                sub_domain = self.get_argument('sub_domain')
                result = DomainSelect(sub_domain)
            elif action == 'create':
                sub_domain = self.get_argument('sub_domain')
                result = DomainCreate(sub_domain)
            elif action == 'remove':
                sub_domain = self.get_argument('sub_domain')
                result = DomainRemove(sub_domain)
            elif action == 'info':
                result = DomainInfo()
            elif action == 'modify':
                sub_domain = self.get_argument('sub_domain')
                modify_ip = self.get_argument('modify_ip')
                result = DomainModify(sub_domain, modify_ip)
            end_time = datetime.datetime.now()
            print(now_time, " 执行时间: ", end_time - start_time)
            print(action, result)
            self.write(result)
        except requests.exceptions.RequestException as err:
            print(err)

#定义路由入口
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/story/([0-9]+)", StoryHandler),
        (r"/dnspod", DnsPod),
    ])

#定义端口
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()