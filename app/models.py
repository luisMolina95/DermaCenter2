import datetime
from typing import List, Literal
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum, func, ForeignKey
from app.database import Base


class Sucursal(Base):
    __tablename__ = "sucursales"
    sucursal_id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    descripcion: Mapped[str] = mapped_column(nullable=False)
    regentes: Mapped[List["Regente"]] = relationship(back_populates="sucursal")
    dependientes: Mapped[List["Dependiente"]
                         ] = relationship(back_populates="sucursal")
    inventarios: Mapped[List["Inventario"]] = relationship(
        back_populates="sucursal")


class Regente(Base):
    __tablename__ = "regentes"
    regente_id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    jvpqf: Mapped[str] = mapped_column(nullable=False)
    sucursal_id: Mapped[int] = mapped_column(
        ForeignKey("sucursales.sucursal_id"))
    sucursal: Mapped["Sucursal"] = relationship(back_populates="regentes")


class Dependiente(Base):
    __tablename__ = "dependientes"
    dependiente_id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    dui: Mapped[str] = mapped_column(nullable=False)
    sucursal_id: Mapped[int] = mapped_column(
        ForeignKey("sucursales.sucursal_id"))
    sucursal: Mapped["Sucursal"] = relationship(back_populates="dependientes")


class Inventario(Base):
    __tablename__ = "inventarios"
    inventario_id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    sucursal_id: Mapped[int] = mapped_column(
        ForeignKey("sucursales.sucursal_id"))
    sucursal: Mapped["Sucursal"] = relationship(back_populates="inventarios")
    pedidos: Mapped[List["Pedido"]] = relationship(back_populates="inventario")
    transferencias_origen: Mapped[List["Transferencia"]] = relationship(
        back_populates="inventario_origen", foreign_keys="Transferencia.inventario_origen_id")
    transferencias_destino: Mapped[List["Transferencia"]] = relationship(
        back_populates="inventario_destino", foreign_keys="Transferencia.inventario_destino_id")


class Pedido(Base):
    __tablename__ = "pedidos"
    pedido_id: Mapped[int] = mapped_column(primary_key=True)
    cantidad: Mapped[int] = mapped_column(nullable=False)
    estado: Mapped[Literal["ingresado", "en proceso", "finalizado"]] = mapped_column(
        Enum("ingresado", "en proceso", "finalizado", name="estado_pedido"))
    fecha: Mapped[datetime.datetime] = mapped_column(
        server_default=func.CURRENT_TIMESTAMP())
    producto_id: Mapped[int] = mapped_column(
        ForeignKey("productos.producto_id"))
    producto: Mapped["Producto"] = relationship(back_populates="pedidos")
    inventario_id: Mapped[int] = mapped_column(
        ForeignKey("inventarios.inventario_id"))
    inventario: Mapped["Inventario"] = relationship(back_populates="pedidos")
    transferencias: Mapped[List["Transferencia"]
                           ] = relationship(back_populates="pedido")


class Transferencia(Base):
    __tablename__ = "transferencias"
    transferencia_id: Mapped[int] = mapped_column(primary_key=True)
    fecha: Mapped[datetime.datetime] = mapped_column(
        server_default=func.CURRENT_TIMESTAMP())
    inventario_origen_id: Mapped[int] = mapped_column(
        ForeignKey("inventarios.inventario_id"))
    inventario_origen: Mapped["Inventario"] = relationship(
        foreign_keys="Transferencia.inventario_origen_id", back_populates="transferencias_origen")
    inventario_destino_id: Mapped[int] = mapped_column(
        ForeignKey("inventarios.inventario_id"))
    inventario_destino: Mapped["Inventario"] = relationship(
        foreign_keys="Transferencia.inventario_destino_id", back_populates="transferencias_destino")
    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.pedido_id"))
    pedido: Mapped["Pedido"] = relationship(back_populates="transferencias")


class Producto(Base):
    __tablename__ = "productos"
    producto_id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False, unique=True)
    precio: Mapped[float] = mapped_column(nullable=False)
    descripcion: Mapped[str] = mapped_column(nullable=False)
    pedidos: Mapped[List["Pedido"]] = relationship(back_populates="producto")
