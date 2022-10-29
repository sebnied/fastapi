"""add content column to posts table

Revision ID: b72c85a1acf7
Revises: 502ad651e815
Create Date: 2022-10-27 20:56:04.939933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b72c85a1acf7'
down_revision = '502ad651e815'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
