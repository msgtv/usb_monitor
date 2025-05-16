from fastapi import HTTPException

from app.exceptions import ObjectNotFound


class UsbException(HTTPException):
    ...


class UsbNotFoundException(UsbException, ObjectNotFound):
    ...