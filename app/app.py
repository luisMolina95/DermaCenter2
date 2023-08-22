import os
import json
from fastapi import Depends, FastAPI
from sqlalchemy import column, select
from sqlalchemy.orm import joinedload, load_only, lazyload
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Pedido, Inventario, Sucursal

# from app.schemas import UserBase
app = FastAPI()


@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong"}

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

@app.get("/pedidos", tags=['PEDIDOS'])
async def get_pedidos(db: AsyncSession = Depends(get_db)):
    query = select(Pedido).options(load_only(Pedido.estado, Pedido.fecha)).options(joinedload(Pedido.inventario).options(load_only(
        Inventario.sucursal_id)).subqueryload(Inventario.sucursal).options(load_only(Sucursal.nombre)))
    result = await db.execute(query)
    todo = result.unique().scalars().all()
    return {"data": todo}
