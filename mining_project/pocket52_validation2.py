import json
import os

import requests


def selfcall_groups():
    url = "https://apis.pocket52.com/api/v1/lobby/groups"
    method = "get"

    headers = {
        "gk-android-id": "94d6b722aace3c12",
        "gk-app-bundle-name": "215",
        "gk-platform": "android",
        "User-Agent": "okhttp/4.10.0",
        "x-request-id": "1727431352398",
        "gk-advertising-id": "a2e355a7-fde0-4110-80e0-ab7a1cfd9552",
        "gk-is-rooted": "true",
        "gk-app-instance-id": "9c7face6cb79e7134d99db7dba0c39fd",
        "gk-android-version": "9",
        "Cookie": "gk-device-id=fec1a1b7-e433-4981-9e1e-e7187e8ee4aa; session-id=705080bf-e37b-4493-89b2-39b1a1226c42; gk-session-id=e0c4fa86-4c1e-4c5f-96b1-649ec178c65f",
        "x-vendor-id": "1",
        "gk-app-signature": "8e58c7b24ed11b7c9f9f91db1b91cc225f829fe1a8e18382a202fa01ed39e26c",
        "authorization": "Bearer e0c4fa86-4c1e-4c5f-96b1-649ec178c65f",
        "gk-device-id": "94d6b722aace3c12",
        "vendor": "pocket52",
        "Accept-Encoding": "gzip",
        "gk-app-version-name": "12.5.1",
        "gk-imei-id": "",
        "gk-app-codepush-label-name": "",
        "gk-wifi-mac": "94",
        "gk-app-type": "CASH_APP",
        "gk-app-version": "215",
        "gk-device-name": "OnePlus ONEPLUS A5010",
        "If-None-Match": "W/\"43c1-KgncLPSpDrumefj9iORlhpIExqk\""
    }
    params = {}

    data = None

    return requests.get(url=url, headers=headers, params=params, data=data, verify=False)


def selfcall_tables(group):
    url = "https://apis.pocket52.com/api/v1/lobby/group/{}/tables".format(str(group))
    method = "get"

    headers = {
        "gk-android-id": "94d6b722aace3c12",
        "gk-app-bundle-name": "215",
        "gk-platform": "android",
        "User-Agent": "okhttp/4.10.0",
        "x-request-id": "1727431274545",
        "gk-advertising-id": "a2e355a7-fde0-4110-80e0-ab7a1cfd9552",
        "gk-is-rooted": "true",
        "gk-app-instance-id": "9c7face6cb79e7134d99db7dba0c39fd",
        "gk-android-version": "9",
        "Cookie": "gk-device-id=fec1a1b7-e433-4981-9e1e-e7187e8ee4aa; session-id=705080bf-e37b-4493-89b2-39b1a1226c42; gk-session-id=e0c4fa86-4c1e-4c5f-96b1-649ec178c65f",
        "x-vendor-id": "1",
        "gk-app-signature": "8e58c7b24ed11b7c9f9f91db1b91cc225f829fe1a8e18382a202fa01ed39e26c",
        "authorization": "Bearer e0c4fa86-4c1e-4c5f-96b1-649ec178c65f",
        "gk-device-id": "94d6b722aace3c12",
        "vendor": "pocket52",
        "Accept-Encoding": "gzip",
        "gk-app-version-name": "12.5.1",
        "gk-imei-id": "",
        "gk-app-codepush-label-name": "",
        "gk-wifi-mac": "94",
        "gk-app-type": "CASH_APP",
        "gk-app-version": "215",
        "gk-device-name": "OnePlus ONEPLUS A5010"
    }
    params = {}

    data = None

    return requests.get(url=url, headers=headers, params=params, data=data, verify=False)


def selfcall_lobby(rooms):
    url = "https://apis.pocket52.com/api/v1/leaderboard/hybrid/lobby"
    method = "get"

    headers = {
        "gk-android-id": "94d6b722aace3c12",
        "gk-app-bundle-name": "215",
        "gk-platform": "android",
        "User-Agent": "okhttp/4.10.0",
        "x-request-id": "1727430860912",
        "gk-advertising-id": "a2e355a7-fde0-4110-80e0-ab7a1cfd9552",
        "gk-is-rooted": "true",
        "gk-app-instance-id": "9c7face6cb79e7134d99db7dba0c39fd",
        "gk-android-version": "9",
        "Cookie": "gk-device-id=fec1a1b7-e433-4981-9e1e-e7187e8ee4aa; session-id=705080bf-e37b-4493-89b2-39b1a1226c42; gk-session-id=e0c4fa86-4c1e-4c5f-96b1-649ec178c65f",
        "x-vendor-id": "1",
        "gk-app-signature": "8e58c7b24ed11b7c9f9f91db1b91cc225f829fe1a8e18382a202fa01ed39e26c",
        "authorization": "Bearer e0c4fa86-4c1e-4c5f-96b1-649ec178c65f",
        "gk-device-id": "94d6b722aace3c12",
        "vendor": "pocket52",
        "Accept-Encoding": "gzip",
        "gk-app-version-name": "12.5.1",
        "gk-imei-id": "",
        "gk-app-codepush-label-name": "",
        "gk-wifi-mac": "94",
        "gk-app-type": "CASH_APP",
        "gk-app-version": "215",
        "gk-device-name": "OnePlus ONEPLUS A5010"
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
