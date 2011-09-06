#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# config.py
# Copyright 2011 by Dominic Miglar


# from '/' -> redirect to this link
mainPath = '/status'

# the host on which the services below are running
host = 'main.we-are-players.de'

# the services-list, to add a new service, just put them into this list
# format: 'name': 'port'
services = { 'MineCraft1': '25565',
             'MineCraft2': '25566',
             'MineCraft3': '25567',
             'CounterStrike_Source': '27015',
             'TeamFortress2': '27066',
             'OpenSim_GridSrv': '8002',
             'OpenSim_SimSrv1': '9000' }


