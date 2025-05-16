from datetime import datetime
from typing import Optional

from app.schemas.base import SBaseModel


class STask(SBaseModel):
    action: str
    is_completed: bool
    sheduled_dt: Optional[datetime]
    computer_id: int
    usb_id: int
