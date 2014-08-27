#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

__author__ = 'XingKaiXin.me'

import exifread

f = open(r'./gpsimg/d.jpg', 'rb')

Longitude = "GPS GPSLongitude"
Latitude = "GPS GPSLatitude"
isSouthorNorth = "GPS GPSLatitudeRef"
isEastorWest = "GPS GPSLongitudeRef"

gps = [Longitude, Latitude, isSouthorNorth, isEastorWest]
tags = exifread.process_file(f)
f.close()
gpsdict = {}
for tag in tags.keys():
    if tag in gps:
        #print "Key: %s, value %s" % (tag, tags[tag])
        gpsdict[tag] = tags[tag]
    # else:
    # 	print "Key: %s, value %s" % (tag, tags[tag])

# def gpstran(a):
# 	return a[0] + a[1]/60 + a[2]/3600

# print gpsdict[Latitude], gpstran(gpsdict[Latitude])
# print gpsdict[Longitude], gpstran(gpsdict[Longitude])


def gpstran(a):
    j = []
    for i in a:
        j.append(i.num/i.den)
        #print j
    return j[0] + j[1]/60.0 + j[2]/3600.0

gpsLatvalues = gpsdict[Latitude].values
gpslongvalues = gpsdict[Longitude].values
print gpsLatvalues, gpslongvalues
# #print gpsvalues, gpsvalues[0],gpsvalues[1],dir(gpsvalues[2])
# print gpsvalues[0],dir(gpsvalues[0]), gpsvalues[0].den,gpsvalues[0].num
# print gpsvalues[1],dir(gpsvalues[1]), gpsvalues[1].den,gpsvalues[1].num
# print gpsvalues[2],dir(gpsvalues[2]), gpsvalues[2].den,gpsvalues[2].num
print gpstran(gpsLatvalues), gpstran(gpslongvalues)
