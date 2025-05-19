from typing import Literal

from fastapi import Query

from app.tasks.models import Task
from app.computers.models import Computer
from app.usbs.models import USB


class TaskSearchArgsDepend:
    def __init__(
            self,
            computer_id: int = Query(None, gt=0),
            usb_id: int = Query(None, gt=0),
            is_completed: bool = Query(None),
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
            department_id: int = Query(None, gt=0),
            computer_id: int = Query(None, gt=0),
            usb_id: int = Query(None, gt=0),
            is_completed: bool = Query(None),
            usb_sn: str = Query(None, description='Серийный номер USB-устройства')
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


class TaskAddArgsDepend:
    def __init__(
            self,
            action: Literal['accept', 'prohibit'],
            computer_id: int = Query(gt=0),
            usb_id: int = Query(gt=0),
    ):
        self.action = action
        self.computer_id = computer_id
        self.usb_id = usb_id

    @property
    def values(self):
        return {
            'action': self.action,
            'computer_id': self.computer_id,
            'usb_id': self.usb_id,
        }
