from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base, int_pk, bool_default_false


class Computer(Base):
    name: Mapped[str]
    is_accepted_usb: Mapped[bool_default_false]

    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"), nullable=True)
    department = relationship(
        "Department",
        back_populates="computers",
    )

    events: Mapped[List["Event"]] = relationship(
        "Event",
        back_populates="computer",
        uselist=True,
    )

    tasks: Mapped[List["Task"]] = relationship(
        "Task",
        back_populates="computer",
        uselist=True,
    )

    usbs: Mapped[List["USB"]] = relationship(
        "USB",
        secondary="usb_accepted_on_computers",
        back_populates="computers",
        uselist=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name})"
