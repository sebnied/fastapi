"""create vote type column

Revision ID: 62bfca43ad50
Revises: b1d9d8e1b3d7
Create Date: 2022-11-06 21:58:40.220128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62bfca43ad50'
down_revision = 'b1d9d8e1b3d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('votes', sa.Column('vote_type', sa.String(), server_default='like', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('votes', 'vote_type')
    # ### end Alembic commands ###