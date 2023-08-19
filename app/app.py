import os
from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import User

from app.schemas import UserBase
app = FastAPI()

@app.get("/",tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong", "extra": os.environ.get('APP_TCP_PORT')}

@app.post("/users",tags=['USERS'])
async def post_user(user: UserBase, db: AsyncSession = Depends(get_db)):
    db_user = User(username=user.username)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@app.get("/users",tags=['USERS'])
async def get_users(db: AsyncSession = Depends(get_db)):
    results = await db.execute(select(User))
    users = results.scalars().all()
    return users