"""initial version

Revision ID: 08f340faf9cf
Revises: 
Create Date: 2017-03-26 12:41:17.599994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08f340faf9cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instruction',
    sa.Column('opcode', sa.Integer(), nullable=False),
    sa.Column('addressing_mode', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('opcode')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instruction')
    # ### end Alembic commands ###
