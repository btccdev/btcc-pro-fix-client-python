#!/usr/bin/python
#coding=utf-8

import quickfix as fix

class AccReqID(fix.StringField):
    def __init__(self, data = None):
        if data == None:
            fix.StringField.__init__(self, 8000)
        else:
            fix.StringField.__init__(self, 8000, data)

### 用户 id
class UserID(fix.IntField):
    def __init__(self, data = None):
        if data == None:
            fix.IntField.__init__(self, 8002)
        else:
            fix.IntField.__init__(self, 8002, data)

### 充值总和
class SumOfDeposit(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8003)
        else:
            fix.DoubleField.__init__(self, 8003, data)

### 现金
class Cash(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8004)
        else:
            fix.DoubleField.__init__(self, 8004, data)

### 总盈亏
class TotalProfit(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8005)
        else:
            fix.DoubleField.__init__(self, 8005, data)

### 总量
class TotalSize(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8006)
        else:
            fix.DoubleField.__init__(self, 8006, data)

### 总共必须的初始保证金
class TotalInitMarginRequired(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8007)
        else:
            fix.DoubleField.__init__(self, 8007, data)

### 总共必须的维持保证金
class TotalMaintenanceMarginRequired(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8009)
        else:
            fix.DoubleField.__init__(self, 8009, data)

### 可用的保证金
class UsableMargin(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8010)
        else:
            fix.DoubleField.__init__(self, 8010, data)

### 保留的仓位
class RemainEquity(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8011)
        else:
            fix.DoubleField.__init__(self, 8011, data)

### 总卖量
class TotalSellSize(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8012)
        else:
            fix.DoubleField.__init__(self, 8012, data)

### 总买量
class TotalBuySize(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8013)
        else:
            fix.DoubleField.__init__(self, 8013, data)

### 持仓数量
class OpenPosition(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8014)
        else:
            fix.DoubleField.__init__(self, 8014, data)

### 收益
class Profit(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8015)
        else:
            fix.DoubleField.__init__(self, 8015, data)

### 市场价
class MarketValue(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8016)
        else:
            fix.DoubleField.__init__(self, 8016, data)

### 待收手续费
class UnchargedFee(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8017)
        else:
            fix.DoubleField.__init__(self, 8017, data)

### 需要的初始保证金
class InitMarginRequired(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8018)
        else:
            fix.DoubleField.__init__(self, 8018, data)

### 需要的维持保证金
class MaintenanceMarginRequired(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8019)
        else:
            fix.DoubleField.__init__(self, 8019, data)

### 初始保证金比例
class InitMarginFactor(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8020)
        else:
            fix.DoubleField.__init__(self, 8020, data)

### 维持保证金比例
class MaintenanceMarginFactor(fix.DoubleField):
    def __init__(self, data = None):
        if data == None:
            fix.DoubleField.__init__(self, 8021)
        else:
            fix.DoubleField.__init__(self, 8021, data)
### 合约数量
class ContractList(fix.IntField):
    def __init__(self, data = None):
        if data == None:
            fix.IntField.__init__(self, 9001)
        else:
            fix.IntField.__init__(self, 9001, data)
class BtccGroup():
    ### 合约Group
    class ContractList(fix.Group):
        def __init__(self):
            order = fix.IntArray(13)
            order[0] = 55
            order[1] = 8012
            order[2] = 8013
            order[3] = 8014
            order[4] = 6
            order[5] = 8015
            order[6] = 8016
            order[7] = 8017
            order[8] = 8018
            order[9] = 8019
            order[10] = 8020
            order[11] = 8021
            order[12] = 0
            fix.Group.__init__(self, 9001, 55, order)
        
