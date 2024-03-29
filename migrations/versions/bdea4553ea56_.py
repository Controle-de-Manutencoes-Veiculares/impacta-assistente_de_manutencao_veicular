"""empty message

Revision ID: bdea4553ea56
Revises: 
Create Date: 2024-03-09 12:04:39.104595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdea4553ea56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id_cliente', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('sexo', sa.String(length=100), nullable=True),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('cpf', sa.String(length=11), nullable=True),
    sa.Column('nascimento', sa.Date(), nullable=True),
    sa.Column('contato', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('id_cliente'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('id_cliente')
    )
    op.create_table('pecas',
    sa.Column('id_peca', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('km', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('id_peca')
    )
    op.create_table('veiculo',
    sa.Column('id_veiculo', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=True),
    sa.Column('cor', sa.String(length=100), nullable=True),
    sa.Column('placa', sa.String(length=100), nullable=True),
    sa.Column('marca', sa.String(length=100), nullable=True),
    sa.Column('km', sa.Numeric(), nullable=True),
    sa.Column('ano', sa.Numeric(), nullable=True),
    sa.Column('modelo', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['id_cliente'], ['cliente.id_cliente'], ),
    sa.PrimaryKeyConstraint('id_veiculo'),
    sa.UniqueConstraint('id_veiculo')
    )
    op.create_table('veiculo_pecas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_peca', sa.Integer(), nullable=True),
    sa.Column('id_veiculo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_peca'], ['pecas.id_peca'], ),
    sa.ForeignKeyConstraint(['id_veiculo'], ['veiculo.id_veiculo'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('veiculo_pecas')
    op.drop_table('veiculo')
    op.drop_table('pecas')
    op.drop_table('cliente')
    # ### end Alembic commands ###
