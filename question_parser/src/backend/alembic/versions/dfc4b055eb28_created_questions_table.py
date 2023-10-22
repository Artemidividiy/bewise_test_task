"""created questions table

Revision ID: dfc4b055eb28
Revises: 7ac7ca7da9e9
Create Date: 2023-10-22 19:42:10.811413

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfc4b055eb28'
down_revision: Union[str, None] = '7ac7ca7da9e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
