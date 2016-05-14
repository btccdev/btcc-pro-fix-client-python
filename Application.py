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
        AIReq = AccountInfoReq(self.sessionID)
        MDReq = MarketDataReq(self.sessionID)
        print '''
        input 1 to get accountinfo,
        input 2 to get marketdata,
        input Q to quit
        '''
        while True:
            input = raw_input()
            if input == '1':
                AIReq.GetAccountInfo(accesskey, secretkey)
            elif input == '2':
                MDReq.GetMarketData()
            elif input == 'Q':
                break
            else:
                continue

