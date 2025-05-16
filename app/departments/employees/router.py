from typing import List, Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination import Page

from app.departments.employees.dao import EmployeeDAO
from app.departments.employees.dependencies import EmployeesSearchArgsDepend
from app.departments.employees.schemas import SEmployee, SEmployeeDetail
from app.departments.employees.exceptions import EmployeeNotFound


router = APIRouter(
    prefix="/employees",
    tags=["Работники"],
)

@router.get('')
async def get_employees(
        args: Annotated[EmployeesSearchArgsDepend, Depends(EmployeesSearchArgsDepend)],
) -> Page[SEmployee]:
    params = {}
    if args.department_id:
        params["department_id"] = args.department_id
    if args.job_title:
        employees = await EmployeeDAO.get_all_by_job_title_paginated(args.job_title, **params)
    else:
        employees = await EmployeeDAO.get_all_paginated(**params)

    return employees


@router.get('/detailed')
async def get_employees_detailed(
    args: Annotated[EmployeesSearchArgsDepend, Depends(EmployeesSearchArgsDepend)],
) -> Page[SEmployeeDetail]:
    params = {}
    if args.department_id:
        params["department_id"] = args.department_id
    if args.job_title:
        employees = await EmployeeDAO.get_all_by_job_title_paginated_detailed(args.job_title, **params)
    else:
        employees = await EmployeeDAO.get_all_paginated_detailed(**params)

    return employees


@router.get('/{employee_id}')
async def get_employee(employee_id: int) -> SEmployeeDetail:
    employee = await EmployeeDAO.get_by_id_detailed(employee_id)
    if employee:
        return employee
    raise EmployeeNotFound(f'No employee with id {employee_id}')
