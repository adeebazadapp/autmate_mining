import json
import os

import requests


def selfcall_groups():
    url = "https://apis.pocket52.com/api/v1/lobby/groups"
    method = "get"

    headers = {
 "gk-device-id": "5eba84bafd15d4eb", 
 "gk-app-type": "CASH_APP", 
 "Accept-Encoding": "gzip", 
 "gk-android-id": "5eba84bafd15d4eb", 
 "gk-app-bundle-name": "219", 
 "gk-advertising-id": "f6d5dfc9-3bc5-49a1-ae2e-4b5976c6c018", 
 "gk-is-rooted": "false", 
 "gk-platform": "android", 
 "gk-app-version-name": "12.6.3", 
 "gk-wifi-mac": "", 
 "gk-app-version": "219", 
 "x-request-id": "1729602486177", 
 "Cookie": "gk-device-id=d288b9ba-b3a1-4ff6-aa52-6d225ee8904a; session-id=716bc01b-8412-4dd7-83a8-b39c389ddd15; gk-session-id=e0c4fa86-4c1e-4c5f-96b1-649ec178c65f", 
 "gk-device-name": "OnePlus ONEPLUS A6003", 
 "gk-app-signature": "8e58c7b24ed11b7c9f9f91db1b91cc225f829fe1a8e18382a202fa01ed39e26c", 
 "x-vendor-id": "1", 
 "gk-app-instance-id": "aeee1c781efab4bb309f485e15de4504", 
 "gk-app-codepush-label-name": "", 
 "gk-imei-id": "", 
 "gk-android-version": "11", 
 "User-Agent": "okhttp/4.10.0"
}
    params = {}

    data = None

    return requests.get(url=url, headers=headers, params=params, data=data, verify=False)


def selfcall_tables(group):
    url = "https://apis.pocket52.com/api/v1/lobby/group/{}/tables".format(str(group))
    method = "get"

    headers = {
 "gk-device-id": "5eba84bafd15d4eb", 
 "gk-app-type": "CASH_APP", 
 "Accept-Encoding": "gzip", 
 "gk-android-id": "5eba84bafd15d4eb", 
 "gk-app-bundle-name": "219", 
 "gk-advertising-id": "f6d5dfc9-3bc5-49a1-ae2e-4b5976c6c018", 
 "gk-is-rooted": "false", 
 "gk-platform": "android", 
 "gk-app-version-name": "12.6.3", 
 "gk-wifi-mac": "", 
 "gk-app-version": "219", 
 "x-request-id": "1729602486177", 
 "Cookie": "gk-device-id=d288b9ba-b3a1-4ff6-aa52-6d225ee8904a; session-id=716bc01b-8412-4dd7-83a8-b39c389ddd15; gk-session-id=e0c4fa86-4c1e-4c5f-96b1-649ec178c65f", 
 "gk-device-name": "OnePlus ONEPLUS A6003", 
 "gk-app-signature": "8e58c7b24ed11b7c9f9f91db1b91cc225f829fe1a8e18382a202fa01ed39e26c", 
 "x-vendor-id": "1", 
 "gk-app-instance-id": "aeee1c781efab4bb309f485e15de4504", 
 "gk-app-codepush-label-name": "", 
 "gk-imei-id": "", 
 "gk-android-version": "11", 
 "User-Agent": "okhttp/4.10.0"
}
    params = {}

    data = None

    return requests.get(url=url, headers=headers, params=params, data=data, verify=False)


def selfcall_lobby(rooms):
    url = "https://apis.pocket52.com/api/v1/leaderboard/hybrid/lobby"
    method = "get"

    headers = {
 "gk-device-id": "5eba84bafd15d4eb", 
 "gk-app-type": "CASH_APP", 
 "Accept-Encoding": "gzip", 
 "gk-android-id": "5eba84bafd15d4eb", 
 "gk-app-bundle-name": "219", 
 "gk-advertising-id": "f6d5dfc9-3bc5-49a1-ae2e-4b5976c6c018", 
 "gk-is-rooted": "false", 
 "gk-platform": "android", 
 "gk-app-version-name": "12.6.3", 
 "gk-wifi-mac": "", 
 "gk-app-version": "219", 
 "x-request-id": "1729602486177", 
 "Cookie": "gk-device-id=d288b9ba-b3a1-4ff6-aa52-6d225ee8904a; session-id=716bc01b-8412-4dd7-83a8-b39c389ddd15; gk-session-id=e0c4fa86-4c1e-4c5f-96b1-649ec178c65f", 
 "gk-device-name": "OnePlus ONEPLUS A6003", 
 "gk-app-signature": "8e58c7b24ed11b7c9f9f91db1b91cc225f829fe1a8e18382a202fa01ed39e26c", 
 "x-vendor-id": "1", 
 "gk-app-instance-id": "aeee1c781efab4bb309f485e15de4504", 
 "gk-app-codepush-label-name": "", 
 "gk-imei-id": "", 
 "gk-android-version": "11", 
 "User-Agent": "okhttp/4.10.0"
}
    params = {"roomIds": str(rooms)}

    data = None

    return requests.get(url=url, headers=headers, params=params, data=data, verify=False)


list_of_groups = []
list_of_tables = []
list_of_users = []

json_res = selfcall_groups().json().get('data')
# json_res = json.loads(resp.get('data'))
groups = json_res.get('groups')

for i in groups:
    if i.get('isPractice') == False:
        list_of_groups.append(i.get('id'))

for group in list_of_groups:
    json_res = selfcall_tables(group).json().get('data')
    # json_res = json.loads(resp.get('data'))
    tables = json_res.get('tables')

    for i in tables:
        if i.get('roomId') not in list_of_tables:
            list_of_tables.append(i.get('roomId'))

    rooms = ','.join(map(str, list_of_tables))
    list_of_tables = []

    json_res = selfcall_lobby(rooms).json().get('data')
    # json_res = json.loads(resp.get('data'))
    # lobby = json_res.get('data')
    if json_res and json_res[0].get("scoreboard"):
        for i in json_res[0].get('scoreboard'):
            # for j in i.get('scoreboard'):
            list_of_users.append(i.get('userId'))

filtered_users = [user for user in list_of_users if user.startswith('105') and len(user) == 8]

print (len(set(filtered_users)))


def pocket52(unique_in_list):
    url = 'http://54.70.36.111/backend/put_data/'
    data = json.dumps({"camp_name": "pocket52", "data": unique_in_list})
    requests.put(url=url, data=data, verify=False)


unique_in_list = list(set(filtered_users))
pocket52(unique_in_list)
