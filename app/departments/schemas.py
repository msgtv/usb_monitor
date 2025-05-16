from typing import Optional

from app.schemas.base import SBaseModel


class SDepartment(SBaseModel):
    name: str
    number: Optional[int]
    dep_type: Optional[str]
