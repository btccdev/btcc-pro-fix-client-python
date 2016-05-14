#!/usr/bin/python
#coding=utf-8
from hashlib import sha1
from hmac import new as hmac
import hashlib
import time
import base64

class GenAccountString():
    def __init__(self, accesskey, secretkey):
        self.accesskey = accesskey
        self.secretkey = secretkey
    def bytArrayToHex(self):
        pass

    def getSignature(self, data, key):
        return "%s" % hmac(key, data, sha1).digest().encode('base64')[:-1]

    def getAccountString(self):
        methodstr = "method=getForwardsAccountInfo&params="
        tonce = '%d'%(time.time() * 1000000)
        params = "tonce=" + tonce + "&accesskey=" + self.accesskey + "&requestmethod=post&id=1&" + methodstr
        hash = hmac(self.secretkey, params, hashlib.sha1).hexdigest()
        userpass = self.accesskey + ":" + hash;
        userpass = base64.b64encode(userpass)
        basicAuth = "%s:Basic %s"%(tonce,userpass)
        return basicAuth

