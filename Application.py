#!/usr/bin/python
#coding=utf-8

import quickfix as fix
import quickfix44 as fix44
from AccountInfoRequest import AccountInfoReq
from MarketDataRequest import MarketDataReq
import Message

class Application (fix.Application):

    def onCreate (self, sessionID):
        self.sessionID = sessionID
        print ("Session created - sessionID: " + sessionID.toString ())

    def onLogon (self, sessionID):
        print "Logon", sessionID

    def onLogout (self, sessionID):
        print "Logout", sessionID 

    def toAdmin (self, message, sessionID):
        pass 

    def fromAdmin (self, message, sessionID):
        pass
       
    def fromApp (self, message, sessionID):
        Message.onMessage(message)
             
    def toApp (self, message, sessionID):
        pass
       
    def run(self, accesskey, secretkey):
        AccountReq = AccountInfoReq(self.sessionID)
        MarketReq = MarketDataReq(self.sessionID)
        print '''
        define requests here
        '''
        AcountReq.GetAccountInfo(accesskey, secretkey)
        MarketReq.GetMarketData()
            

