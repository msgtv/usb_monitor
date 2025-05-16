from fastapi import HTTPException

from app.exceptions import ObjectNotFound


class EmployeeException(HTTPException):
    ...


class EmployeeNotFound(EmployeeException, ObjectNotFound):
    ...
