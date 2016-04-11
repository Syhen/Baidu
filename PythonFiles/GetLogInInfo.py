# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 20:10:15 2016

@author: Shen
"""


import time
import random
import math
import json


def guideRandom():
    stype = 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'
    i = 0
    while i < len(stype):
        stype = stype[0:i] + getRep(str(stype[i:i+1])) + stype[i+1:]
        i += 1
    return stype
    
def getRep(s):
    b = True
    if s == '-' or s == '4':
        b = False
        v = s
    if b:
        r = int(random.random()*16) | 0
        v = r
        if s == 'y':
            v = r & 3 | 8
        v = hex(v)[2:].upper()
    return v

def getTT():
    t = time.time()
    st = str(t)
    st = st.replace(".","")
    st = st + '0' * (13-len(st))
    return st

def ten2n(number,n):
    temp = []
    loop = '0123456789abcdefghijklmnopqrstuvwxyz'
    while number != 0:
        temp.append(loop[number % n])
        number = number / n
    temp.reverse()
    s = ""
    for t in temp:
        s = s + t
    return s

def get_callback():
    return ten2n(int(math.floor(random.random() * 2147483648)),36)


def getToken(opener,gid,tt,callback):
    url = 'https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3&tt='+tt+'&class=login&gid='+gid+'&logintype=dialogLogin&callback=bd__cbs__' + callback
    doc1 = opener.open(url).read()
#    doc1 = urllib2.urlopen(url).read()
    j = json.loads(doc1[16:-1].replace('\'','"'))
    token = j['data']['token']
    return token
    
def getKeys(opener,token,gid,tt,callback):
    url = 'https://passport.baidu.com/v2/getpublickey?token='+token+'&tpl=mn&apiver=v3&tt='+tt+'&gid='+gid+'&callback=bd__cbs__'+callback
#    con = urllib2.urlopen(url)
    con = opener.open(url)
    doc = con.read()
    j = json.loads(doc[16:-1].replace('\'','"'))
    pubkey = j['pubkey']
    key = j['key']
    return pubkey,key

