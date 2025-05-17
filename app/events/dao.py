from sqlalchemy.orm import joinedload

from app.computers.models import Computer
from app.dao.base import BaseDAO
from app.usbs.models import USB
from app.departments.employees.models import Employee
from app.events.models import Event


class EventDAO(BaseDAO):
    model = Event

    @classmethod
    def set_order_by(cls, query):
        return query.order_by(cls.model.date.desc())


class EventDAODetailed(EventDAO):
    @classmethod
    def set_options(cls, query):
        query = query.options(
            joinedload(cls.model.usb).load_only(
                USB.id,
                USB.created_at,
                USB.updated_at,
                USB.name,
                USB.vendor,
                USB.sn,
                USB.vid,
                USB.pid,
                USB.class_type,
                USB.is_accepted,
            ).joinedload(USB.department),
            joinedload(cls.model.computer).joinedload(Computer.department),
            joinedload(cls.model.employee).joinedload(Employee.department),
        )

        return query

