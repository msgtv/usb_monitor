from typing import Optional

from app.schemas.base import SBaseModel
from app.departments.schemas import SDepartment


class SComputer(SBaseModel):
    name: str
    is_accepted_usb: bool
    department_id: Optional[int]


class SComputerDetailed(SBaseModel):
    name: str
    is_accepted_usb: bool
    department: Optional[SDepartment]
