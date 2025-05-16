from fastapi_pagination.ext.sqlalchemy import apaginate
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.computers.models import Computer
from app.database import async_session_maker


class ComputerDAO(BaseDAO):
    model = Computer

    @classmethod
    async def get_all_detailed_paginated(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(**filter_by)
                .where(cls.model.is_deleted.is_(False))
                .options(
                    joinedload(cls.model.department)
                )
            )

            print(query.compile(compile_kwargs={"literal_binds": True}))

            result = await apaginate(session, query)

            return result
