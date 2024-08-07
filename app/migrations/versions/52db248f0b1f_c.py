"""c

Revision ID: 52db248f0b1f
Revises: 55b59dbd8c05
Create Date: 2024-06-30 16:42:06.089672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52db248f0b1f'
down_revision: Union[str, None] = '55b59dbd8c05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bookings', 'total_days')
    op.drop_column('bookings', 'total_cost')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookings', sa.Column('total_cost', sa.INTEGER(), sa.Computed('((date_from - date_to) * price)', persisted=True), autoincrement=False, nullable=True))
    op.add_column('bookings', sa.Column('total_days', sa.INTEGER(), sa.Computed('(date_from - date_to)', persisted=True), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
