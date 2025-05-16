from typing import Optional

from app.schemas.base import SBaseModel


class SComputer(SBaseModel):
    name: str
    is_accepted_usb: bool
    department_id: Optional[int]
