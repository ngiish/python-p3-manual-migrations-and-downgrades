"""Renaming enrolled_date column to date_enrolled column

Revision ID: 66d576cc7e22
Revises: 35ab16c4fd2c
Create Date: 2023-12-08 15:37:26.674345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66d576cc7e22'
down_revision = '35ab16c4fd2c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_column('enrolled_date', 'date_enrolled')


def downgrade() -> None:
    op.rename_column('date_enrolled', 'enrolled_date')
