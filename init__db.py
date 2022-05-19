from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, ToDoItem

engine = create_engine("sqlite:///tasks.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
s = Session()

for desc in ("прочитать книгу", "поспать", "поесть"):
    s.add(ToDoItem(desc))

s.commit()
