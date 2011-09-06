#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# socketChecker.py
# Copyright 2011 by Dominic Miglar

import socket

def socketChecker(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        return True
    except:
        return False
        
