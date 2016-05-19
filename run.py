#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
#sys.path.append('libs')

from bottle import route, static_file, default_app
from app.controllers import *


@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

from bottle import run, debug
run(server='gunicorn', host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True, workers=10)

## gunicorn
#app = default_app()
