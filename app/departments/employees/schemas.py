from typing import Optional

from app.schemas.base import SBaseModel


class SEmployee(SBaseModel):
    fullname: Optional[str]
    username: Optional[str]
    job_title: Optional[str]
    department_id: Optional[int]
