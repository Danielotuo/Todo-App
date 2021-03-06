"""empty message

Revision ID: 0faed16b6064
Revises: 073034b9088b
Create Date: 2020-05-25 15:47:25.511289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0faed16b6064'
down_revision = '073034b9088b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
