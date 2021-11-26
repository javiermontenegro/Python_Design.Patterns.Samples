#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#*********************************************************************
# Filename:   Python_SQLite3.Connection_Singleton.Pattern.py
# Author:     Javier Montenegro (javiermontenegro.github.io)
# Copyright:  @2020
# Details:    this gist is a example of singleton pattern in Python
#*********************************************************************

import sqlite3

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqllite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print ("Connection db1", db1)
print ("Connection db2", db2)