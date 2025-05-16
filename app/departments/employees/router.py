from typing import List

from fastapi import APIRouter
from fastapi_pagination import Page

from app.departments.employees.dao import EmployeeDAO
from app.departments.employees.schemas import SEmployee, SEmployeeDetailed
from app.departments.employees.exceptions import EmployeeNotFound


router = APIRouter(
    prefix="/employees",
    tags=["Работники"],
)

@router.get('')
async def get_employees() -> Page[SEmployee]:
    employees = await EmployeeDAO.get_all_paginated()

    return employees


@router.get('/detailed')
async def get_employee_detailed() -> Page[SEmployeeDetailed]:
    employees = await EmployeeDAO.get_all_paginated_detailed()

    return employees


@router.get('/{employee_id}')
async def get_employee(employee_id: int) -> SEmployeeDetailed:
    employee = await EmployeeDAO.get_by_id_detailed(employee_id)
    if employee:
        return employee
    raise EmployeeNotFound(f'No employee with id {employee_id}')
