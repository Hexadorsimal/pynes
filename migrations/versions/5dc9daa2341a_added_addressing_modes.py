"""Added addressing modes

Revision ID: 5dc9daa2341a
Revises: a9d75d93abaf
Create Date: 2017-03-26 12:51:30.078153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dc9daa2341a'
down_revision = 'a9d75d93abaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addressing_mode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('addressing_mode')
    # ### end Alembic commands ###