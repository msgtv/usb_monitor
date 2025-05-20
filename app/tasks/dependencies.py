from typing import Annotated

from fastapi import Query

from app.tasks.models import Task
from app.computers.models import Computer


class TaskSearchArgsDepend:
    def __init__(
            self,
            computer_id: Annotated[int, Query(ge=1)] = None,
            usb_id: Annotated[int, Query(ge=1)] = None,
            is_completed: Annotated[bool, Query()] = None,
    ):
        self.computer_id = computer_id
        self.usb_id = usb_id
        self.is_completed = is_completed

    @property
    def filters(self):
        filters = []

        if self.computer_id:
            filters.append(Task.computer_id == self.computer_id)
        if self.usb_id:
            filters.append(Task.usb_id == self.usb_id)
        if self.is_completed is not None:
            filters.append(Task.is_completed.is_(self.is_completed))

        return filters


class TaskDetailedSearchArgsDepend(TaskSearchArgsDepend):
    def __init__(
            self,
            department_id: Annotated[int, Query(gt=0)] = None,
            computer_id: Annotated[int, Query(gt=0)] = None,
            usb_id: Annotated[int, Query(gt=0)] = None,
            is_completed: Annotated[bool, Query()] = None,
            usb_sn: Annotated[str, Query(description='Серийный номер USB-устройства')] = None
    ):
        super().__init__(
            computer_id=computer_id,
            usb_id=usb_id,
            is_completed=is_completed,
        )
        self.department_id = department_id
        self.usb_sn = usb_sn

    @property
    def filters(self):
        filters = super().filters

        if self.department_id:
            filters.append(Computer.department_id == self.department_id)
        if self.usb_sn is not None:
            filters.append(Task.usb.has(sn=self.usb_sn))

        return filters

