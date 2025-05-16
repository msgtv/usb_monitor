from typing import Optional

from app.schemas.base import SBaseModel
from app.departments.schemas import SDepartment


class SComputerBase(SBaseModel):
    name: str
    is_accepted_usb: bool


class SComputer(SComputerBase):
    department_id: Optional[int]


class SComputerDetail(SComputerBase):
    department: Optional[SDepartment]
