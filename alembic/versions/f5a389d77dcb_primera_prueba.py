"""primera prueba 

Revision ID: f5a389d77dcb
Revises: 
Create Date: 2025-05-17 15:14:13.596649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5a389d77dcb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.create_table(
        'pruebas',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String(50))
    )


def downgrade():
    op.drop_table('pruebas')
