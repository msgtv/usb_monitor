from typing import List

from fastapi import APIRouter

from app.events.dao import EventDAO
from app.events.schemas import SEvent

router = APIRouter(
    prefix="/events",
    tags=["События SNS"],
)

@router.get('')
async def get_events() -> List[SEvent]:
    events = await EventDAO().get_all()

    return events
