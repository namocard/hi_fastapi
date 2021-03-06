"""Add timestamp mixin

Revision ID: 6ca631bd6060
Revises: e6a8e7cf7f6c
Create Date: 2021-02-03 17:30:19.090868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ca631bd6060'
down_revision = 'e6a8e7cf7f6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Grades', sa.Column('CreatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.add_column('Grades', sa.Column('UpdatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.add_column('Schools', sa.Column('CreatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.add_column('Schools', sa.Column('UpdatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.add_column('Students', sa.Column('CreatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.add_column('Students', sa.Column('UpdatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.add_column('Users', sa.Column('CreatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.add_column('Users', sa.Column('UpdatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'UpdatedAt')
    op.drop_column('Users', 'CreatedAt')
    op.drop_column('Students', 'UpdatedAt')
    op.drop_column('Students', 'CreatedAt')
    op.drop_column('Schools', 'UpdatedAt')
    op.drop_column('Schools', 'CreatedAt')
    op.drop_column('Grades', 'UpdatedAt')
    op.drop_column('Grades', 'CreatedAt')
    # ### end Alembic commands ###
