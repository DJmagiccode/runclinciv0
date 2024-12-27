"""Add user_id to Patient model

Revision ID: d4d68db0d9e5
Revises: 42e84d0d6ddf
Create Date: 2024-12-28 02:33:35.486169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4d68db0d9e5'
down_revision = '42e84d0d6ddf'
branch_labels = None
depends_on = None

def upgrade():
    # Drop the temporary table if it exists
    op.execute('DROP TABLE IF EXISTS _alembic_tmp_patient')

    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False, server_default='1'))  # Set a default value
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('contact',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=20),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('emergency_contact',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=20),
               existing_nullable=False)
        batch_op.alter_column('photo',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.create_unique_constraint('uq_patient_contact', ['contact'])
        batch_op.create_foreign_key('fk_patient_user', 'user', ['user_id'], ['id'])

    # Remove the default value after the column is populated
    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.alter_column('user_id', server_default=None)

    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('photo',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)
        batch_op.alter_column('emergency_contact',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=150),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=150),
               existing_nullable=False)
        batch_op.alter_column('contact',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=150),
               existing_nullable=False)
        batch_op.alter_column('address',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=150),
               existing_nullable=False)
        batch_op.alter_column('last_name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=150),
               existing_nullable=False)
        batch_op.alter_column('first_name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=150),
               existing_nullable=False)
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
