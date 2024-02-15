from sqlalchemy import Column, ForeignKey, Integer, Float, String
#from sqlalchemy.orm import relationship

from .database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    username = Column(String, default="")

