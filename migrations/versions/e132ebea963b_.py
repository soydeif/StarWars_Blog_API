"""empty message

Revision ID: e132ebea963b
Revises: 5d4f83fbfee1
Create Date: 2021-09-12 11:27:37.634032

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e132ebea963b'
down_revision = '5d4f83fbfee1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.Column('hair_color', sa.String(length=250), nullable=False),
    sa.Column('skin_color', sa.String(length=250), nullable=False),
    sa.Column('birth_year', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('gravity', sa.String(length=250), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('name', sa.String(length=250), nullable=False))
    op.add_column('user', sa.Column('last_name', sa.String(length=250), nullable=False))
    op.add_column('user', sa.Column('username', sa.String(length=250), nullable=False))
    op.alter_column('user', 'is_active',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'is_active',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.drop_column('user', 'username')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'name')
    op.drop_table('favorites')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###