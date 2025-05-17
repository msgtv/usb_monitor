from typing import List, Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination import Page

from app.departments.employees.dao import EmployeeDAO, EmployeeDAODetailed
from app.departments.employees.dependencies import EmployeesSearchArgsDepend
from app.departments.employees.schemas import SEmployee, SEmployeeDetail
from app.departments.employees.exceptions import EmployeeNotFound
from app.departments.employees.models import Employee

router = APIRouter(
    prefix="/employees",
    tags=["Работники"],
)

@router.get('')
async def get_employees(
        args: Annotated[EmployeesSearchArgsDepend, Depends(EmployeesSearchArgsDepend)],
) -> Page[SEmployee]:
    return await EmployeeDAO.get_all_paginated(args.filters)


@router.get('/detailed')
async def get_employees_detailed(
    args: Annotated[EmployeesSearchArgsDepend, Depends(EmployeesSearchArgsDepend)],
) -> Page[SEmployeeDetail]:
    return await EmployeeDAODetailed.get_all_paginated(args.filters)


@router.get('/{employee_id}')
async def get_employee(employee_id: int) -> SEmployeeDetail:
    employee = await EmployeeDAODetailed.get_by_id(employee_id)
    if employee:
        return employee
    raise EmployeeNotFound(f'No employee with id {employee_id}')
