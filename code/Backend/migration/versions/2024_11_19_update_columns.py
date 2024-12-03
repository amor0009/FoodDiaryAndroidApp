"""Update columns

Revision ID: 454767d4e8d7
Revises: 2024_11_06_date
Create Date: 2024-11-19 04:43:36.026759

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2024_11_19_update_columns'
down_revision: Union[str, None] = '2024_11_06_date'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_meal_name', table_name='meal')
    op.create_index(op.f('ix_meal_name'), 'meal', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_meal_name'), table_name='meal')
    op.create_index('ix_meal_name', 'meal', ['name'], unique=True)
    # ### end Alembic commands ###
