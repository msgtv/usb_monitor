from typing import Optional

from fastapi_pagination.ext.sqlalchemy import apaginate
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.comments.models import Comment
from app.computers.models import Computer
from app.departments.employees.models import Employee
from app.departments.models import Department
from app.events.models import Event
from app.tasks.models import Task
from app.usbs.models import USB


class CommentDAO(BaseDAO):
    model = Comment

    @classmethod
    def set_order_by(cls, query):
        return query.order_by(cls.model.created_at.desc())

    @classmethod
    async def add_comment(cls, session: AsyncSession, object_type: str, object_id: int, text: str):
        match object_type:
            case 'Department':
                object_type = Department
            case 'Employee':
                object_type = Employee
            case 'Computer':
                object_type = Computer
            case 'USB':
                object_type = USB
            case 'Event':
                object_type = Event
            case 'Task':
                object_type = Task
            case _:
                return None

        get_obj_query = (
            select(object_type)
            .filter_by(id=object_id)
        )

        res = await session.execute(get_obj_query)
        obj = res.scalars().one_or_none()

        if obj is None:
            return None

        new_comment = Comment(
            user='test',  # TODO: username
            text=text,
        )

        new_comment.object = obj

        session.add(new_comment)

        await session.commit()

        return new_comment
