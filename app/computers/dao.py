from fastapi_pagination.ext.sqlalchemy import apaginate
from sqlalchemy import select, update
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.computers.models import Computer


class ComputerDAO(BaseDAO):
    model = Computer

    @classmethod
    def set_order_by(cls, query):
        return query.order_by(cls.model.name)


class ComputerDAODetailed(ComputerDAO):
    @classmethod
    def set_options(cls, query):
        return query.options(joinedload(cls.model.department))

