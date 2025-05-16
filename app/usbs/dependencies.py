from typing import List, Tuple, Annotated, Optional

from fastapi import Query


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
