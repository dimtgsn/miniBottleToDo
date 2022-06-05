import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
import psycopg2


# DATABASE = {
#     'host': 'ec2-3-248-121-12.eu-west-1.compute.amazonaws.com',
#     'port': '5432',
#     'username': 'ohlhfraksogfbn',
#     'pass': '062947cf65f0bdff74c5e167ed22425c04ca909f1be5ba686a498bdca5105b5c',
#     'database': 'deuai0l41nr67p'
# }
DATABASE_URL = "postgresql+psycopg2://" + os.environ['DATABASE_URL'].split("://")[1]
# DATABASE = {
#     'host': 'localhost',
#     'port': '5432',
#     'username': 'postgres',
#     'pass': '171512',
#     'database': 'todolist'
# }


Base = declarative_base()


class ToDoItem(Base):
    
    __tablename__ = 'tasks'

    uid = Column(Integer, primary_key=True)
    description = Column(String(255))
    is_completed = Column(Boolean, default=False)

    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description.lower()
