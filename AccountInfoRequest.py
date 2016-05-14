#!/usr/bin/python
#coding=utf-8

import quickfix as fix
import quickfix44 as fix44
from hashlib import sha1
from hmac import new as hmac
import hashlib
import uuid
import time
import base64

import DefineField as myfix

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


class AccountInfoReq():

    def __init__(self, sessionID):
        self.sessionID = sessionID

    def GetAccountInfo(self,accessKey, secretKey):
        message = fix.Message ()
        header = message.getHeader()
        header.setField(fix.MsgType ('U1000'))
        account = GenAccountString(accessKey, secretKey).getAccountString()
        message.setField(fix.Account(account))
        accReqID = str(uuid.uuid1())
        message.setField(myfix.AccReqID(accReqID)) 
        fix.Session.sendToTarget(message, self.sessionID)
