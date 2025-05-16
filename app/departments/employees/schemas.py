from typing import Optional

from app.departments.schemas import SDepartment
from app.schemas.base import SBaseModel


class SEmployeeBase(SBaseModel):
    fullname: Optional[str]
    username: Optional[str]
    job_title: Optional[str]


class SEmployee(SEmployeeBase):
    department_id: Optional[int]


class SEmployeeDetail(SEmployeeBase):
    department: Optional[SDepartment]
