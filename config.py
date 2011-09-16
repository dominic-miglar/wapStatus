#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# config.py
# Copyright 2011 by Dominic Miglar

from serviceClass import Service

# from '/' -> redirect to this link
mainPath = '/status'


services = [
            Service(name='MineCraft1', port=25565, hostName='main.we-are-players.de'),
            Service(name='MineCraft2', port=25566, hostName='main.we-are-players.de'),
            Service(name='MineCraft3', port=25567, hostName='main.we-are-players.de'),
            Service(name='CounterStrike Source', port=27015, hostName='main.we-are-players.de'),
            Service(name='Team Fortress 2', port=27066, hostName='main.we-are-players.de'),
            Service(name='OpenSim Grid Srv', port=8002, hostName='main.we-are-players.de'),
            Service(name='OpenSim Sim Srv 01', port=9000, hostName='main.we-are-players.de'),
           ]


