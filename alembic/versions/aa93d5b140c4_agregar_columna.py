"""agregar columna

Revision ID: aa93d5b140c4
Revises: f5a389d77dcb
Create Date: 2025-05-17 18:29:22.705199

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa93d5b140c4'
down_revision: Union[str, None] = 'f5a389d77dcb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('pruebas', sa.Column('nueva_columna', sa.String(50)))
    op.add_column('pruebas', sa.Column('nueva_columna', sa.String(50)))
    pass

def downgrade():
    op.drop_column('pruebas', 'nueva_columna')
    pass
