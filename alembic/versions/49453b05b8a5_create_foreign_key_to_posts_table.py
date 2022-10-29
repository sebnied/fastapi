"""create foreign key to posts table

Revision ID: 49453b05b8a5
Revises: fbe153e5983e
Create Date: 2022-10-27 21:07:56.329469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49453b05b8a5'
down_revision = 'fbe153e5983e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fkey', source_table='posts',
                          referent_table='users', local_cols=['owner_id'],
                          remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fkey', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
