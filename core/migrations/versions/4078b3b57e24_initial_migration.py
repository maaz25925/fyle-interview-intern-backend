"""Initial migration.

Revision ID: 4078b3b57e24
Revises:
Create Date: 2021-09-16 08:05:36.381863

"""

from alembic import op
import sqlalchemy as sa

from core import db
from core.models.users import User

# revision identifiers, used by Alembic.
revision = "4078b3b57e24"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=80), nullable=False),
        sa.Column("email", sa.String(length=120), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )

    student_user_1 = User(email="student1@fylebe.com", username="student1")
    student_user_2 = User(email="student2@fylebe.com", username="student2")
    teacher_user_1 = User(email="teacher1@fylebe.com", username="teacher1")
    teacher_user_2 = User(email="teacher2@fylebe.com", username="teacher2")

    db.session.add(student_user_1)
    db.session.add(student_user_2)
    db.session.add(teacher_user_1)
    db.session.add(teacher_user_2)
    db.session.commit()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
