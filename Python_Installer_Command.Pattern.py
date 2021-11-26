#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#*********************************************************************
# Filename:   Python_Installer_Command.Pattern.py
# Author:     Javier Montenegro (javiermontenegro.github.io)
# Copyright:  @2019
# Details:    this gist is a example of command pattern in Python
#*********************************************************************

class Installer:
    def __init__(self, source, dir):
        self.options = []
        self.dir = dir
        self.source = source

    def add_preferences(self, cmd):
        self.options.append(cmd)

    def install(self):
        for option in self.options:
            value = [v for k, v in option.items()]

            if (value[0]):
                print("installing files -- ", [k for k, v in option.items()], self.source, " to ", self.dir)
            else:
                print('Not installed: ', [k for k, v in option.items()])

installer =  Installer('C++ binaries', 'c:\\c++\\binaries')
installer.add_preferences({'c++':True})
installer.add_preferences({'c#': False})
installer.install()

