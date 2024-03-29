"""Add bio and profile solumns to table users

Revision ID: 556e51cad32e
Revises: b8f9d89a437e
Create Date: 2019-12-01 17:26:12.132109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '556e51cad32e'
down_revision = 'b8f9d89a437e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
