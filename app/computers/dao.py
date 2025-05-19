from fastapi_pagination.ext.sqlalchemy import apaginate
from sqlalchemy import select, update
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.computers.models import Computer
from app.database import async_session_maker


class ComputerDAO(BaseDAO):
    model = Computer

    @classmethod
    def set_order_by(cls, query):
        return query.order_by(cls.model.name)

    @classmethod
    async def update(cls, computer_id, **values):
        async with async_session_maker() as session:
            query = (
                update(cls.model)
                .values(**values)
                .where(cls.model.id == computer_id)
                .returning(cls.model)
            )

            res = await session.execute(query)
            await session.commit()

            return res.scalars().one_or_none()


class ComputerDAODetailed(ComputerDAO):
    @classmethod
    def set_options(cls, query):
        return query.options(joinedload(cls.model.department))

