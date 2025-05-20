from fastapi import HTTPException

from app.exceptions import ObjectNotFound


class TaskException(HTTPException):
    ...


class TaskNotFound(TaskException, ObjectNotFound):
    ...


class ComputerOrUsbNotFound(TaskException, ObjectNotFound):
    ...
