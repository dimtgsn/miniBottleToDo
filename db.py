from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
import psycopg2


Base = declarative_base()

DATABASE = {
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'pass': '171512',
    'database': 'todolist'
}


class ToDoItem(Base):
    
    __tablename__ = 'tasks'

    uid = Column(Integer, primary_key=True)
    description = Column(String(255))
    is_completed = Column(Boolean, default=False)

    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description.lower()
