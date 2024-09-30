import json
import random

import  requests
import os
import  urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from mysql import connector as mysql
def lenskart(orderId):
    url = "https://api-gateway.juno.lenskart.com/v4/orders/aggregator/inventory"
    method = "get"

    headers = {
     "accept-language": "en",
     "Accept-Encoding": "gzip",
     "x-country-code": "IN",
     "udid": "fbcbbc82ded538f7",
     "x-country-code-override": "IN",
     "brand": "xiaomi",
     "X-B3-TraceId": "1726953126965",
     "x-session-token": "95104b7c-99dd-4f01-bd4f-e71a75504f44",
     "appversion": "4.4.7 (240905001)",
     "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; M2101K6P Build/RQ3A.211001.001)",
     "x-app-version": "4.4.7 (240905001)",
     "x-api-client": "android",
     "X-Build-Version": "240905001",
     "uniqueId": "192166d7c35fbcbb",
     "x-accept-language": "en",
     "x-customer-type": "REPEAT",
     "model": "M2101K6P",
     "api_key": "valyoo123",
     "Content-Type": "application/json"
    }
    params = {'orderId': str(orderId), 'phone': '9873581569', 'sha1Phone': 'c01e0e4674babac6fe5f88ddd8c48bb54f52ab1d'}


    data = None


    resp = requests.get(url=url,headers=headers,data=data,params=params,verify=False)
    return resp



def get_last_orderid():
    conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend",passwd="123admin!", database="techteam")
    cursor = conn.cursor()
    cursor.execute('''SELECT order_id FROM lenskart_orderId''')
    data = cursor.fetchall()
    user_id = list(data[-1])[0]
    cursor.close()
    return int(user_id)



def pocket52(unique_in_list):
    url = 'http://54.70.36.111/backend/put_data/'
    data = json.dumps({"camp_name": "lenskart", "data": unique_in_list})
    requests.put(url=url,data=data,verify=False)


db_order_id = get_last_orderid() # last mined id
ids_list =[]
print(db_order_id)
last_order_id = None
try:
    for i in range(db_order_id, db_order_id+300):
        orderId = i
        if lenskart(orderId).status_code == 200:
            ids_list.append(orderId)


        last_order_id = i

except:
    pass
loop_count =0
while loop_count <2:
    if len(ids_list) == 0:
        for i in range(last_order_id,last_order_id+200):
            orderId = i
            if lenskart(orderId).status_code == 200:
                ids_list.append(orderId)

    loop_count += 1
print(ids_list)
pocket52(unique_in_list=ids_list)


