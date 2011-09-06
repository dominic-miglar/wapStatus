#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright 2011 by Dominic Miglar

from bottle import route, run, redirect, debug, static_file
from bottle import jinja2_template as template

from config import mainPath, host, services
from gameStatus import gameStatus

@route('/')
def index():
    redirect(mainPath)

@route(mainPath)
def status():
    statusResults = gameStatus(host, services)
    statusResults = statusResults.items() 
    statusResults.sort() 
    return template('child', statuses=statusResults)

@route('/styles/:style')
def styles(style):
    return static_file(style, root='styles')

@route('/pictures/:pic')
def pictures(pic):
    return static_file(pic, root='pictures')

debug(True)
run(host='0.0.0.0', port='8080')


