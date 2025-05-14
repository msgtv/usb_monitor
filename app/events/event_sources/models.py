from typing import List

from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class EventSource(Base):
    data_source_name: Mapped[str]
    name: Mapped[str]
    db_type: Mapped[str] = mapped_column(String(20))
    driver: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String(250))
    password: Mapped[str] = mapped_column(String(250))
    host: Mapped[str] = mapped_column(String(250))
    port: Mapped[int]
    database_name: Mapped[str] = mapped_column(String(100))
    additional_params: Mapped[JSON] = mapped_column(JSON, nullable=True)

    events: Mapped[List["Event"]] = relationship(
        "Event",
        back_populates="event_source",
        uselist=True,
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id} name={self.name})"
