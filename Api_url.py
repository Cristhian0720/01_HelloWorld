# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:34:45 2021

@author: CRISTHIAN TIPAN
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key = "IuKFwRcqRzo6EVYArkxbNUZsshHr0Z8D"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})


print("URL:" + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")