from datetime import datetime

from sqlalchemy import ForeignKey, and_, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base, int_pk, bool_default_false


ACTION_USB_ACCEPT = 'accept'
ACTION_USB_PROHIBIT = 'prohibit'


class Task(Base):
    action: Mapped[str]
    is_completed: Mapped[bool_default_false]

    sheduled_dt: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    computer_id: Mapped[int] = mapped_column(ForeignKey('computers.id'), nullable=False)
    computer = relationship("Computer", back_populates="tasks")

    usb_id: Mapped[int] = mapped_column(ForeignKey('usbs.id'), nullable=False)
    usb = relationship("USB", back_populates="tasks")

    def __str__(self):
        return f"Task #{self.id} ({self.action})"

    def __repr__(self):
        return f'Task(id={self.id}, action={self.action})'