#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
#sys.path.append('libs')

from bottle import route, static_file, default_app
from app.controllers import *


@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

from bottle import run, debug
debug(True)
run(host='localhost', port=9009, reloader=True)

## gunicorn
#app = default_app()
