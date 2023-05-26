from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Role(Base):
    __tablename__ = 'tb_role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

class User(Base):
    __tablename__ = 'tb_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    midlename = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    birthdate = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    old_password = Column(String(255), nullable=False)
    is_activate = Column(Boolean, nullable=True)
    role_id = Column(Integer, ForeignKey('tb_role.id'), nullable=False)
    photo_id = Column(Integer, ForeignKey('tb_profile_photo.id'), nullable=True)
    role = relationship('Role', backref='users')
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

class Photo(Base):
    __tablename__ = 'tb_profile_photo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo_name = Column(String(255), nullable=False)
    photo_url = Column(Text, nullable=False)
    is_activate = Column(Boolean, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

