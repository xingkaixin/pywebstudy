#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

__author__ = 'XingKaiXin.me'

import exifread
import os
from baidu import geoconv


Longitude, Latitude, isSouthorNorth, isEastorWest = "GPS GPSLongitude", "GPS GPSLatitude", \
                                                    "GPS GPSLatitudeRef", "GPS GPSLongitudeRef"
gps = [Longitude, Latitude, isSouthorNorth, isEastorWest]
files = [r'./gpsimg/a.jpg', r'./gpsimg/b.jpg', r'./gpsimg/c.jpg', r'./gpsimg/d.jpg']


def printgps(file):
    filename = os.path.split(file)[1]
    with open(file, 'rb') as f:
        tags = exifread.process_file(f)

    gpsdict = {}
    for tag in tags.keys():
        if tag in gps:
            gpsdict[tag] = tags[tag]

    def gpstran(a):
        j = []
        for i in a:
            j.append(i.num/i.den)
        return j[0] + j[1]/60.0 + j[2]/3600.0

    gpsisSourthorNorth = gpsdict[isSouthorNorth].values
    gpsisEastorWest = gpsdict[isEastorWest].values
    gpsLatvalues = gpsdict[Latitude].values
    gpslongvalues = gpsdict[Longitude].values
    # print filename, gpsisEastorWest, gpstran(gpslongvalues), gpsisSourthorNorth, gpstran(gpsLatvalues)
    print filename, geoconv.conv(str(gpstran(gpslongvalues)) + ',' + str(gpstran(gpsLatvalues)))

for f in files:
    printgps(f)

