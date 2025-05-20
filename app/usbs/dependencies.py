from typing import Tuple, Annotated

from fastapi import Query, Path

from app.usbs.models import USB


class UsbSearchArgsDepend:
    def __init__(
            self,
            class_type: Tuple[int] = Query(None, description="Класс USB-устройства (например, 1299, 1, 1008)"),
            is_accepted: bool = None,
            department_id: int = Query(None, ge=1),
    ):
        self.class_types = class_type
        self.is_accepted = is_accepted
        self.department_id = department_id
        
    @property
    def filters(self):
        filters = []

        if self.is_accepted is not None:
            filters.append(USB.is_accepted.is_(self.is_accepted))
        if self.department_id is not None:
            filters.append(USB.department_id == self.department_id)
        
        return filters


class UsbManageArgsDepend:
    def __init__(
            self,
            usb_id: Annotated[int, Path(ge=1)],
            is_accepted: bool = None,
            department_id: Annotated[int, Query(ge=1)] = None,
    ):
        self.usb_id = usb_id
        self.is_accepted = is_accepted
        self.department_id = department_id

    @property
    def values(self):
        values = {}
        if self.is_accepted is not None:
            values['is_accepted'] = self.is_accepted
        if self.department_id is not None:
            values['department_id'] = self.department_id

        return values
