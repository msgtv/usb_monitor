from fastapi import HTTPException

from app.exceptions import ObjectNotFound

class ComputerException(HTTPException):
    ...


class ComputerNotFoundException(ComputerException, ObjectNotFound):
    ...
