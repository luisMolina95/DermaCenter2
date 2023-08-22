from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.orm import joinedload, load_only
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Pedido, Inventario, Sucursal
from app.schemas import PedidoBase

app = FastAPI()


@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong"}


@app.post("/pedidos", status_code=201, tags=['PEDIDOS'])
async def post_user(pedido: PedidoBase, db: AsyncSession = Depends(get_db)):
    db_pedido = Pedido(producto_id=pedido.producto_id, inventario_id=pedido.inventario_id,
                       cantidad=pedido.cantidad, estado="ingresado")
    db.add(db_pedido)
    await db.commit()
    await db.refresh(db_pedido)
    return {"data": db_pedido}


@app.get("/pedidos/{id}", tags=['PEDIDOS'])
async def read_item(id: int, db: AsyncSession = Depends(get_db)):
    query = select(Pedido).options(joinedload(Pedido.producto)).options(joinedload(Pedido.inventario).subqueryload(
        Inventario.sucursal).subqueryload(Sucursal.regentes)).where(Pedido.pedido_id == id)
    result = await db.execute(query)
    todo = result.scalar()
    return {"data": todo}


@app.get("/pedidos", tags=['PEDIDOS'])
async def get_pedidos(db: AsyncSession = Depends(get_db)):
    query = select(Pedido).options(load_only(Pedido.estado, Pedido.fecha)).options(joinedload(Pedido.inventario).options(load_only(
        Inventario.sucursal_id)).subqueryload(Inventario.sucursal).options(load_only(Sucursal.nombre)))
    result = await db.execute(query)
    todo = result.unique().scalars().all()
    return {"data": todo}
