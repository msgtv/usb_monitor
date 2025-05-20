from typing import Annotated, Literal, Any

from fastapi import Path, Query, Body

from app.comments.models import Comment
from app.computers.models import Computer
from app.departments.employees.models import Employee
from app.departments.models import Department
from app.events.models import Event
from app.tasks.models import Task
from app.usbs.models import USB


class CommentsSearchArgsDepend:
    def __init__(
            self,
            object_type: Annotated[
                Literal['Department', 'Employee', 'Computer', 'USB', 'Event', 'Task'],
                Query()
            ],
            object_id: Annotated[int, Query(ge=1)] = None,
    ):
        self.object_type = object_type
        self.object_id = object_id

    @property
    def filters(self):
        filters = [Comment.object_type == self.object_type]

        if self.object_id:
            filters.append(Comment.object_id == self.object_id)

        return filters


class CommentsAddArgsDepend:
    def __init__(
            self,
            object_type: Annotated[
                Literal['Department', 'Employee', 'Computer', 'USB', 'Event', 'Task'],
                Body()
            ],
            text: Annotated[str, Body()],
            object_id: Annotated[int, Body(ge=1)] = None,
    ):
        self.object_type = object_type
        self.object_id = object_id
        self.text = text

    @property
    def values(self):
        return {
            'object_type': self.object_type,
            'object_id': self.object_id,
            'text': self.text,
        }
