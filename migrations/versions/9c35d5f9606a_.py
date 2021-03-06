"""empty message

Revision ID: 9c35d5f9606a
Revises: 
Create Date: 2017-11-16 18:41:34.193000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9c35d5f9606a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('telephone', sa.String(length=12), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('student')
    op.drop_table('ticket')
    op.drop_table('practice')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('practice',
    sa.Column('class', mysql.VARCHAR(length=12), nullable=True),
    sa.Column('teacher', mysql.VARCHAR(length=12), nullable=True),
    sa.Column('qq', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('qq'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('ticket',
    sa.Column('id', mysql.VARCHAR(length=30), nullable=True),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('student',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('class', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('age', mysql.VARCHAR(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('user')
    # ### end Alembic commands ###
