#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'XingKaiXin.me'


import urllib
import json

args = urllib.urlencode([('num', 10), ('page', 0)])
url = 'http://api.map.baidu.com/geoconv/v1/?coords=113.544961111,22.1887777778&from=1&to=5&ak=你的密钥'
data = urllib.urlopen(url, args)

json_data = json.loads([i for i in data][0])


print json_data

for i in json_data:
    print i