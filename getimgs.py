#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'XingKaiXin.me'

import os

def getImgs():
    path = './gpsimg'
    actimgs = []
    imgs = os.listdir(path)
    for i in imgs:
        actimgs.append(path+"/"+i)
    return actimgs
