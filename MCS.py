#!/usr/bin/env python3
import time  
import requests  
import json  
import random

deviceId = "D3pjG0LF"  
deviceKey = "0gMx4NKky1UpENZK"

def post_to_mcs(payload):  
  host = "http://api.mediatek.com"
  endpoint = "/mcs/v2/devices/" + deviceId + "/datapoints"
  # url = ''.join([host,endpoint])
  url = host + endpoint
  headers = {"Content-type": "application/json", "deviceKey": deviceKey}
  r = requests.post(url,headers=headers,data=json.dumps(payload))
  print(payload)
  print(r.text)
  print(r.url)

while True:  
  h0 = random.randint(0,30)
  t0 = random.randint(0,30)
  payload = {"datapoints":[{"dataChnId":"Humidity","values":{"value":h0}},{"dataChnId":"Temperature","values":{"value":t0}}]}
  post_to_mcs(payload)
  time.sleep(10)
