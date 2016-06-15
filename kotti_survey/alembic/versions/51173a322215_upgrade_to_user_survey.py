"""Upgrade to user survey.

Revision ID: 51173a322215
Revises:
Create Date: 2016-06-15 13:03:17.071246

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import (
    Column,
    Unicode,
    Integer,
    Boolean,
    String
)

# revision identifiers, used by Alembic.
revision = '51173a322215'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    try:
        with op.batch_alter_table("surveys") as batch_op:
            batch_op.add_column(Column("collect_user_info",
                                Boolean, default=False))
            batch_op.add_column(Column("redirect_url", String))
    except Exception as e:
        print e
        pass


def downgrade():
    try:
        with op.batch_alter_table("surveys") as batch_op:
            batch_op.drop_column('collect_user_info')
            batch_op.drop_column('redirect_url')
    except Exception as e:
        print e
        pass
