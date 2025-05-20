from typing import List, Annotated

from fastapi import Query, Path
from sqlalchemy import BinaryExpression

from app.computers.models import Computer


class ComputersSearchArgsDepend:
    def __init__(
            self,
            department_id: Annotated[int, Query(gt=0)] = None,
            is_accepted_usb: Annotated[bool, Query()] = None,
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
            computer_id: Annotated[int, Path(ge=1)],
            is_accepted_usb: Annotated[bool, Query()],
    ):
        self.computer_id = computer_id
        self.is_accepted_usb = is_accepted_usb

    @property
    def values(self):
        values = {}
        if self.is_accepted_usb:
            values['is_accepted_usb'] = self.is_accepted_usb

        return values
