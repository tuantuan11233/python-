#!/miniconda3/bin/python3
# -*- coding:utf-8 -*-
from pymongo import MongoClient
import wget, ssl


import pymysql

conn = pymysql.connect(host='', user='', passwd='', db='')
cur = conn.cursor()

sql = "SELECT image_url FROM `UserFace` WHERE `source` != 4 and similarity<0.4"
reCount = cur.execute(sql)
print(reCount)
data_url = cur.fetchall()

for i in data_url:
    #try:
    url = i[0]
    print(url)
    ssl._create_default_https_context = ssl._create_unverified_context
    out_fname = './bad-mysql/'
    wget.download(url, out=out_fname)
    #except:
        #pass


cur.close()
conn.close()


#mongo连接
client = MongoClient('mongodb://')

databases_name = ''
table_name = ''

databases = client[databases_name]
collection = databases[table_name]
print('mongodb connect successful!')

#good文件放similarity大于0.4的
for i in collection.find({'similarity': {'$gte': 0.4}}):
    data_url = i['face_url']
    print(data_url)
    ssl._create_default_https_context = ssl._create_unverified_context
    out_fname = './good/'
    wget.download(data_url, out=out_fname)
    
#bad文件放similarity小于0.4的
for i in collection.find({'similarity': {'$lt': 0.4}}):
    data_url = i['face_url']
    print(data_url)
    ssl._create_default_https_context = ssl._create_unverified_context
    out_fname = './bad/'
    wget.download(data_url, out=out_fname)