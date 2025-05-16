from typing import List

from fastapi import APIRouter
from fastapi_pagination import Page

from app.departments.employees.dao import EmployeeDAO
from app.departments.employees.schemas import SEmployee

router = APIRouter(
    prefix="/employees",
    tags=["Работники"],
)

@router.get('')
async def get_employees() -> Page[SEmployee]:
    employees = await EmployeeDAO.get_all_paginated()

    return employees
