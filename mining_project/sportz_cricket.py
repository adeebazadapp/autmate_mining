import json

import requests, os,time,random,datetime

os.environ['http_proxy'] = "http://localhost:8888"
os.environ['https_proxy'] = "http://localhost:8888"

def sportsbaazi(list2):
    url = 'http://team2.appanalytics.in/backend/put_data/'
    data = json.dumps({"camp_name": "sportsbaazi", "data": list2})
    requests.put(url=url, data=data, verify=False)





def step1():
    url = "https://bbapi.ballebaazi.com/cricket/v2/homepage"
    method = "get"

    headers = {
    "Accept-Encoding": "gzip",
    "apptype": "react-native",
    "accesstoken": "48d0a87ad6fca8d37a40c521262c182eb1fdbe45",
    "package": "com.ballebaazi",
    "User-Agent": "okhttp/4.10.0",
    "platform": "android",
    "version": "3.3.65",
    "Cookie": "AWSALBTG=LgqEG3CZRZ0JMD0QgLeAxRATwFwDRtfhZimj0fGHPL65OEgn/kZ0z6XXtnVXH0DoM5icqRxzZRT9ShOx6OXWqozEVJPE1JZ0+VxAbscdzriV7eHDjhy/h54fxrmy0Q23chu79PBEHmdXLNbX8KkKUS/iiIA+5X8x7RZC6JoRoai7aqszEek=; AWSALBTGCORS=LgqEG3CZRZ0JMD0QgLeAxRATwFwDRtfhZimj0fGHPL65OEgn/kZ0z6XXtnVXH0DoM5icqRxzZRT9ShOx6OXWqozEVJPE1JZ0+VxAbscdzriV7eHDjhy/h54fxrmy0Q23chu79PBEHmdXLNbX8KkKUS/iiIA+5X8x7RZC6JoRoai7aqszEek=",
    "versionname": "3.3.65",
    "versioncode": "21403365",
    "If-None-Match": "W/\"627e-dBMXCVW6gvxla1+LwysNRcmswFA\"",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMDY5MDM5NiwicGhvbmUiOiI4OTUzNTcxMjM0IiwiaWF0IjoxNzI5NTkwMDU5LCJleHAiOjE3NjA2OTQwNTl9.CbKuzR_fBrwDHapuU6xId6CQ0jBwR9eLhzmj8D4YHI8",
    "loginid": "10690396"
    }
    params = {}


    data = None
    resp = requests.get(url=url,headers=headers,params=params,data=data,verify=False)
    if resp.status_code==200:
        cricket = resp.json().get('response').get('livematches').get('cricket')

    return  cricket
cricket = step1()


def step2(cricket):
    method = "get"

    headers = {
    "Accept-Encoding": "gzip",
    "apptype": "react-native",
    "accesstoken": "48d0a87ad6fca8d37a40c521262c182eb1fdbe45",
    "package": "com.ballebaazi",
    "User-Agent": "okhttp/4.10.0",
    "platform": "android",
    "version": "3.3.65",
    "Cookie": "AWSALBTG=l69xsdo8JmwZljUFhjMVkVZ5rNjPPugqaGQbNxG3kb82ZWMw675RsePJiRIep5MIXSuF8AemFxAHC/HNamnllb6GfvQlReqIiQDqA8tQwvT06oaLlTeN46S14EXmbRu5YqC4RhxrRWrJaWkFVicSRtpsDFlCAtHDuKiAuVo2aW7623ujijA=; AWSALBTGCORS=l69xsdo8JmwZljUFhjMVkVZ5rNjPPugqaGQbNxG3kb82ZWMw675RsePJiRIep5MIXSuF8AemFxAHC/HNamnllb6GfvQlReqIiQDqA8tQwvT06oaLlTeN46S14EXmbRu5YqC4RhxrRWrJaWkFVicSRtpsDFlCAtHDuKiAuVo2aW7623ujijA=",
    "versionname": "3.3.65",
    "versioncode": "21403365",
    "If-None-Match": "W/\"9900-3CSYUDu5AQmhTntqmfdwVSFwXZQ\"",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMDY5MDM5NiwicGhvbmUiOiI4OTUzNTcxMjM0IiwiaWF0IjoxNzI5NTkwMDU5LCJleHAiOjE3NjA2OTQwNTl9.CbKuzR_fBrwDHapuU6xId6CQ0jBwR9eLhzmj8D4YHI8",
    "loginid": "10690396"
    }
    params = {'sport_score_type': '1'}


    data = None
    leagues  = []
    for i in cricket:
        url = "https://bbapi.ballebaazi.com/cricket/v2/leagues/{}/1".format(i.get('match_key'))
        resp = requests.get(url=url, headers=headers, params=params, data=data, verify=False)

        if resp.status_code == 200:
            for i in resp.json().get('response').get('leaguesBycategory'):
                if len(i.get('leaguelist')) >=1:
                   for j in  i.get('leaguelist'):
                       leagues.append(j.get('league_id'))
    return  leagues


league_id = step2(cricket)



def step3(league_id):

    method = "get"

    headers = {
    "Accept-Encoding": "gzip",
    "apptype": "react-native",
    "accesstoken": "48d0a87ad6fca8d37a40c521262c182eb1fdbe45",
    "package": "com.ballebaazi",
    "User-Agent": "okhttp/4.10.0",
    "platform": "android",
    "version": "3.3.65",
    "Cookie": "AWSALBTG=tC2QMrEvkxUlOkxTa63ydOOGT4TwATmrcLZeXdsq2+6QnM196splKlvsn6zWXZyveMtQRBcKLTnTzzFnA59CZ30eNxmbMiwwSgyTlhIX9sP8pxyIDPD0gcH3eW2ByQULA7XCp8UOyl2qSiNR1NKPBSzcv3yf48GJZ1abysuvsvHJ52uqB28=; AWSALBTGCORS=tC2QMrEvkxUlOkxTa63ydOOGT4TwATmrcLZeXdsq2+6QnM196splKlvsn6zWXZyveMtQRBcKLTnTzzFnA59CZ30eNxmbMiwwSgyTlhIX9sP8pxyIDPD0gcH3eW2ByQULA7XCp8UOyl2qSiNR1NKPBSzcv3yf48GJZ1abysuvsvHJ52uqB28=",
    "versionname": "3.3.65",
    "versioncode": "21403365",
    "If-None-Match": "W/\"2355a-ss4djTm8XCNZu4pb1+uW0z6cawk\"",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMDY5MDM5NiwicGhvbmUiOiI4OTUzNTcxMjM0IiwiaWF0IjoxNzI5NTkwMDU5LCJleHAiOjE3NjA2OTQwNTl9.CbKuzR_fBrwDHapuU6xId6CQ0jBwR9eLhzmj8D4YHI8",
    "loginid": "10690396"
    }
    params = {}

    opponentJoiners = []
    data = None
    for i in league_id:
        url = "https://bbapi.ballebaazi.com/cricket/league/winners/{}".format(i)
        resp = requests.get(url=url, headers=headers, params=params, data=data, verify=False)
        if resp.status_code==200:
            for i in resp.json().get('response').get('opponentJoiners'):
                opponentJoiners.append(i)

    return opponentJoiners

user_list = step3(league_id)
print(user_list)
def check_registered_date(registered_date_str):
    # Step 1: Parse the date
    registered_date = datetime.datetime.strptime(registered_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")

    # Step 2: Extract the year, month, and day
    year = registered_date.year
    month = registered_date.month
    day = registered_date.day

    # Step 3: Compare the values (customize the comparison logic)
    # Let's assume we want to check if the date is in June 2024 (month = 6, year = 2024)
    if year == 2024 and month >= 8 :
        # Step 4: Indent (perform any action, like printing an indented message)
       return True
    else:
        return False

def step4(user_list):

    method = "get"

    headers = {
    "Accept-Encoding": "gzip",
    "apptype": "react-native",
    "accesstoken": "48d0a87ad6fca8d37a40c521262c182eb1fdbe45",
    "package": "com.ballebaazi",
    "User-Agent": "okhttp/4.10.0",
    "platform": "android",
    "version": "3.3.65",
    "Cookie": "AWSALBTG=23wk66cj1NVPdxku7nG0it2y6BOSFM/IHSPl3x5ExTxywxxytCLpWnux5qXpAMvIoDjHQedDIKJKc90eFpV4NeYsCS/VlCme+ByHx36Qw8HXMGBE7c5UIJX1dYsfdeVK+es7gn7SFg+N1yvBmz6NQZ87fiwXGBb717UPDdKWzwHq3TbtQBg=; AWSALBTGCORS=23wk66cj1NVPdxku7nG0it2y6BOSFM/IHSPl3x5ExTxywxxytCLpWnux5qXpAMvIoDjHQedDIKJKc90eFpV4NeYsCS/VlCme+ByHx36Qw8HXMGBE7c5UIJX1dYsfdeVK+es7gn7SFg+N1yvBmz6NQZ87fiwXGBb717UPDdKWzwHq3TbtQBg=",
    "versionname": "3.3.65",
    "versioncode": "21403365",
    "If-None-Match": "W/\"cb5-HOSgFMnfWYgw3Pdkgnvh4r+IgFI\"",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMDY5MDM5NiwicGhvbmUiOiI4OTUzNTcxMjM0IiwiaWF0IjoxNzI5NTkwMDU5LCJleHAiOjE3NjA2OTQwNTl9.CbKuzR_fBrwDHapuU6xId6CQ0jBwR9eLhzmj8D4YHI8",
    "loginid": "10690396"
    }

    data = None
    valid_user_list = []

    for i in user_list:
        params = {'user': str(i.get('user'))}
        url = "https://bbapi.ballebaazi.com/users/profile/{}".format(i.get('user_id'))
        kyc = requests.get(url=url,headers=headers,params=params,data=data,verify=False)
        if kyc.status_code == 200:
            valid_user= kyc.json().get('response').get('user')

            registered_date_str = str(valid_user.get('registered_date'))
            if check_registered_date(registered_date_str):
                valid_user_list.append(valid_user)
    return valid_user_list

valid_user_list = step4(user_list)


list = []
for i in valid_user_list:
    list.append(i.get('user_id'))
list = set(list)
list2 = [i for i in list]


sportsbaazi(list2)

