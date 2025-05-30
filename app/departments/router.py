from typing import Annotated

from fastapi import APIRouter, Path
from fastapi_pagination import Page
from fastapi import Depends

from app.dependencies import SessionDepend
from app.departments.dao import DepartmentDAO
from app.departments.schemas import SDepartment
from app.departments.exceptions import DepartmentNotFound
from app.auth.dependencies import DefaultUser, ManagerUser, AdminUser, RootUser

router = APIRouter(
    prefix="/departments",
    tags=["Подразделения"],
)

@router.get('', dependencies=[Depends(DefaultUser)])
async def get_departments(
        session: SessionDepend,
) -> Page[SDepartment]:
    departments = await DepartmentDAO.get_all_paginated(session=session)
    return departments

@router.get('/{department_id}', dependencies=[Depends(DefaultUser)])
async def get_department_by_id(
        department_id: Annotated[int, Path(ge=1)],
        session: SessionDepend,
) -> SDepartment:
    department = await DepartmentDAO.get_by_id(session=session, obj_id=department_id)

    if department:
        return department

    raise DepartmentNotFound(f'No department with id {department_id}')
