from fastapi import Query


class ComputersSearchArgsDepend:
    def __init__(
            self,
            department_id: int = Query(None, gt=0),
            is_accepted_usb: bool = None,
    ):
        self.department_id = department_id
        self.is_accepted_usb = is_accepted_usb
