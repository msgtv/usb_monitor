from typing import List

from sqlalchemy import select

from app.dao.base import BaseDAO
from app.usbs.models import USB
from app.database import async_session_maker


class UsbDAO(BaseDAO):
    model = USB

    @classmethod
    async def get_usbs_by_class_type(cls, class_types: List[int], **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(**filter_by)
                .where(cls.model.class_type.in_(class_types))
                # TODO: remove limits
                .limit(100)
            )

            result = await session.execute(query)

            return result.scalars().all()
