# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:57:31 2016

@author: Shen
"""

import LogIn

username = ''
password = ''

b,opener = LogIn.LogIn(username,password)
print b
if b:
    doc = opener.open('http://www.baidu.com').read()
    index = doc.find(username)
    print index