#!/miniconda3/bin/python3
# -*- coding:utf-8 -*-
import requests, json, sys

status_code = 0

try:
    port = ("8083", "48083")
    for i in port:
        url = 'http://10.10.176.2:' + i + '/connectors'
        r1 = requests.get(url=url, timeout=10)
        table_list = r1.text.split(',')
        #print(table_list)
    
        for table_name in table_list:
            table_name = table_name.strip("[").strip("]").strip("\"")
            r2_url = 'http://10.10.176.2:' + i + '/connectors/' + table_name + '/status'
            r2 = requests.get(r2_url)

            status_con = json.loads(r2.text)['connector']['state']
            status_tasks = json.loads(r2.text)['tasks'][0]['state']

            if status_con == 'RUNNING':
                if status_tasks == 'RUNNING':
                    status_code = 1
                else:
                    status_code = 0
                    print(status_code)
                    sys.exit(1)
            else:
                status_code = 0
                print(status_code)
                sys.exit(1)
    print(status_code)
    
except requests.exceptions.RequestException as e:
    print(0)
