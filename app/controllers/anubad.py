# -*- coding:utf-8 -*-

import sys
sys.path.append('libs')

from bottle import route, post, request, redirect
from bottlim import plim_template as template, plim_view as view
from plim import preprocessor

import app.models.en_to_np
model = app.models.en_to_np.EnToNp()

@route('/')
@route('/<page:int>')
def index(page=1):
    #result = model.load(page)
    return template('index')

@route('/search')
def search():
    search_phrase = request.GET.getunicode('phrase').strip()
    try:
        result = model.search(search_phrase)
    except IndexError:
        result = None
    return template('result', result=result)

@route('/api/search')
def api_search():
    search_phrase = request.GET.getunicode('phrase').strip()

    result = model.json_search(search_phrase)
    return str(result)
