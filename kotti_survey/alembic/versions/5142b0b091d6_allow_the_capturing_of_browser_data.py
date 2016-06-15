"""Allow the capturing of browser data.

Revision ID: 5142b0b091d6
Revises: 51173a322215
Create Date: 2016-06-15 14:49:17.670204

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
from sqlalchemy.dialects.postgresql import JSON

# revision identifiers, used by Alembic.
revision = '5142b0b091d6'
down_revision = '51173a322215'
branch_labels = None
depends_on = None


def upgrade():
    try:
        with op.batch_alter_table("surveys") as batch_op:
            batch_op.add_column(Column("browser_data", JSON))
        with op.batch_alter_table("surveys") as batch_op:
            batch_op.add_column(Column("survey_id",
                                ForeignKey('surveys.id'), primary_key=True))
    except Exception as e:
        print e
        pass


def downgrade():
    try:
        with op.batch_alter_table("surveys") as batch_op:
            batch_op.drop_column('browser_data')
        with op.batch_alter_table("survey_answers") as batch_op:
            batch_op.drop_column('survey_id')
    except Exception as e:
        print e
        pass
