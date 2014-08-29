#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'XingKaiXin.me'


import urllib
import json


def conv(gps):
    url = r'http://api.map.baidu.com/geoconv/v1/?'
    dash = r'&'
    ak = 'ak='+r'kTeTU4YDNM6WtE1xbMwgQvrf'
    coords = 'coords=' + gps

    args = urllib.urlencode([('num', 10), ('page', 0)])
    url = url + coords + dash + ak
    #print url
    data = urllib.urlopen(url, args)

    json_data = json.loads([i for i in data][0])

    #print json_data

    if json_data['status'] == 0:
        return json_data['result'][0]['x'], json_data['result'][0]['y']
    else:
        return