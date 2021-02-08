# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 06:36:57 2021

@author:
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key = "IuKFwRcqRzo6EVYArkxbNUZsshHr0Z8D"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)
