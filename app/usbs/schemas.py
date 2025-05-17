from typing import Optional

from app.schemas.base import SBaseModel
from app.departments.schemas import SDepartment


class SUsbBase(SBaseModel):
    name: str
    vendor: Optional[str]
    sn: Optional[str]
    vid: Optional[str]
    pid: Optional[str]
    class_type: Optional[int]
    is_accepted: bool

class SUsb(SUsbBase):
    department_id: Optional[int]


class SUsbDetail(SUsbBase):
    department: Optional[SDepartment]


class SUsbDetailedData(SUsbDetail):
    data: Optional[bytes]
