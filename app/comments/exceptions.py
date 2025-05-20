from fastapi import HTTPException
from starlette import status

from app.exceptions import ObjectNotFound

class CommentException(HTTPException):
    ...


class CommentAddException(HTTPException):
    ...


class CommentAddObjectNotFound(ObjectNotFound):
    ...
