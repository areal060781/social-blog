"""empty message

Revision ID: 915a10b64d43
Revises: 37471f45461d
Create Date: 2020-06-25 10:11:26.117048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '915a10b64d43'
down_revision = '37471f45461d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
