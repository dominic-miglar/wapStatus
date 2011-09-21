#!/usr/bin/env python

# socketChecker.py
# Copyright 2011 by Dominic Miglar

from socketChecker import socketChecker

class Service(object):
    def __init__(self, name, port, hostName):
        self.name = name
        self.port = port
        self.hostName = hostName

    def status(self):           # if socket checker returns true, service is Online, otherwise (false) service is offline   
        return socketChecker(self.hostName, self.port)     


