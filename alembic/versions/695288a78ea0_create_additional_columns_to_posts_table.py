"""create additional columns to posts table

Revision ID: 695288a78ea0
Revises: d2f300a9b1ca
Create Date: 2022-03-06 12:36:05.812995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '695288a78ea0'
down_revision = 'd2f300a9b1ca'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
