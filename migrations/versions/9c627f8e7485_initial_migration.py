"""Initial migration.

Revision ID: 9c627f8e7485
Revises:
Create Date: 2022-06-02 16:36:26.217830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9c627f8e7485"
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
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_shortened_url_shortcode"),
        "shortened_url",
        ["shortcode"],
        unique=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_shortened_url_shortcode"), table_name="shortened_url"
    )
    op.drop_table("shortened_url")
    # ### end Alembic commands ###