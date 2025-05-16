from datetime import datetime

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base, bool_default_false
from app.events.event_sources.models import EventSource


class Event(Base):
    event_id: Mapped[str]

    date: Mapped[datetime]
    is_closed: Mapped[bool_default_false]

    event_source_id: Mapped[int] = mapped_column(ForeignKey('eventsources.id', name='fk_event_event_source'),
                                              nullable=False)
    event_source = relationship(
        EventSource,
        back_populates="events",
    )

    usb_id: Mapped[int] = mapped_column(ForeignKey("usbs.id", name="fk_event_usb"), nullable=False)
    usb = relationship(
        "USB",
        back_populates="events",
    )

    computer_id: Mapped[int] = mapped_column(ForeignKey("computers.id"), nullable=False)
    computer = relationship(
        "Computer",
        back_populates="events",
    )

    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id", name="fk_event_employee"),
        nullable=True
    )
    employee = relationship(
        "Employee",
        back_populates="events",
    )

    __table_args__ = (
        UniqueConstraint('event_id', 'event_source_id', name='uix__event_id__source'),
    )

    def __str__(self):
        return f"SNS Event {self.event_id}"

    def __repr__(self):
        return f"{self.__class__.__name__}: {str(self)}"