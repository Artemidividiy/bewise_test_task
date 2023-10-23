"""added utility info

Revision ID: 8c4a53899aeb
Revises: df64ad221b1b
Create Date: 2023-10-23 14:51:35.042330

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8c4a53899aeb'
down_revision: Union[str, None] = 'df64ad221b1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_questions_id', table_name='questions')
    op.drop_table('questions')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('question_text', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('answer_text', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('question_created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='questions_pkey'),
    sa.UniqueConstraint('answer_text', name='questions_answer_text_key'),
    sa.UniqueConstraint('question_created_at', name='questions_question_created_at_key'),
    sa.UniqueConstraint('question_text', name='questions_question_text_key')
    )
    op.create_index('ix_questions_id', 'questions', ['id'], unique=False)
    # ### end Alembic commands ###