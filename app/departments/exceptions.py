from fastapi import HTTPException


class DepartmentException(HTTPException):
    ...


class DepartmentNotFound(DepartmentException):
    status_code = 404

    def __init__(self, detail: str):
        super().__init__(detail=detail, status_code=self.status_code)
