from sqlalchemy import select, insert, and_

from app.database import async_session_maker
from fastapi_pagination.ext.sqlalchemy import apaginate


class BaseDAO:
    model = None

    @classmethod
    def get_select_query(cls, **filter_by):
        return (
            select(cls.model)
            .filter_by(**filter_by)
        )

    @classmethod
    async def get_by_id(cls, model_id):
        async with async_session_maker() as session:
            query = (
                cls.get_select_query(id=model_id)
                .where(cls.model.is_deleted.is_(False))
            )
            result = await session.execute(query)
            return result.scalars().one_or_none()

    @classmethod
    async def get_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                cls.get_select_query(**filter_by)
                .where(cls.model.is_deleted.is_(False))
            )
            result = await session.execute(query)

            return result.scalars().one_or_none()

    @classmethod
    async def get_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                cls.get_select_query(**filter_by)
                .where(cls.model.is_deleted.is_(False))
            )
            result = await session.execute(query)

            return result

    @classmethod
    async def get_all_paginated(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                cls.get_select_query(**filter_by)
                .where(cls.model.is_deleted.is_(False))
            )

            result = await apaginate(session, query)

            return result

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model.id)
            await session.execute(query)
            await session.commit()
