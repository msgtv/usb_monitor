from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
