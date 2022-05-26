import os
from bottle import route, view, redirect, static_file, request, run
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import ToDoItem, Base, DATABASE
import psycopg2


engine = create_engine(f"postgresql+psycopg2://{DATABASE['username']}:{DATABASE['pass']}@{DATABASE['host']}/{DATABASE['database']}", echo=True)
engine.connect()
Session = sessionmaker(bind=engine)
s = Session()


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
    tasks = s.query(ToDoItem).order_by(ToDoItem.uid)
    total_tasks = s.query(ToDoItem).count()
    incomplete = s.query(ToDoItem).filter(ToDoItem.is_completed == False).count()
    return {'tasks': tasks,
            'total_tasks': total_tasks,
            'incomplete': incomplete
            }


@route('/ToDoList/add-task', method='POST')
def add_task():
    desc = request.POST.description.strip()
    if len(desc) > 0 and s.query(ToDoItem).filter(ToDoItem.description == desc).count() == 0:
        t = ToDoItem(desc)
        s.add(t)
        s.commit()
    return redirect('/ToDoList')


@route('/api/delete/<uid:int>')
def api_delete(uid):
    s.query(ToDoItem).filter(ToDoItem.uid == uid).delete()
    s.commit()
    return redirect('/ToDoList')


@route('/api/complete/<uid:int>')
def api_complete(uid):
    t = s.query(ToDoItem).filter(ToDoItem.uid == uid).first()
    t.is_completed = True
    s.commit()
    return redirect("/ToDoList")


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8000, debug=True)
