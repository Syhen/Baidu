# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:08:18 2016

@author: Shen
"""

import urllib2
import urllib
import cookielib
import GetEncoding
import GetLogInInfo

def LogIn(username,password):
    url_main = 'http://www.baidu.com'
    tt = GetLogInInfo.getTT()
    gid = GetLogInInfo.guideRandom()
    callback = GetLogInInfo.get_callback()
    url_login = 'https://passport.baidu.com/v2/api/?login'
    
    token = ""
    cookie = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    
    while len(token) != 32:
        token = GetLogInInfo.getToken(opener,gid,tt,callback)
    
    pubkey,key = GetLogInInfo.getKeys(opener,token,gid,tt,callback)
    
    strcookie = cookie.as_lwp_str()
    s = ""
    for i in strcookie.split('\n'):
        if i == "":
            break
        s = s + i.split(';')[0]
    s = s.replace('Set-Cookie3: ',';')
    s = s.replace('\"','')
    s = s[1:]
    
    pwd = GetEncoding.getPassword(password,pubkey)
    usnm = GetEncoding.getUserName(username)
    headers = {
        "Accept":"text/html, application/xhtml+xml, */*",
        "Referer":"https://www.baidu.com/",
        "Accept-Language":"zh-CN",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Content-Type":"application/x-www-form-urlencoded",
    #    "Accept-Encoding":"gzip, deflate",
        "Host":"passport.baidu.com",
        "Content-Length":"746",
        "DNT":"1",
        "Connection":"Keep-Alive",
        "Cache-Control":"no-cache",
        "cookie":s
    }
    
    data = {
        "staticpage":"https%3A%2F%2Fwww.baidu.com%2Fcache%2Fuser%2Fhtml%2Fv3Jump.html",
        "charset":"utf-8",
        "token":token,
        "tpl":"mn",
        "subpro":"",
        "apiver":"v3",
        "tt":tt,
        "codestring":"",
        "safeflg":"0",
        "u":"https%3A%2F%2Fwww.baidu.com%2F",
        "isPhone":"false",
        "detect":"1",
        "gid":gid,
        "quick_user":"0",
        "logintype":"dialogLogin",
        "logLoginType":"pc_loginDialog",
        "idc":"",
        "loginmerge":"true",
        "splogin":"rate",
        "username":usnm,
        "password":pwd,
        "verifycode":"",
        "mem_pass":"on",
        "rsakey":key,
        "crypttype":"12",
        "ppui_logintime":"7923",
        "countrycode":"",
        "callback":"parent.bd__pcbs__"+callback
    }
    
    postDate = urllib.urlencode(data)
    postDate = postDate.replace('%25','%')
    req = urllib2.Request(
        headers = headers,
        data = postDate,
        url = url_login
    )
    
    rst = opener.open(req)
    
    doc = rst.read()
    
    doc2 = opener.open(url_main).read()
    index = doc2.find('登录')
    b = False
    if index == -1:
        b = True
    return b,opener