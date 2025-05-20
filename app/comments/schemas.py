from app.schemas.base import SBaseModel


class SComment(SBaseModel):
    object_type: str
    object_id: int
    user: str
    text: str
