from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, ToDoItem, DATABASE
import psycopg2

engine = create_engine(f"postgresql+psycopg2://{DATABASE['username']}:{DATABASE['pass']}@{DATABASE['host']}/{DATABASE['database']}", echo=True)
engine.connect()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
s = Session()

for desc in ("прочитать книгу", "научиться жонглировать", "выучить новый язык"):
    s.add(ToDoItem(desc))

s.commit()
