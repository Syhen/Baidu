# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 18:52:22 2016

@author: Shen
"""

import rsa
import urllib2
import base64
#import M2Crypto

def escapeSymbol(source):
    ls = ['#','&','+','=','/','\\',' ','\f','\r','\n','\t']
    source = source.replace("%","！")
    for l in ls:
        source = source.replace(l,reTo(l))
    source = source.replace("！","%25")
    return source

def reTo(s):
    return "%" + hex(256 + ord(s[0]))[3:].upper()

def getUserName(userName):
    return urllib2.quote(userName)

def getPassword(pwd,pub_key):
    key = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)
    pwd = escapeSymbol(base64.encodestring(rsa.encrypt(pwd, key)))
#    pwd = base64.encodestring(rsa.encrypt(pwd, key))
    return pwd