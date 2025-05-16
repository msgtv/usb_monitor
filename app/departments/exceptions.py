from fastapi import HTTPException

from app.exceptions import ObjectNotFound


class DepartmentException(HTTPException):
    ...


class DepartmentNotFound(DepartmentException, ObjectNotFound):
    ...
