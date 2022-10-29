"""add last few columns to posts table

Revision ID: 89cbcc779150
Revises: 49453b05b8a5
Create Date: 2022-10-27 21:12:32.643225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89cbcc779150'
down_revision = '49453b05b8a5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts",
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"),
                            nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
