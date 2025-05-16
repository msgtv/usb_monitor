from fastapi_pagination.ext.sqlalchemy import apaginate
from sqlalchemy.orm import joinedload

from app.computers.models import Computer
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.departments.employees.models import Employee
from app.events.models import Event


class EventDAO(BaseDAO):
    model = Event

    @classmethod
    async def get_all_paginated_detailed(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                cls.get_select_query(**filter_by)
                .options(
                    joinedload(cls.model.usb),
                    joinedload(cls.model.computer).joinedload(Computer.department),
                    joinedload(cls.model.employee).joinedload(Employee.department),
                )
            )

            result = await apaginate(session, query)

            return result


