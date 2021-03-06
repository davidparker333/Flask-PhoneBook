"""empty message

Revision ID: 849477078617
Revises: b3dd1f9c6aa9
Create Date: 2021-05-12 18:13:19.026869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '849477078617'
down_revision = 'b3dd1f9c6aa9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number'),
    sa.UniqueConstraint('phone_number'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('phone_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phone_number',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('phone_number', sa.VARCHAR(length=15), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone_number')
    )
    op.drop_table('user')
    # ### end Alembic commands ###
