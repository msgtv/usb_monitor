from fastapi_pagination.ext.sqlalchemy import apaginate
from sqlalchemy import select, and_
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.departments.employees.models import Employee


class EmployeeDAO(BaseDAO):
    model = Employee

    @classmethod
    def set_order_by(cls, query):
        return query.order_by(cls.model.fullname)


class EmployeeDAODetailed(EmployeeDAO):
    @classmethod
    def set_options(cls, query):
        return query.options(joinedload(cls.model.department))
