from fastapi_pagination.ext.sqlalchemy import apaginate
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.computers.models import Computer
from app.database import async_session_maker


class ComputerDAO(BaseDAO):
    model = Computer

    @classmethod
    async def get_all_paginated_detailed(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(**filter_by)
                .where(cls.model.is_deleted.is_(False))
                .options(
                    joinedload(cls.model.department)
                )
            )

            result = await apaginate(session, query)

            return result

    @classmethod
    async def get_by_id_detail(cls, model_id):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(id=model_id)
                .where(cls.model.is_deleted.is_(False))
                .options(
                    joinedload(cls.model.department)
                )
            )
            result = await session.execute(query)
            return result.scalars().one_or_none()
