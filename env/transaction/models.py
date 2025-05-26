from sqlalchemy import String, Column, Integer, Float, ForeignKey
from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True)
    email= Column(String, unique=True)
    password = Column(String)


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Float(2)) 
    statement = Column(String(500))
    user_id= Column(Integer, ForeignKey("user.id"))

