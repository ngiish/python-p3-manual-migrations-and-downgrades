"""Renaming students to scholars

Revision ID: 35ab16c4fd2c
Revises: 791279dd0760
Create Date: 2023-12-08 15:24:06.430718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35ab16c4fd2c'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
