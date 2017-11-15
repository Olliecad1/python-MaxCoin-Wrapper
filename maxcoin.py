#!/usr/bin/env python
# encoding=utf8
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

import json
import urllib2

def GetBlockCount():
    query = urllib2.urlopen('http://api.maxcoinhub.io/Blockchain/GetBlockCount')

    query = query.read()

    j = json.loads(query)

    s = j['result']

    new = str(s)

    print 'Block Count: ' + new

def GetBlockHash():
    query = urllib2.urlopen('http://api.maxcoinhub.io/Blockchain/GetBlockCount')

    query = query.read()

    j = json.loads(query)

    s = j['result']

    new = str(s)

    url = urllib2.urlopen('http://api.maxcoinhub.io/Blockchain/GetBlockHash/' + new)

    url = url.read()

    j = json.loads(url)

    results = j['result']

    code = str(results)

    print 'Block Hash ' + code


def GetBlock():
    query = urllib2.urlopen('http://api.maxcoinhub.io/Blockchain/GetBlockCount')

    query = query.read()

    j = json.loads(query)

    s = j['result']

    new = str(s)

    url = urllib2.urlopen('http://api.maxcoinhub.io/Blockchain/GetBlockHash/' + new)

    url = url.read()

    j = json.loads(url)

    results = j['result']

    code = str(results)

    new = urllib2.urlopen('http://api.maxcoinhub.io/Blockchain/GetBlock/' + code)

    new = new.read()

    j1  = json.loads(new)

    print j1 
   
