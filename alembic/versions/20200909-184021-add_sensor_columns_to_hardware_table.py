"""add sensor columns to hardware table

Revision ID: 30e93b155660
Revises: 7a36ce5577d0
Create Date: 2020-09-09 18:40:21.330273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30e93b155660'
down_revision = '7a36ce5577d0'
branch_labels = None
depends_on = None


TABLE_NAME = 'hardware'


def upgrade():
    op.add_column(TABLE_NAME, sa.Column('cpu_load', sa.Float))
    op.add_column(TABLE_NAME, sa.Column('cpu_percent', sa.Float))
    op.add_column(TABLE_NAME, sa.Column('cpu_temperature', sa.Float))
    op.add_column(TABLE_NAME, sa.Column('disk_free_bytes', sa.BigInteger))
    op.add_column(TABLE_NAME, sa.Column('disk_total_bytes', sa.BigInteger))
    op.add_column(TABLE_NAME, sa.Column('disk_used_bytes', sa.BigInteger))
    op.add_column(TABLE_NAME, sa.Column('memory_available_bytes', sa.BigInteger))
    op.add_column(TABLE_NAME, sa.Column('memory_total_bytes', sa.BigInteger))
    op.add_column(TABLE_NAME, sa.Column('network_recv_bytes', sa.BigInteger))
    op.add_column(TABLE_NAME, sa.Column('network_sent_bytes', sa.BigInteger))


def downgrade():
    op.drop_column(TABLE_NAME, 'cpu_load')
    op.drop_column(TABLE_NAME, 'cpu_percent')
    op.drop_column(TABLE_NAME, 'cpu_temperature')
    op.drop_column(TABLE_NAME, 'disk_free_bytes')
    op.drop_column(TABLE_NAME, 'disk_total_bytes')
    op.drop_column(TABLE_NAME, 'disk_used_bytes')
    op.drop_column(TABLE_NAME, 'memory_available_bytes')
    op.drop_column(TABLE_NAME, 'memory_total_bytes')
    op.drop_column(TABLE_NAME, 'network_recv_bytes')
    op.drop_column(TABLE_NAME, 'network_sent_bytes')
