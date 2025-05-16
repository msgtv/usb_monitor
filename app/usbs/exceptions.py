from fastapi import HTTPException

class UsbException(HTTPException):
    ...


class UsbNotFoundException(UsbException):
    status_code = 404

    def __init__(self, detail: str):
        super().__init__(status_code=self.status_code, detail=detail)
