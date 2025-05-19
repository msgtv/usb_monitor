from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.usbs.models import USB
from app.database import async_session_maker


class UsbDAO(BaseDAO):
    model = USB

    @classmethod
    def set_order_by(cls, query):
        return query.order_by(cls.model.name)

    @classmethod
    async def update(cls, usb_id, **values):
        async with async_session_maker() as session:
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
