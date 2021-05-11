"""empty message

Revision ID: 49d5463513e8
Revises: 89045d2294d2
Create Date: 2021-05-11 19:00:08.062643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49d5463513e8'
down_revision = '89045d2294d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('phone_numer', sa.Column('name', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('phone_numer', 'name')
    # ### end Alembic commands ###
