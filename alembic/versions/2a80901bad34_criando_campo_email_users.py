"""criando campo email users

Revision ID: 2a80901bad34
Revises: 106e7e5a9ae9
Create Date: 2023-12-02 15:51:50.857595

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a80901bad34'
down_revision: Union[str, None] = '106e7e5a9ae9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
