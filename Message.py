#!/usr/bin/python
#coding=utf-8

import quickfix as fix
import quickfix44 as fix44

import DefineField as myfix

def Message_W(message):
    noMDEntries = fix.NoMDEntries()
    message.getField(noMDEntries)
    
def Message_U2001(message):
    accReqID = myfix.AccReqID()
    userID = myfix.UserID()
    sumOfDeposit = myfix.SumOfDeposit()
    cash = myfix.Cash()
    totalProfit = myfix.TotalProfit()
    totalSize = myfix.TotalSize()
    totalInitMarginRequired = myfix.TotalInitMarginRequired()
    totalMaintenanceMarginRequired = myfix.TotalMaintenanceMarginRequired()
    usableMargin = myfix.UsableMargin()
    remainEquity = myfix.RemainEquity()
    contractLen = myfix.ContractList()
    contractList = myfix.BtccGroup.ContractList()
    
    message.getField(accReqID)
    message.getField(userID)
    message.getField(sumOfDeposit)
    message.getField(cash)
    message.getField(totalProfit)
    message.getField(totalSize)
    message.getField(totalInitMarginRequired)
    message.getField(totalMaintenanceMarginRequired)
    message.getField(usableMargin)
    message.getField(remainEquity)
    message.getField(contractLen)
    contractList_value = []

    for contractidx in range(1, contractLen.getValue() + 1):
        message.getGroup(contractidx, contractList)

        totalSellSize = myfix.TotalSellSize()
        totalBuySize = myfix.TotalBuySize()
        openPosition = myfix.OpenPosition()
        profit = myfix.Profit()
        marketValue = myfix.MarketValue()
        unchargedFee = myfix.UnchargedFee()
        initMarginRequired = myfix.InitMarginRequired()
        maintenanceMarginRequired = myfix.MaintenanceMarginRequired()
        initMarginFactor = myfix.InitMarginFactor()
        maintenanceMarginFactor = myfix.MaintenanceMarginFactor()

        if contractList.isSetField(totalSellSize):
            contractList.getField(totalSellSize)
        else:
            totalSellSize.setField(-1)
        if contractList.isSetField(totalBuySize):
            contractList.getField(totalBuySize)
        else:
            totalBuySize.setField(-1)
        contractList.getField(openPosition)
        contractList.getField(profit)
        contractList.getField(marketValue)
        contractList.getField(unchargedFee)
        contractList.getField(initMarginRequired)
        contractList.getField(maintenanceMarginRequired)
        contractList.getField(initMarginFactor)
        contractList.getField(maintenanceMarginFactor)
        
        contractNode = {
            'TotalSellSize': totalSellSize.getValue(),
            'TotalBuySize': totalBuySize.getValue(),
            'OpenPosition': openPosition.getValue(),
            'Profit': profit.getValue(),
            'MarketValue': marketValue.getValue(),
            'UnchargedFee': unchargedFee.getValue(),
            'InitMarginRequired': initMarginRequired.getValue(),
            'MaintenanceMarginRequired': maintenanceMarginRequired.getValue(),
            'InitMarginFactor': initMarginFactor.getValue(),
            'MaintenanceMarginFactor': maintenanceMarginFactor.getValue(),
        }
        contractList_value.append(contractNode)

    res = {
        'AccReqID': accReqID.getValue(),
        'UserID': userID.getValue(),
        'SumOfDeposit': sumOfDeposit.getValue(),
        'Cash': cash.getValue(),
        'TotalProfit': totalProfit.getValue(),
        'TotalSize': totalSize.getValue(),
        'TotalInitMarginRequired': totalInitMarginRequired.getValue(),
        'TotalMaintenanceMarginRequired': totalMaintenanceMarginRequired.getValue(),
        'UsableMargin': usableMargin.getValue(),
        'RemainEquity': remainEquity.getValue(),
        'ContractList': contractList_value,
    }
    print res

def onMessage(message):
    msgType = fix.MsgType ()
    message.getHeader ().getField (msgType)
    if (msgType.getValue () == "W"):
        Message_W(message)
    if (msgType.getValue () == "U2001"):
        Message_U2001(message)
