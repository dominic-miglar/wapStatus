#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# gameStatus.py
# Copyright 2011 by Dominic Miglar

#from config import host, services
from socketChecker import socketChecker

def gameStatus(services):
    returnDict = {}
    #for game, port in services.iteritems():
    #    status = socketChecker(host, port)
    #    if status:
    #        status = 'Online'
    #    else: 
    #        status = 'Offline'
    #    gameStatusDict = { game: status }
       
    for service in services:
        if service.status():
            status = 'Online'
        else:
            status = 'Offline'
        
        gameStatusDict = { service.name: status }
        returnDict.update(gameStatusDict)
    return returnDict
