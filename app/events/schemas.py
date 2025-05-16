from datetime import datetime
from typing import Optional

from app.schemas.base import SBaseModel


class SEvent(SBaseModel):
    date: datetime
    is_closed: bool
    event_source_id: int
    usb_id: int
    computer_id: int
    employee_id: Optional[int]
