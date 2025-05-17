from typing import List

from fastapi_pagination.ext.sqlalchemy import apaginate
from sqlalchemy import select

from app.dao.base import BaseDAO
from app.usbs.models import USB
from app.database import async_session_maker


class UsbDAO(BaseDAO):
    model = USB

    @classmethod
    def set_order_by(cls, query):
        return query.order_by(cls.model.name)
