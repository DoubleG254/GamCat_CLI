"""Empty Init

Revision ID: 946dbce6a8a9
Revises: 193b8545c80c
Create Date: 2023-09-08 10:44:47.091623

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '946dbce6a8a9'
down_revision: Union[str, None] = '193b8545c80c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
