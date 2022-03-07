"""create post table

Revision ID: 6935d5a2e0fc
Revises: 
Create Date: 2022-03-06 11:30:07.918846

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6935d5a2e0fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
