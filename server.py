from bottle import *


@route('/static/style.css')
def send_static():
    return static_file('style.css', root='static')


@route('/')
@view('index')
def index():
    pass


run(
    port=8000, host='localhost'
)
