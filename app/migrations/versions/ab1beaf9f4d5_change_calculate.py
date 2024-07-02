"""change calculate

Revision ID: ab1beaf9f4d5
Revises: 52db248f0b1f
Create Date: 2024-06-30 16:43:35.203651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab1beaf9f4d5'
down_revision: Union[str, None] = '52db248f0b1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookings', sa.Column('total_cost', sa.Integer(), sa.Computed('(date_to - date_from) * price', ), nullable=True))
    op.add_column('bookings', sa.Column('total_days', sa.Integer(), sa.Computed('date_to - date_from', ), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bookings', 'total_days')
    op.drop_column('bookings', 'total_cost')
    # ### end Alembic commands ###
