from typing import List

from sqlalchemy.orm import Mapped, relationship

from app.database import Base, int_null_true, str_null_true


class Department(Base):
    name: Mapped[str]
    number: Mapped[int_null_true]
    dep_type: Mapped[str_null_true]

    employees: Mapped[List["Employee"]] = relationship(
        "Employee",
        back_populates="department",
        uselist=True,
    )
    usbs: Mapped["USB"] = relationship(
        "USB",
        back_populates="department",
        uselist=True,
    )
    employees: Mapped["Employee"] = relationship(
        "Employee",
        back_populates="department",
        uselist=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {str(self)}"
