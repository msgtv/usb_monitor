from typing import List

from sqlalchemy import ForeignKey, Boolean, Table, Column, LargeBinary
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base, str_null_true, int_null_true


class USB(Base):
    name: Mapped[str]
    vendor: Mapped[str_null_true]
    sn: Mapped[str_null_true]
    vid: Mapped[str_null_true]
    pid: Mapped[str_null_true]
    class_type: Mapped[int_null_true]
    data: Mapped[bytes] = mapped_column(LargeBinary, nullable=True)
    is_accepted: Mapped[bool] = mapped_column(Boolean, default=False)

    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"), nullable=True)
    department: Mapped["Department"] = relationship(
        "Department",
        back_populates="usbs",
    )

    events: Mapped[List["Event"]] = relationship(
        "Event",
        back_populates="usb",
        uselist=True,
    )

    tasks: Mapped[List["Task"]] = relationship(
        "Task",
        back_populates="usb",
        uselist=True,
    )

    computers: Mapped[List["Computer"]] = relationship(
        "Computer",
        secondary="usb_accepted_on_computers",
        back_populates="usbs",
        uselist = True
    )


usb_accepted_on_computers = Table(
    "usb_accepted_on_computers",
    Base.metadata,
    Column("usb_id", ForeignKey("usbs.id")),
    Column("computer_id", ForeignKey("computers.id")),
)
