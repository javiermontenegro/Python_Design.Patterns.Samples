#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#*********************************************************************
# Filename:   Python_Process.Order_Command.Pattern.py
# Author:     Javier Montenegro (javiermontenegro.github.io)
# Copyright:  @2019
# Details:    this gist is a example of command pattern in Python
#*********************************************************************

# Abstract Command class
class Order(ABC):

    @abstractmethod
    def process(self):
        pass

# Concrete Command class
class BuyStock(Order):
    def __init__(self, stock):
        self.stock = stock

    def process(self):
        self.stock.buy()

# Concrete Command class
class SellStock(Order):
    def __init__(self, stock):
        self.stock = stock

    def process(self):
        self.stock.sell()

# Receiver class
class Trade:
    def buy(self):
        print("Stock buy request placed.")

    def sell(self):
        print("Stock sell request placed.")


class Invoker:
    def __init__(self):
        self._queue = []

    def process_order(self, order):
        self._queue.append(order)
        order.process()

trade = Trade()
buy_stock = BuyStock(trade)
sell_stock = SellStock(trade)

invoker = Invoker()
invoker.process_order(buy_stock)
invoker.process_order(sell_stock)
