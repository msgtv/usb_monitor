from typing import List

from fastapi import APIRouter
from fastapi_pagination import Page

from app.events.dao import EventDAO
from app.events.schemas import SEvent, SEventDetail

router = APIRouter(
    prefix="/events",
    tags=["События SNS"],
)

@router.get('')
async def get_events() -> Page[SEvent]:
    events = await EventDAO.get_all_paginated()

    return events


@router.get('/detailed')
async def get_events_detailed() -> Page[SEventDetail]:
    events = await EventDAO.get_all_paginated_detailed()
    return events
