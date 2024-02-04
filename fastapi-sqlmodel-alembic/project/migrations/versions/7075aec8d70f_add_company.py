"""add company

Revision ID: 7075aec8d70f
Revises: 46f397038381
Create Date: 2024-01-30 16:32:52.310664

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel             # NEW


# revision identifiers, used by Alembic.
revision = '7075aec8d70f'
down_revision = '46f397038381'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_song_year', table_name='song')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_song_year', 'song', ['year'], unique=False)
    op.drop_table('company')
    # ### end Alembic commands ###
