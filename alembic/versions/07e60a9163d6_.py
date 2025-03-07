"""empty message

Revision ID: 07e60a9163d6
Revises: f52e2d816518
Create Date: 2024-03-26 16:05:09.593869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07e60a9163d6'
down_revision: Union[str, None] = 'f52e2d816518'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Voting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Leader', sa.String(), nullable=False),
    sa.Column('Name_of_Voter', sa.String(), nullable=False),
    sa.Column('Reason', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Voting')
    # ### end Alembic commands ###
