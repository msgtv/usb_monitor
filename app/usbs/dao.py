from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.usbs.models import USB


class UsbDAO(BaseDAO):
    model = USB

    @classmethod
    def set_order_by(cls, query):
        return query.order_by(cls.model.name)

    @classmethod
    async def update(cls, session: AsyncSession, usb_id: int, **values):
        query = (
            update(cls.model)
            .values(**values)
            .where(cls.model.id == usb_id)
            .returning(cls.model)
        )

        try:
            res = await session.execute(query)

            await session.commit()

            return res.scalars().one_or_none()
        except IntegrityError:
            return None


class UsbDetailedDAO(UsbDAO):
    @classmethod
    def set_order_by(cls, query):
        return query.options(
            joinedload(cls.model.department)
        )
