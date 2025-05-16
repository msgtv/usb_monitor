from fastapi import HTTPException

class ObjectNotFound(HTTPException):
    status_code = 404

    def __init__(self, detail: str) -> None:
        super().__init__(detail=detail, status_code=self.status_code)
