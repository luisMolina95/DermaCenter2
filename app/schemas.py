from typing import Literal
from pydantic import BaseModel


class PedidoBase(BaseModel):
    cantidad: int
    producto_id: int
    inventario_id: int
