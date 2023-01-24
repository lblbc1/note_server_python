from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "sys_user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    password = Column(String(255))


class Note(Base):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    content = Column(String(255))
