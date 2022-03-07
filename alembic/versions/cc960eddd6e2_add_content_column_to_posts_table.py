"""add content column to posts table

Revision ID: cc960eddd6e2
Revises: 6935d5a2e0fc
Create Date: 2022-03-06 11:58:10.716987

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cc960eddd6e2'
down_revision = '6935d5a2e0fc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
