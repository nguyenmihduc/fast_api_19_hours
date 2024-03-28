"""add content column

Revision ID: 7eb23d6311ee
Revises: cb3188a607e5
Create Date: 2024-03-27 19:18:05.283994

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7eb23d6311ee"
down_revision: Union[str, None] = "cb3188a607e5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
