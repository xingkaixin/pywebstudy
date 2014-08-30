#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

__author__ = 'XingKaiXin.me'

import exifread
import os
from baidu import geoconv
import getimgs

Longitude, Latitude, isSouthorNorth, isEastorWest = "GPS GPSLongitude", "GPS GPSLatitude", \
                                                    "GPS GPSLatitudeRef", "GPS GPSLongitudeRef"
gps = [Longitude, Latitude, isSouthorNorth, isEastorWest]
files = getimgs.getImgs()


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
    gpspoint = geoconv.conv(str(gpstran(gpslongvalues)) + ',' + str(gpstran(gpsLatvalues)))
    point = []
    point.append(gpspoint[0])
    point.append(gpspoint[1])
    point.append(filename)
    return point

def getallimgs():
    a = []
    for f in files:
        a.append(printgps(f))
    return a


