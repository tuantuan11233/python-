#!/miniconda3/bin/python3
# -*- coding:utf-8 -*-
from pymongo import MongoClient
import psycopg2


#脚本同步mongo数据至pgsql，查询后插入
conn = psycopg2.connect(database="", user="", password="", host="", port="")
print('postgresql connect successful!')

client = MongoClient('mongodb://')

databases_name = ''
table_name = ''

databases = client[databases_name]
collection = databases[table_name]
print('mongodb connect successful!')

cur = conn.cursor()
'''
for i in collection.find():

    sk = ""
    sv = ""
    tl = []

    for key, value in i.items():
        if type(value) == list:
            tl.append(str(value))
        else:
            tl.append(value)
        sk += (key + ",")
        sv += "%s,"
    else:
        insert = 'INSERT INTO responder_post(%s)VALUES(%s)' % (sk[0:-1], sv[0:-1])
        tv = tuple(tl)
        print(insert, tv)
        #cur.execute(insert, tv)


#增加一个字段
#cur.execute('ALTER TABLE post ADD wangye varchar;')

# 关闭连接
conn.commit()
cur.close()
conn.close()


'''




# 获取结果
cur.execute('SELECT * FROM Livelog')
results = cur.fetchall()
print(results)

'''
#cur.execute("CREATE TABLE post(_id varchar, gid varchar, tid varchar, title varchar, text varchar, serverTime varchar, authorId varchar, rpid varchar, rseq varchar, farpid varchar, rtext varchar, rtime varchar, raid varchar, seq varchar, loveCount varchar, deleted varchar, votelog varchar, votenum varchar);")
#cur.execute("CREATE TABLE responder_post(_id varchar,gid varchar,tid varchar,serverTime varchar,authorId varchar,tUserId varchar,tText varchar,seq varchar,deleted varchar,audioTime varchar,audioUrl varchar,evaluate varchar,money varchar,isFree varchar,star varchar,svs varchar,eval_reason varchar,strEval varchar);")


#for i in mycol.find():
    #sql = 'INSERT INTO post('+str(list(i.keys())).strip("[").strip("]").replace('\'', '')+') VALUES ('+(str(list(i.values()))).strip("[").strip("]")+')'
    #cur.execute(sql)
    #print(sql)
    #if i.keys()["_id"] == 'wxpt0858a61d2263f91314aefd94':
    #print(i.items())

#cur.execute("CREATE TABLE student(id integer,name varchar,sex varchar);")

# 插入数据
#cur.execute("")

cur.execute("INSERT INTO post(_id,gid,tid,title,text,serverTime,authorId,rpid,farpid,rseq,rtext,rtime,raid,seq,loveCount,deleted)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",('wxpt010796c017808600775d8aa0', 'feeling', 'wxth3f350e6c561306377cc3da14', '呃呃呃呃呃呃呃呃', '很棒', 1542687158544, 'stff3b51d3d0269e8dd1c8be8fa0', '', '', 0, '', 1542628033900, '', 13, 0, 1))
'''



