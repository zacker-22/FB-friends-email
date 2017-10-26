# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:50:49 2017

@author: Zacker
"""

import sys
import re
import urllib
import urllib2
import cookielib
import requests
import json
import os
import time

username = ""
password = ""

CHandler = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
browser = urllib2.build_opener(CHandler)
browser.addheaders = [('User-agent', 'InFB - ruel@ruel.me - http://ruel.me')]
urllib2.install_opener(browser)
res = browser.open('http://m.facebook.com/index.php')
temp=res.read()

mxt = re.search('name="post_form_id" value="(\w+)"', temp)

res.close()
data = urllib.urlencode({
		'lsd'				: '',
		'charset_test' 		: urllib.unquote_plus('%E2%82%AC%2C%C2%B4%2C%E2%82%AC%2C%C2%B4%2C%E6%B0%B4%2C%D0%94%2C%D0%84'),
		'email'				: username,
		'pass'				: password,
		'login'				: 'Login'
	})

acct = "EAACEdEose0cBAEoV4BPwX8dGGuGu1EEm0mni8AqPGGdyZApwLJlK0VIbh9nQ7WhF3dS7yNGHs76Flz4XtwPbPcernhc269ZBYZCAkkhuTG4HR45XUCawb1q7G96k7KsZA7UkUFSMGKFqBN5lfIeXe6n21UhHVuQiarSRU4NiNfrl7JkH3PncrDMWwTRR11PhLZBjThQrqfwZDZD"
res = browser.open('https://www.facebook.com/login.php?m=m&refsrc=http%3A%2F%2Fm.facebook.com%2Findex.php&refid=8', data)
"""
print 'Using access token: %s' % acct
res = browser.open('https://graph.facebook.com/me/friends?access_token=%s' % acct)
fres = res.read()
jdata = json.loads(fres)
"""
temp=res.read()
ind=temp.index("pymmList:null,groups:[],list:")
temp=temp[ind+29:]
ind=temp.index("]")
temp=temp[:ind+1]
temp=temp.strip("[")
temp=temp.strip("]")
friends_id_list=temp.split(",")
friends_id_list=[x[1:-3] for x in friends_id_list]
count=0
friends_id_list=list(set(friends_id_list))

for idd in friends_id_list:
    fid = idd;count+=1
  

	# Go to ID's profile
    res = browser.open('http://m.facebook.com/profile.php?id=%s&v=info&refid=17' % fid)
    html = res.read()
    xma = re.search('mailto:(.*?)"', html)
    data= requests.get('https://graph.facebook.com/'+fid+"?access_token="+acct)
    
    jdata=json.loads(data.text)
    if "name" in jdata:
            name=jdata["name"]
            print name , 
            if xma:
        		# Replace the html entity from the scraped information
                email = xma.group(1).replace('%40', '@')
                
                print " "*(30-len(name))+email
            else:
                print " "*(30-len(name))+"Email not Visible"
