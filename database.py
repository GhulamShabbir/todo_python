# database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
SQLALCHEMY_DATABASE_URL = "postgresql://ghulamshabbir1234567:ZwecNslv1id3@ep-long-rice-78270144.us-east-2.aws.neon.tech/fastapi-todo?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)


class TodoCreate(BaseModel):
    title: str
    description: str

class TodoUpdate(BaseModel):
    title: str
    description: str

class TodoInDB(Todo):
    pass

class TodoInResponse(BaseModel):
    id: int
    title: str
    description: str

