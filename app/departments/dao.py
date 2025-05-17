from app.dao.base import BaseDAO
from app.departments.models import Department


class DepartmentDAO(BaseDAO):
    model = Department

    @classmethod
    def set_order_by(cls, query):
        return query.order_by(cls.model.number)
