import json
import random
import time
import uuid

import requests
import os
import  urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
os.environ['http_proxy'] = "http://localhost:8888"
os.environ['https_proxy'] = "http://localhost:8888"



def self_call_compdata(gameVariants,lbStakes):
    url = "https://apis.pocket52.com/api/v1/leaderboard/campaigns/1724916257947/child"
    method = "get"

    headers = {
    "gk-device-id": "5eba84bafd15d4eb",
    "gk-app-type": "CASH_APP",
    "Accept-Encoding": "gzip",
    "gk-android-id": "5eba84bafd15d4eb",
    "gk-app-bundle-name": "215",
    "gk-advertising-id": str(uuid.uuid4()),
    "gk-is-rooted": "true",
    "gk-platform": "android",
    "gk-app-version-name": "12.5.1",
    "gk-wifi-mac": "",
    "gk-app-version": "215",
    "x-request-id": "1727268721280",
    "Cookie": "gk-device-id=d69ee878-9dd7-495e-ade2-28eaf51b13c4; session-id=898f1cb6-1ec4-4df1-9a2a-360669c0f402; gk-session-id=e0c4fa86-4c1e-4c5f-96b1-649ec178c65f",
    "gk-device-name": "OnePlus ONEPLUS A6003",
    "gk-app-signature": "8e58c7b24ed11b7c9f9f91db1b91cc225f829fe1a8e18382a202fa01ed39e26c",
    "x-vendor-id": "1",
    "gk-app-instance-id": "ab1a95d7ca32fb9357387ee128bc3e46",
    "gk-app-codepush-label-name": "",
    "gk-imei-id": "",
    "gk-android-version": "11",
    "User-Agent": "okhttp/4.10.0"
    }

    params = {'lbStakes':lbStakes, 'gameVariants': gameVariants}


    data = None


    return  requests.get(url=url,headers=headers,params=params,data=data,verify=False)




lbStakes = ['5', '10', '15', '20']
gameVariants = ['PLO','NLHE']

# Restructure the game dictionary for clarity
game = {stake: variant for stake in lbStakes for variant in gameVariants}
completed = []
for variant in gameVariants:
    for stake in lbStakes:
        camp_data = self_call_compdata(gameVariants=variant, lbStakes=stake)  # Properly pass lbStakes argument
        if camp_data.status_code == 200:
            camp_data_2 = camp_data.json().get('data', {})
            completed_leaderboards = camp_data_2.get('leaderboards', {}).get('Completed', [])

            # Collect required information if available
            for leaderboard in completed_leaderboards:
                completed.append({
                    'childLeaderboardId': leaderboard.get('childLeaderboardId'),
                    'leaderboardGroupId': leaderboard.get('leaderboardGroupId'),
                    'campaignTag': leaderboard.get('campaignTag')
                })


def self_call_play(childLeaderboardId, leaderboardGroupId, campaignTag):
    url = "https://apis.pocket52.com/api/v1/leaderboard/group/{}/child/{}/details".format(leaderboardGroupId,childLeaderboardId)
    method = "get"

    headers = {
    "gk-device-id": "5eba84bafd15d4eb",
    "gk-app-type": "CASH_APP",
    "Accept-Encoding": "gzip",
    "gk-android-id": "5eba84bafd15d4eb",
    "gk-app-bundle-name": "215",
    "gk-advertising-id": str(uuid.uuid4()),
    "gk-is-rooted": "true",
    "gk-platform": "android",
    "gk-app-version-name": "12.5.1",
    "gk-wifi-mac": "",
    "gk-app-version": "215",
    "x-request-id": str(int(time.time())),
    "Cookie": "gk-device-id=d69ee878-9dd7-495e-ade2-28eaf51b13c4; session-id=898f1cb6-1ec4-4df1-9a2a-360669c0f402; gk-session-id=e0c4fa86-4c1e-4c5f-96b1-649ec178c65f",
    "gk-device-name": "OnePlus ONEPLUS A6003",
    "gk-app-signature": "8e58c7b24ed11b7c9f9f91db1b91cc225f829fe1a8e18382a202fa01ed39e26c",
    "x-vendor-id": "1",
    "gk-app-instance-id": "ab1a95d7ca32fb9357387ee128bc3e46",
    "gk-app-codepush-label-name": "",
    "gk-imei-id": "",
    "gk-android-version": "11",
    "User-Agent": "okhttp/4.10.0"
    }
    params = {'numOfRecords': '100', 'campaignTag': str(campaignTag), 'offset': '0'}


    data = None
    return  requests.get(url=url,headers=headers,params=params,data=data,verify=False)
def pocket52(unique_in_list):
    url = 'http://54.70.36.111/backend/put_data/'
    data = json.dumps({"camp_name": "pocket52", "data": unique_in_list})
    requests.put(url=url,data=data,verify=False)

play_user_data=[]

for i in completed:
    childLeaderboardId = i.get('childLeaderboardId')
    leaderboardGroupId = i.get('leaderboardGroupId')
    campaignTag = i.get('campaignTag')
    user_data = self_call_play(childLeaderboardId, leaderboardGroupId, campaignTag).json().get('data')
    try:
        play_user_data.extend(user_data.get('scoreboard'))
    except:
        print (i, user_data.get("scoreboard"))

# print(play_user_data)

unique_in_list1 = []
for i in play_user_data:
    if str(i.get('userId')).startswith("105") and len(i.get('userId')) >= 8:
        unique_in_list1.append(i.get('userId'))


unique_in_list = list(set(unique_in_list1))
pocket52(unique_in_list)




