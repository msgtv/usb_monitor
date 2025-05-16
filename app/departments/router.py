from typing import List

from fastapi import APIRouter
from fastapi_pagination import Page

from app.departments.dao import DepartmentDAO
from app.departments.schemas import SDepartment
from app.departments.exceptions import DepartmentNotFound

router = APIRouter(
    prefix="/departments",
    tags=["Подразделения"],
)

@router.get('')
async def get_departments() -> Page[SDepartment]:
    departments = await DepartmentDAO.get_all_paginated()

    return departments

@router.get('/{department_id}')
async def get_department_by_id(department_id: int) -> SDepartment:
    department = await DepartmentDAO.get_by_id(department_id)

    if department:
        return department

    raise DepartmentNotFound(f'No department with id {department_id}')
