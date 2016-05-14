#!/usr/bin/python
#coding=utf-8

import quickfix as fix
import quickfix44 as fix44
import uuid

import DefineField as myfix

class MarketDataReq():

    def __init__(self, sessionID):
        self.sessionID = sessionID

    def GetMarketData(self):
        message = fix.Message ()
        header = message.getHeader()
        header.setField(fix.MsgType (fix.MsgType_MarketDataRequest))
 
        noRelatedSym = fix44.MarketDataRequest().NoRelatedSym()
        noRelatedSym.setField(fix.Symbol('XBTCNY'))
        message.addGroup(noRelatedSym)
 
        message.setField(fix.NoRelatedSym(1))
        message.setField(fix.MDReqID('1'))
        message.setField(fix.SubscriptionRequestType('0'))
        message.setField(fix.MarketDepth(10))
        group = fix44.MarketDataRequest().NoMDEntryTypes()
        group.setField(fix.MDEntryType('0'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('1'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('2'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('3'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('4'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('5'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('6'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('7'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('8'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('9'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('A'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('B'))
        message.addGroup(group)
        group.setField(fix.MDEntryType('C'))
        message.addGroup(group)
 
        fix.Session.sendToTarget(message, self.sessionID)
