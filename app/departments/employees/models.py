from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base, str_null_true


class Employee(Base):
    fullname: Mapped[str_null_true]
    username: Mapped[str_null_true]
    job_title: Mapped[str_null_true]

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id", name="fk_user_deparment"),
        nullable=True
    )

    department: Mapped["Department"] = relationship("Department", back_populates="employees")
    events: Mapped[List["Event"]] = relationship("Event", back_populates="employee")

    def __str__(self) -> str:
        return f"{self.fullname} ({self.username})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, fullname={self.fullname})"
