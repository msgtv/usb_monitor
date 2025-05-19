from typing import List

from fastapi import Query
from sqlalchemy import BinaryExpression

from app.computers.models import Computer


class ComputersSearchArgsDepend:
    def __init__(
            self,
            department_id: int = Query(None, gt=0),
            is_accepted_usb: bool = None,
    ):
        self.department_id = department_id
        self.is_accepted_usb = is_accepted_usb

    @property
    def filters(self) -> List[BinaryExpression]:
        filters = []

        if self.department_id:
            filters.append(Computer.department_id == self.department_id)
        if self.is_accepted_usb:
            filters.append(Computer.is_accepted_usb.is_(True))

        return filters


class ComputerPatchArgsDepend:
    def __init__(
            self,
            computer_id: int,
            is_accepted_usb: bool,
    ):
        self.computer_id = computer_id
        self.is_accepted_usb = is_accepted_usb

    @property
    def values(self):
        values = {}
        if self.is_accepted_usb:
            values['is_accepted_usb'] = self.is_accepted_usb

        return values
