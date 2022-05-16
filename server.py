from bottle import *


class ToDoItem:
    def __init__(self, description):
        self.description = description
        self.is_complete = False

    def __str__(self):
        return self.description


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')


@route('/')
@view('index')
def index():
    pass


@route('/ToDoList')
@view('ToDoList')
def to_do_list():
    tasks = [
        ToDoItem('поспать'),
        ToDoItem('поесть'),
        ToDoItem('питон'),
    ]
    return {'tasks': tasks}


run(
    port=8000, host='localhost'
)
