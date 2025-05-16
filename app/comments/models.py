from sqlalchemy import Unicode, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import generic_relationship

from app.database import Base


class Comment(Base):
    object_type: Mapped[str] = mapped_column(Unicode(255))
    object_id: Mapped[int] = mapped_column(Integer)
    object = generic_relationship(object_type, object_id)
    user: Mapped[str]

    text: Mapped[str]
