"""Renaming students to scholars

Revision ID: 4e05c843563f
Revises: 791279dd0760
Create Date: 2025-08-20 12:33:00.113857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e05c843563f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')