import os
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User

from app.schemas import UserBase
app = FastAPI()

@app.get("/",tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong", "extra": os.environ.get('APP_TCP_PORT')}

@app.post("/users",tags=['USERS'])
def post_user(user: UserBase, db: Session = Depends(get_db)):
    db_user = User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users",tags=['USERS'])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users