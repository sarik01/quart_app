"""add se

Revision ID: 8fd83b823eb5
Revises: 161b5ce3d361
Create Date: 2023-03-22 15:02:46.609046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fd83b823eb5'
down_revision = '161b5ce3d361'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('se', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'se')
    # ### end Alembic commands ###
