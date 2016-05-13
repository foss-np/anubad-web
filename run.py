#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
#sys.path.append('libs')

from bottle import route, static_file, default_app
from app.controllers import *


@route('/stat/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./stat/')

from bottle import run, debug
debug(True)
run(host='localhost', port=8080, reloader=True)

## gunicorn
#app = default_app()