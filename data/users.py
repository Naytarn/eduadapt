from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    password = Column(String(length=100), nullable=False)
    phone_number = Column(String(length=11), nullable=False)
    lang_lvl = Column(String(length=2), nullable=False)
    native_lang = Column(String(length=100), nullable=False)
    profile_id = Column(Integer, ForeignKey("profile.id"), nullable=False)
    
    profile_data = relationship("Profile", backref="users")