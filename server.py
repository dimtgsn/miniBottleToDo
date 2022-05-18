from bottle import *


class ToDoItem:
    def __init__(self, description, unique_id):
        self.description = description
        self.is_complete = False
        self.uid = unique_id

    def __str__(self):
        return self.description.lower()


tasks_db = {
    1: ToDoItem('поесть', 1),
    2: ToDoItem('поспать', 2),
    3: ToDoItem('питон', 3),
    4: ToDoItem('полежать', 4)
}


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
    tasks = tasks_db.values()
    return {'tasks': tasks}


@route('/ToDoList/add-task', method='POST')
def add_task():

    desc = request.POST.description.strip()

    if (len(desc) > 0) and (desc not in tasks_db.values()):
        new_uid = max(tasks_db.keys()) + 1
        tasks_db[new_uid] = ToDoItem(desc, new_uid)

    redirect('/ToDoList')


@route('/api/complete/<uid:int>')
def api_complete(uid):
    tasks_db[uid].is_complete = True
    redirect('/ToDoList')


@route('/api/delete/<uid:int>')
def api_delete(uid):
    tasks_db.pop(uid)
    redirect('/ToDoList')


run(
    port=8000, host='localhost'
)
