"""create hardware table

Revision ID: 7a36ce5577d0
Revises:
Create Date: 2020-09-08 18:24:03.271813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a36ce5577d0'
down_revision = None
branch_labels = None
depends_on = None


TABLE_NAME = 'hardware'
INDEX_NAME = 'index_created_at'


def upgrade():
    op.create_table(
        TABLE_NAME,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime, nullable=False)
    )
    op.create_index(INDEX_NAME, TABLE_NAME, ['created_at'], unique=True)


def downgrade():
    op.drop_index(INDEX_NAME, TABLE_NAME)
    op.drop_table(TABLE_NAME)
