"""Add table blogs

Revision ID: 9da86cf7507b
Revises: 743ed1568459
Create Date: 2019-11-29 14:37:30.626934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9da86cf7507b'
down_revision = '743ed1568459'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('blog', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('user', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogs')
    # ### end Alembic commands ###
