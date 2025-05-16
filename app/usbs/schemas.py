from typing import Optional

from app.schemas.base import SBaseModel


class SUsb(SBaseModel):
    name: str
    vendor: Optional[str]
    sn: Optional[str]
    vid: Optional[str]
    pid: Optional[str]
    class_type: Optional[int]
    data: Optional[bytes]
    is_accepted: bool

    department_id: Optional[int]
