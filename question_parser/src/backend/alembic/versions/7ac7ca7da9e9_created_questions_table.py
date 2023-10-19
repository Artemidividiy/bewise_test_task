"""created questions table

Revision ID: 7ac7ca7da9e9
Revises: a6a2bf9fbd09
Create Date: 2023-10-19 22:49:57.248900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ac7ca7da9e9'
down_revision: Union[str, None] = 'a6a2bf9fbd09'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
