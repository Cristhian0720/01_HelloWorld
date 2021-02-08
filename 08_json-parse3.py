# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 06:12:21 2021

@author: CRISTHIAN TIPAN
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "IuKFwRcqRzo6EVYArkxbNUZsshHr0Z8D"

while True:
    orig = input("Starting location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL:" + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A sucessfull route call.\n")
    
    