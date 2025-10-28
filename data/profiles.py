from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

from .db_session import SqlAlchemyBase


class Profile(SqlAlchemyBase):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_path = Column(String, default='../assets/default.png')
    
    users = relationship("User", backref="profile_data")