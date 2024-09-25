import json
import time
import requests
import os
import urllib3
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime
from mining.models import MinedData

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
os.environ['http_proxy'] = "http://localhost:8888"
os.environ['https_proxy'] = "http://localhost:8888"

class Command(BaseCommand):
    help = 'Runs the mining script and stores the result in the database'

    def self_call_de_shiprocket(self, awb):
        url = "https://shiprocket.co/pocx/tracking/{}".format(awb)
        headers = {
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br, zstd",
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
        resp = requests.get(url=url, headers=headers, verify=False)
        return resp

    def self_call_darmacompany(self, incrementId):
        url = "https://customer.thedermaco.com/v1/customer/guest/is-repeated-user"
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
        data = {"incrementId": str(incrementId)}
        resp = requests.post(url=url, headers=headers, data=json.dumps(data), verify=False)
        return resp

    def parse_date(self, date_str):
        try:
            # Assuming the date format from the API response is "dd MMM YYYY"
            return datetime.strptime(date_str, '%d %b %Y').strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            self.stderr.write(self.style.ERROR(f"Invalid date format: {date_str}"))
            return None

    def handle(self, *args, **kwargs):
        incrementId = 81008258484
        awb = 151769649489158
        for i in range(100):
            try:
                awb += 1
                DE = self.self_call_de_shiprocket(awb)
                if DE.status_code == 200:
                    tracking_json = DE.json().get('tracking_json', {})
                    company_name = tracking_json.get('company', {}).get('name')
                    if company_name == 'Derma Co':
                        de_order_details = tracking_json.get('order', {})
                        order_id = de_order_details.get('order_id')
                        system_order_id = de_order_details.get('system_order_id')
                        order_date_str = de_order_details.get('order_date')
                        order_date = self.parse_date(order_date_str)
                        order_total = de_order_details.get('order_total')
                        customer_pincode = de_order_details.get('customer_pincode')
                        extra_details = de_order_details
                        createdAt = de_order_details.get('order_date')
                        isUsed= False
                        used_at = None
                        if order_date:
                            # Check if the order_id already exists
                            if not MinedData.objects.filter(order_id=order_id).exists():
                                MinedData.objects.create(
                                    order_id=order_id,
                                    system_order_id=system_order_id,
                                    order_date=order_date,
                                    order_total=order_total,
                                    createdAt=createdAt,
                                    extra_details=extra_details,
                                    isUsed = False,
                                    used_at=None
                                )
                                self.stdout.write(self.style.SUCCESS(f"Successfully stored order ID: {order_id}"))
                            else:
                                self.stdout.write(self.style.WARNING(f"Order ID already exists: {order_id}"))
                    else:
                        self.stdout.write(self.style.WARNING(f"Company name not 'Derma Co': {company_name}"))
                else:
                    self.stderr.write(self.style.ERROR(f"Failed API request: Status code {DE.status_code}"))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Error: {e}"))
