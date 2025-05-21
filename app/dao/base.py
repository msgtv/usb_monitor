from typing import List

from sqlalchemy import select, insert, and_, BinaryExpression, update
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_pagination.ext.sqlalchemy import apaginate


class BaseDAO:
    model = None

    @classmethod
    def get_select_query(cls, filters: List[BinaryExpression] = None):
        query = select(cls.model)
        query = cls.set_filters(query, filters)
        # query = cls.get_base_select_query(**filter_by)
        query = cls.set_where(query)
        query = cls.set_options(query)
        query = cls.set_order_by(query)

        return query

    @classmethod
    def set_filters(cls, query, filters: List[BinaryExpression] = None):
        if filters:
            for condition in filters:
                query = query.where(condition)

        return query

    @classmethod
    def get_base_select_query(cls, **filter_by):
        return (
            select(cls.model)
            .filter_by(**filter_by)
        )

    @classmethod
    def set_where(cls, query):
        return query.where(cls.model.is_deleted.is_(False))

    @classmethod
    def set_options(cls, query):
        return query

    @classmethod
    def set_order_by(cls, query):
        return query.order_by(cls.model.id.desc())

    @classmethod
    async def get_by_id(cls, session: AsyncSession, obj_id):
        query = cls.get_select_query([cls.model.id == obj_id])
        result = await session.execute(query)
        return result.scalars().one_or_none()

    @classmethod
    async def get_one_or_none(cls, session: AsyncSession, filters: List[BinaryExpression] = None):
        query = cls.get_select_query(filters)
        result = await session.execute(query)

        return result.scalars().one_or_none()

    @classmethod
    async def get_all(cls, session: AsyncSession, filters: List[BinaryExpression] = None):
        query = cls.get_select_query(filters)
        result = await session.execute(query)

        return result

    @classmethod
    async def get_all_paginated(cls, session: AsyncSession, filters: List[BinaryExpression] = None):
        query = cls.get_select_query(filters)

        result = await apaginate(session, query)

        return result

    @classmethod
    async def add(cls, session: AsyncSession, **data):
        query = insert(cls.model).values(**data).returning(cls.model)
        result = await session.execute(query)
        await session.flush()
        return result.scalars().one_or_none()

    @classmethod
    async def update(cls, session: AsyncSession, obj_id, **data):
        query = (
            update(cls.model)
            .values(**data)
            .where(cls.model.id == obj_id)
            .returning(cls.model)
        )

        res = await session.execute(query)
        await session.flush()

        return res.scalars().one_or_none()
