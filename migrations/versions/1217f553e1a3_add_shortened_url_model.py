"""Add Shortened URL Model

Revision ID: 1217f553e1a3
Revises:
Create Date: 2022-06-02 14:21:12.470584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1217f553e1a3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "shortened_url",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("url", sa.String(), nullable=True),
        sa.Column("shortcode", sa.String(), nullable=True),
        sa.Column("clicks", sa.Integer(), nullable=True),
        sa.Column("creation_date", sa.DateTime(), nullable=True),
        sa.Column("last_visit", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("shortened_url")
    # ### end Alembic commands ###
