from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Annotated
from models import Base, Transaction
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import random


#Base.metadata.create_all(bind=engine)



app = FastAPI()

class TransactionBase(BaseModel):
    id : int
    balance : float 
    statement : str
    user_id: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/transaction/{id}")
async def find_transaction(id: int, db: db_dependency):
    t = db.query(Transaction).filter(Transaction.id == id).first()
    if not t:
        raise HTTPException(status_code=404, detail="transaction not found")
    return t

@app.get("user/transactions")
async def find_transactions(): #jwt user id http only cookie
    return

@app.post("/transactions")
def create_transaction(t :TransactionBase, db :db_dependency):
    db_transaction = Transaction(id=t.id,balance=t.balance,statement=t.statement)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return status.HTTP_200_OK
  

hogwarts_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
@app.get("/home/{id}")
def find_home(id: str):
    if id == "Yusuf":
        return hogwarts_houses[3]
    else:
        i = random.randint(0, 3)
        print(i)
        return hogwarts_houses[i]