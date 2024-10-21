
import  time,random,os,requests,json,datetime
import uuid


import mysql.connector as mysql

conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend", passwd="123admin!", database="techteam")
cursor = conn.cursor()
def get_ip_info():
    ipInfo= {}
    try:
        if not ipInfo:
            response = requests.get(url="http://ip-api.com/json/?fields=61439")
            if response.status_code == 200:
                data = json.loads(response.content)
                ipInfo = {
                    "city": str(data.get("city", "")).lower(),
                    "region": str(data.get("regionName", "")).lower(),
                    "pincode": str(data.get("zip", "")).lower(),
                    "lat": data.get("lat", 0.0),
                    "lon": data.get("lon", 0.0),
                    "isp": data.get("isp", ""),
                    "ip": data.get("query", ""),
                    "country": str(data.get("countryCode", "")),

                }
    except:
        pass
    try:
        if not ipInfo:
            response = requests.get(url="http://lumtest.com/echo.json")
            if response.status_code == 200:
                data = json.loads(response.content)
                if "geo" in data:
                    ipInfo = {
                        "city": str(data["geo"].get("city", "")).lower(),
                        "region": str(data["geo"].get("region_name", "")).lower(),
                        "pincode": str(data["geo"].get("postal_code", "")).lower(),
                        "lat": data["geo"].get("latitude", 0.0),
                        "lon": data["geo"].get("longitude", 0.0),
                        "country": str(data.get("country", "")),
                    }
                ipInfo["ip"] = data.get("ip", "")
                ipInfo["isp"] = data.get("asn", {}).get("org_name", "")
    except:
        pass

    return ipInfo





def self_call_sam_com_validation(user_id):
    url = "https://tradws.stocknote.com/samco-webservice/AOF/KycStatus/1.0.0"
    method = "post"

    headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept-Encoding": "gzip",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36"
    }
    params = {}


    data = {"request":{"appID":str(uuid.uuid4()).replace('-',''),"formFactor":"M","requestType":"U","response_format":"json","data":{"user_id":str(user_id)}}}


    response = requests.post(url=url,params=params,headers=headers,data=json.dumps(data),verify=False)
    return response


def get_last_orderid():
    conn = mysql.connect(host="rds-datapis.cd89nha3un9e.us-west-2.rds.amazonaws.com", user="team2backend",passwd="123admin!", database="techteam")
    cursor = conn.cursor()
    cursor.execute('''SELECT DISTINCT user_id FROM samco_userIds''')
    data = cursor.fetchall()
    user_id = list(data[-1])[0]
    cursor.close()
    return int(user_id)
last_user_id = get_last_orderid()

print(last_user_id)


user_id = int(last_user_id)
cursor.execute('''SELECT DISTINCT user_id FROM samco_userIds''')
for i in range(50):

    zone = "dc_t2"
    password = "4p2hpz54qqp7"
    session = "{}{}".format(str(int(time.time() * 1000)), random.randint(100000, 999999))
    country = "IN"
    proxy_str = 'http://brd-customer-hl_c7dea9fc-zone-{}-country-{}-session-{}:{}@brd.superproxy.io:22225'.format(zone,str(country).lower(),session,password)
    os.environ['https_proxy'] = proxy_str
    os.environ['http_proxy'] = proxy_str
    user_id = user_id+1
    user_data = self_call_sam_com_validation(user_id)
    print(get_ip_info())

    rows = cursor.fetchall()
    if user_data.status_code==200:
        if user_data.json().get('response').get('data').get('user_details').get('client_id') != '':
            user_details = user_data.json().get('response').get('data').get('user_details')
            print(json.dumps(user_details))
            print(user_details.get('user_id'))


            if user_details.get('client_id') != '':
                data = user_details.get("mobile") + ", " + user_details.get("email")

                created_at = str(datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S:%f")[:-3])

                cursor.execute('''INSERT INTO samco_userIds (created_at, isUsed, user_id, user_details)
                                         VALUES ('{}',0, '{}', '{}')'''.format(created_at, str(user_id),
                                                                               json.dumps(user_details)))
                conn.commit()

























