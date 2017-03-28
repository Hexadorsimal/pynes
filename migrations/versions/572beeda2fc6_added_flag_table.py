"""added flag table

Revision ID: 572beeda2fc6
Revises: 43580b3b983e
Create Date: 2017-03-27 20:22:52.046948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '572beeda2fc6'
down_revision = '43580b3b983e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('letter', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('mask', sa.Integer(), nullable=True),
    sa.Column('register_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['register_id'], ['register.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flag')
    # ### end Alembic commands ###
