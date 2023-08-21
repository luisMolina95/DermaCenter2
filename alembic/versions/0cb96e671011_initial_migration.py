"""Initial migration

Revision ID: 0cb96e671011
Revises: 
Create Date: 2023-08-20 21:29:28.525034

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0cb96e671011'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productos',
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('descripcion', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('producto_id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('sucursales',
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('descripcion', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('sucursal_id')
    )
    op.create_table('dependientes',
    sa.Column('dependiente_id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('dui', sa.String(), nullable=False),
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursales.sucursal_id'], ),
    sa.PrimaryKeyConstraint('dependiente_id')
    )
    op.create_table('inventarios',
    sa.Column('inventario_id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursales.sucursal_id'], ),
    sa.PrimaryKeyConstraint('inventario_id')
    )
    op.create_table('regentes',
    sa.Column('regente_id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('jvpqf', sa.String(), nullable=False),
    sa.Column('sucursal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sucursal_id'], ['sucursales.sucursal_id'], ),
    sa.PrimaryKeyConstraint('regente_id')
    )
    op.create_table('pedidos',
    sa.Column('pedido_id', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('estado', sa.Enum('ingresado', 'en proceso', 'finalizado', name='estado_pedido'), nullable=False),
    sa.Column('fecha', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('inventario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['inventario_id'], ['inventarios.inventario_id'], ),
    sa.ForeignKeyConstraint(['producto_id'], ['productos.producto_id'], ),
    sa.PrimaryKeyConstraint('pedido_id')
    )
    op.create_table('transferencias',
    sa.Column('transferencia_id', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('inventario_origen_id', sa.Integer(), nullable=False),
    sa.Column('inventario_destino_id', sa.Integer(), nullable=False),
    sa.Column('pedido_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['inventario_destino_id'], ['inventarios.inventario_id'], ),
    sa.ForeignKeyConstraint(['inventario_origen_id'], ['inventarios.inventario_id'], ),
    sa.ForeignKeyConstraint(['pedido_id'], ['pedidos.pedido_id'], ),
    sa.PrimaryKeyConstraint('transferencia_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transferencias')
    op.drop_table('pedidos')
    op.drop_table('regentes')
    op.drop_table('inventarios')
    op.drop_table('dependientes')
    op.drop_table('sucursales')
    op.drop_table('productos')
    # ### end Alembic commands ###