"""principals

Revision ID: 52a401750a76
Revises: 2087a1db8595
Create Date: 2024-01-07 19:15:22.771993

"""

from alembic import op
import sqlalchemy as sa

from core import db
from core.models.users import User
from core.models.principals import Principal


# revision identifiers, used by Alembic.
revision = "52a401750a76"
down_revision = "2087a1db8595"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "principals",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    principal_user = User(email="principal@fylebe.com", username="principal")
    db.session.add(principal_user)

    principal = Principal(user_id=User.get_by_email("principal@fylebe.com").id)

    db.session.add(principal)
    db.session.commit()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("principals")
    # ### end Alembic commands ###
