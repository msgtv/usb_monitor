from datetime import datetime
from typing import Optional

from app.schemas.base import SBaseModel
from app.computers.schemas import SComputerDetail
from app.usbs.schemas import SUsbDetail


class STaskBase(SBaseModel):
    action: str
    is_completed: bool
    sheduled_dt: Optional[datetime]
    computer_id: int
    usb_id: int


class STask(STaskBase):
    computer_id: int
    usb_id: int


class STaskDetail(STaskBase):
    computer: Optional[SComputerDetail]
    usb: Optional[SUsbDetail]
