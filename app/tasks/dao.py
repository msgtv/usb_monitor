from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.tasks.models import Task
from app.computers.models import Computer
from app.usbs.models import USB


class TaskDAO(BaseDAO):
    model = Task

    @classmethod
    def set_order_by(cls, query):
        return query.order_by(cls.model.created_at.desc())


class TaskDAODetailed(TaskDAO):
    @classmethod
    def set_options(cls, query):
        return query.options(
            joinedload(cls.model.computer).joinedload(Computer.department),
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
            ).joinedload(USB.department)
        )
