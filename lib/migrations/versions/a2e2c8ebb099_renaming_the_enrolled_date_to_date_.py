"""Renaming the enrolled_date to date_enrolled

Revision ID: a2e2c8ebb099
Revises: 66d576cc7e22
Create Date: 2023-12-08 15:45:07.378533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2e2c8ebb099'
down_revision = '66d576cc7e22'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('enrolled_date', 'date_enrolled')


def downgrade() -> None:
    op.alter_column('date_enrolled', 'enrolled_date')
