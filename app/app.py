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

@app.post("/user",tags=['USER'])
def index(user: UserBase, db: Session = Depends(get_db)):
    db_user = User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user