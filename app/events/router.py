from fastapi import APIRouter
from fastapi_pagination import Page
from fastapi import Depends
from typing import Annotated

from app.dependencies import SessionDepend
from app.events.dao import EventDAO, EventDAODetailed
from app.events.schemas import SEvent, SEventDetail
from app.auth.dependencies import DefaultUser, ManagerUser, AdminUser, RootUser


router = APIRouter(
    prefix="/events",
    tags=["События SNS"],
)

@router.get('', dependencies=[Depends(DefaultUser)])
async def get_events(
        session: SessionDepend,
) -> Page[SEvent]:
    events = await EventDAO.get_all_paginated(session=session)
    return events


@router.get('/detailed', dependencies=[Depends(ManagerUser)])
async def get_events_detailed(
        session: SessionDepend,
) -> Page[SEventDetail]:
    events = await EventDAODetailed.get_all_paginated(session=session)
    return events
