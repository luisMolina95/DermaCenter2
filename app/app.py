import os
from fastapi import Depends, FastAPI
from sqlalchemy import column, select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Sucursal, Regente, Inventario, Transferencia

# from app.schemas import UserBase
app = FastAPI()


@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong", "extra": os.environ.get('APP_TCP_PORT')}

# @app.post("/users",tags=['USERS'])
# async def post_user(user: UserBase, db: AsyncSession = Depends(get_db)):
#     db_user = User(username=user.username)
#     db.add(db_user)
#     await db.commit()
#     await db.refresh(db_user)
#     return db_user


# @app.get("/users",tags=['USERS'])
# async def get_users(db: AsyncSession = Depends(get_db)):
#     query = select(Sucursal, Regente).options(joinedload(Sucursal.regentes))
#     result = await db.execute(query)
#     todo = result.scalars().first()
#     print(todo)
#     return todo

@app.get("/users", tags=['USERS'])
async def get_users(db: AsyncSession = Depends(get_db)):
    query = select(Inventario, Transferencia).where(column("inventario_id") == 1).options(
        joinedload(Inventario.transferencias_destino), joinedload(Inventario.transferencias_origen))
    result = await db.execute(query)
    todo = result.scalars().first()
    print(todo)
    return todo
