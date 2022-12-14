"""empty message

Revision ID: 47c8f9fccf79
Revises: 456891f2fed5
Create Date: 2022-12-02 21:30:42.862344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47c8f9fccf79'
down_revision = '456891f2fed5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('imagen_producto',
    sa.Column('id_imagen', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=128), nullable=False),
    sa.Column('data', sa.LargeBinary(), nullable=False),
    sa.Column('renderate_date', sa.Text(), nullable=False),
    sa.Column('idProducto', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idProducto'], ['producto.idProducto'], ),
    sa.PrimaryKeyConstraint('id_imagen')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('imagen_producto')
    # ### end Alembic commands ###
