from datetime import datetime
from typing import Optional

from app.schemas.base import SBaseModel
from app.usbs.schemas import SUsbDetail
from app.computers.schemas import SComputerDetail
from app.departments.employees.schemas import SEmployeeDetail


class SEventBase(SBaseModel):
    date: datetime
    is_closed: bool
    event_source_id: int


class SEvent(SEventBase):
    usb_id: int
    computer_id: int
    employee_id: Optional[int]


class SEventDetail(SEventBase):
    usb: Optional[SUsbDetail]
    computer: Optional[SComputerDetail]
    employee: Optional[SEmployeeDetail]