"""Add table comments

Revision ID: 7649015ecfdb
Revises: 9da86cf7507b
Create Date: 2019-11-29 16:01:20.552849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7649015ecfdb'
down_revision = '9da86cf7507b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('user', sa.String(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
