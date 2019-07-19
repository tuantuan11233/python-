#!/miniconda3/bin/python3
# -*- coding:utf-8 -*-

import requests, json
f = open('/Users/wangye/Desktop/admin.log', 'r')
result = list()
for line in f.readlines():
    result.append(line)
f.close()

field = "http_x_forward"

num = 1
ip_list = ['39.155.212.2']
for i in result:
    #i = i.replace('-', '0.00')
    dict_i = eval(i)
    ip = dict_i[field].split(',', 2)
    if ip[0] in ip_list:
        continue
    ip_list.append(ip[0])
    num += 1

ip_list.sort()
print('总ip数是:', num, ip_list)


'''
for i in result:
    dict_i = eval(i)
    if dict_i['status'] == '200':
        continue
    num += 1
    print(dict_i['@timestamp'].strip()[11:19], dict_i['status'], dict_i['responsetime'], dict_i['size'], dict_i['request'])
'''




'''
f = open('/Users/wangye/Desktop/2019-05-02-12.txt', 'r')

result = list()
for line in f.readlines():
    line = line.strip()[19:]
    result.append(line)
f.close()

type_1=0
type_4=0
type_6=0

for i in result:
    dict_i=eval(i)
    if dict_i['targetType'] == 1:
        type_1 += 1
    elif dict_i['targetType'] == 4:
        type_4 += 1
    elif dict_i['targetType'] == 6:
        type_6 += 1
    else:
        print(dict_i['targetType'])

print('type1的个数是:', type_1)
print('type4的个数是:', type_4)
print('type6的个数是:', type_6)

'''
'''
type_1=0
f = open('/Users/wangye/Desktop/2019-05-16-dict', 'r')

for line in f.readlines():
    dict_line = eval(line)
    time = dict_line['dateTime'][11:19]
    type = dict_line[targetType]
    print(time, type)



dic_type = {
    "targetType-1" : 0,
    "targetType-4" : 0,
    "targetType-6" : 0,
    "targetType-other" : set(),
}
tag = "start"
num = 0
dic_date = {}
with open("C:\\Users\Administrator\Desktop\\aaa.txt",'r') as A:
    for line in A:
        if line:
            data = eval(line[19:])
            if data["targetType"] == 1:
                dic_type["targetType-1"] += 1
            elif data["targetType"] == 4:
                dic_type["targetType-4"] += 1
            elif data["targetType"] == 6:
                dic_type["targetType-6"] += 1
            else:
                 dic_type["targetType-other"].add(data["targetType"])
            date = line[14:16]
            if tag != date:
                dic_date[line[0:16]] = 1
                tag = date
            else:
                dic_date[line[0:16]] += 1
print(dic_date)
print(dic_type)
'''
