
import json
import time
import requests
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from mysql import connector as mysql
def self_call_de_shiprocket (awb) :
    url = "https://shiprocket.co/pocx/tracking/{}".format(awb)
    method = "get"
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Cookie": "_ga=GA1.2.916392292.1726224002; _gid=GA1.2.114555421.1726741723; _gat_gtag_UA_52128413_3=1; _ga_DFSWBZV7QM=GS1.1.1726741722.2.0.1726741727.0.0.0",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua-mobile": "?0",
        "Referer": "https://shiprocket.co/tracking/{}".format(awb),
        "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
        "Sec-Fetch-Dest": "empty"
    }

    params = {}


    data =None


    resp = requests.get(url=url, headers=headers, params=params, data=data, verify=False)
    return resp

def self_call_darmacompany(incrementId):
    url = "https://customer.thedermaco.com/v1/customer/guest/is-repeated-user"
    method = "post"

    headers = {
    "x-version-code": "36",
    "x-source": "mobile-app",
    "x-appsflyer-id": "{}-5783006761541268090".format(int(time.time()*1000)),
    "x-app-version-full-name": "2.4.19",
    "x-codepush-version": "19",
    "User-Agent": "okhttp/4.9.1",
    "devicetype": "Handset",
    "deviceid": "0be6502bfb8aae23",
    "useragent": "honasa-tdc-android-2.4.19(36)",
    "x-platform": "android",
    "systemver": "11",
    "Content-Type": "application/json;charset=UTF-8",
    "x-app-version-name": "2.4",
    "Accept-Encoding": "gzip"
    }
    params = {'source': 'mobile-app', 'version': '2.4.19(36)', 'platform': 'android'}


    data = {"incrementId":str(incrementId)}


    resp = requests.post(url=url,headers=headers,params=params,data=json.dumps(data),verify=False)
    return  resp


def derma(unique_in_list):
    url = 'http://54.70.36.111/backend/put_data/'
    data = json.dumps({"camp_name": "derma", "data": unique_in_list})
    requests.put(url=url,data=data,verify=False)

def get_last_orderid():
    conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend",passwd="123admin!", database="techteam")
    cursor = conn.cursor()
    cursor.execute('''SELECT DISTINCT AWB FROM derma_user_data''')
    data = cursor.fetchall()
    user_id = list(data[-1])[0]
    cursor.close()
    return int(user_id)



incrementId = 81008222089
awb = get_last_orderid()



ids_list = []
for i in range(200):
    try:
        awb =awb+1
        DE = self_call_de_shiprocket(awb)
        if DE.status_code == 200:
            valid_data = DE.json()
            if valid_data.get('tracking_json').get('company').get('name') == 'Derma Co':
                if valid_data.get('tracking_json').get('tracking_data').get('shipment_status_text') == 'DELIVERED':
                    de_order_details = dict(DE.json().get('tracking_json').get('order'))
                    waybill = {'AWB':awb}

                    de_order_details.update(waybill)
                    final_order = {"order_id": de_order_details.get('order_id'),
                                   "order_total": de_order_details.get('order_total'),
                                   "order_date": de_order_details.get('order_date'),
                                   "system_order_id": de_order_details.get('system_order_id'), "AWB": awb}
                    ids_list.append(final_order)



                if DE.json().get('tracking_json').get('order').get('payment_method') == 'Prepaid':
                    de_order_details = dict(DE.json().get('tracking_json').get('order'))
                    final_order = {"order_id": de_order_details.get('order_id'), "order_total": de_order_details.get('order_total'),
                                   "order_date": de_order_details.get('order_date'), "system_order_id": de_order_details.get('system_order_id'), "AWB": awb}

                    ids_list.append(final_order)


    except:
        pass



derma(unique_in_list=ids_list)



