from typing import List

from fastapi import APIRouter

from app.departments.employees.dao import EmployeeDAO
from app.departments.employees.schemas import SEmployee

router = APIRouter(
    prefix="/employees",
    tags=["Работники"],
)

@router.get('')
async def get_employees() -> List[SEmployee]:
    employees = await EmployeeDAO.get_all()

    return employees
