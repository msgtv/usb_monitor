from fastapi import APIRouter
from fastapi_pagination import Page

from app.dependencies import SessionDepend
from app.events.dao import EventDAO, EventDAODetailed
from app.events.schemas import SEvent, SEventDetail


router = APIRouter(
    prefix="/events",
    tags=["События SNS"],
)

@router.get('')
async def get_events(session: SessionDepend) -> Page[SEvent]:
    events = await EventDAO.get_all_paginated(session=session)

    return events


@router.get('/detailed')
async def get_events_detailed(session: SessionDepend) -> Page[SEventDetail]:
    events = await EventDAODetailed.get_all_paginated(session=session)
    return events
