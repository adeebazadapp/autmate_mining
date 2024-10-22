import json
import random
import time
import uuid

import requests
import os
def self_call_compdata(gameVariants,lbStakes):
    url = "https://apis.pocket52.com/api/v1/leaderboard/campaigns/1724916257947/child"
    method = "get"

    headers = {
 "gk-android-id": "5eba84bafd15d4eb", 
 "gk-app-bundle-name": "219", 
 "gk-platform": "android", 
 "User-Agent": "okhttp/4.10.0", 
 "x-request-id": "1729602484710", 
 "gk-advertising-id": "f6d5dfc9-3bc5-49a1-ae2e-4b5976c6c018", 
 "gk-is-rooted": "false", 
 "gk-app-instance-id": "aeee1c781efab4bb309f485e15de4504", 
 "gk-android-version": "11", 
 "Cookie": "gk-device-id=d288b9ba-b3a1-4ff6-aa52-6d225ee8904a; session-id=716bc01b-8412-4dd7-83a8-b39c389ddd15; gk-session-id=e0c4fa86-4c1e-4c5f-96b1-649ec178c65f", 
 "x-vendor-id": "1", 
 "gk-app-signature": "8e58c7b24ed11b7c9f9f91db1b91cc225f829fe1a8e18382a202fa01ed39e26c", 
 "authorization": "Bearer undefined", 
 "gk-device-id": "5eba84bafd15d4eb", 
 "vendor": "pocket52", 
 "Accept-Encoding": "gzip", 
 "gk-app-version-name": "12.6.3", 
 "gk-imei-id": "", 
 "gk-app-codepush-label-name": "", 
 "gk-wifi-mac": "", 
 "gk-app-type": "CASH_APP", 
 "gk-app-version": "219", 
 "gk-device-name": "OnePlus ONEPLUS A6003"
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
 "gk-android-id": "5eba84bafd15d4eb", 
 "gk-app-bundle-name": "219", 
 "gk-platform": "android", 
 "User-Agent": "okhttp/4.10.0", 
 "x-request-id": "1729602484710", 
 "gk-advertising-id": "f6d5dfc9-3bc5-49a1-ae2e-4b5976c6c018", 
 "gk-is-rooted": "false", 
 "gk-app-instance-id": "aeee1c781efab4bb309f485e15de4504", 
 "gk-android-version": "11", 
 "Cookie": "gk-device-id=d288b9ba-b3a1-4ff6-aa52-6d225ee8904a; session-id=716bc01b-8412-4dd7-83a8-b39c389ddd15; gk-session-id=e0c4fa86-4c1e-4c5f-96b1-649ec178c65f", 
 "x-vendor-id": "1", 
 "gk-app-signature": "8e58c7b24ed11b7c9f9f91db1b91cc225f829fe1a8e18382a202fa01ed39e26c", 
 "authorization": "Bearer undefined", 
 "gk-device-id": "5eba84bafd15d4eb", 
 "vendor": "pocket52", 
 "Accept-Encoding": "gzip", 
 "gk-app-version-name": "12.6.3", 
 "gk-imei-id": "", 
 "gk-app-codepush-label-name": "", 
 "gk-wifi-mac": "", 
 "gk-app-type": "CASH_APP", 
 "gk-app-version": "219", 
 "gk-device-name": "OnePlus ONEPLUS A6003"
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




